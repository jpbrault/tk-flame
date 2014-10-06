# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

def preCustomExport(info, userData):
    """
    Hook called before a custom export begins. The export will be blocked
    until this function returns. This can be used to fill information that would
    have normally been extracted from the export window.
    
    :param info: Dictionary with info about the export. Contains the keys
                 - destinationHost: Host name where the exported files will be written to.
                 - destinationPath: Export path root.
                 - presetPath: Path to the preset used for the export.
                 - abort: Pass True back to flame if you want to abort
                 - abortMessage: Abort message to feed back to client
                 
    :param userData: Dictionary that could have been populated by previous export hooks and that
                     will be carried over into the subsequent export hooks.
                     This can be used by the hook to pass black box data around.
    """
    
    # first, get the toolkit engine
    import sgtk
    engine = sgtk.platform.current_engine()

    # get the preset that the user selected from the menu
    current_preset = userData.get("preset_title")

    # create a session object in the engine - this is how we keep track of what is going on
    session_id = engine.create_export_session(current_preset)
    userData["session_id"] = session_id

    # tell the engine to dispatch the request to the correct toolkit app
    engine.trigger_export_callback(session_id, "preCustomExport", info)

   
 
def preExportSequence(info, userData):
    """
    Hook called before a sequence export begins. The export will be blocked
    until this function returns.
    
    :param info: Information about the export. Contains the keys      
                 - destinationHost: Host name where the exported files will be written to.
                 - destinationPath: Export path root.
                 - sequenceName: Name of the exported sequence.
                 - shotNames: Tuple of all shot names in the exported sequence. 
                              Multiple segments could have the same shot name.
                 - abort: Hook can set this to True if the export sequence process should
                          be aborted. If other sequences are exported in the same export session
                          they will still be exported even if this export sequence is aborted.
                 - abortMessage: Error message to be displayed to the user when the export sequence
                                 process has been aborted.
    
    :param userData: Dictionary that could have been populated by previous export hooks and that
                     will be carried over into the subsequent export hooks.
                     This can be used by the hook to pass black box data around.    
    """
    # first, get the toolkit engine
    import sgtk
    engine = sgtk.platform.current_engine()

    # check if there is a toolkit export session currently 
    # progressing - in that case dispatch it to the appropriate app
    session_id = userData.get("session_id")
    if session_id:
        engine.trigger_export_callback(session_id, "preExportSequence", info)        


def preExportAsset(info, userData):
    """    
    Hook called before an asset export starts. The export will be blocked
    until this function returns.
    
    :param info: Dictionary with a number of parameters:
    
       destinationHost: Host name where the exported files will be written to.
       destinationPath: Export path root.
       namePattern:     List of optional naming tokens.
       resolvedPath:    Full file pattern that will be exported with all the tokens resolved.
       name:            Name of the exported asset.
       sequenceName:    Name of the sequence the asset is part of.
       shotName:        Name of the shot the asset is part of.
       assetType:       Type of exported asset. ( 'video', 'audio', 'batch', 'openClip', 'batchOpenClip' )
       width:           Frame width of the exported asset.
       height:          Frame height of the exported asset.
       aspectRatio:     Frame aspect ratio of the exported asset.
       depth:           Frame depth of the exported asset. ( '8-bits', '10-bits', '12-bits', '16 fp' )
       scanFormat:      Scan format of the exported asset. ( 'FILED_1', 'FIELD_2', 'PROGRESSIVE' )
       fps:             Frame rate of exported asset.
       sequenceFps:     Frame rate of the sequence the asset is part of.
       sourceIn:        Source in point in frame and asset frame rate.
       sourceOut:       Source out point in frame and asset frame rate.
       recordIn:        Record in point in frame and sequence frame rate.
       recordOut:       Record out point in frame and sequence frame rate.
       track:           ID of the sequence's track that contains the asset.
       trackName:       Name of the sequence's track that contains the asset.
       segmentIndex:    Asset index (1 based) in the track.
       versionName:     Current version name of export (Empty if unversioned).
       versionNumber:   Current version number of export (0 if unversioned).
    
    :param userData: Dictionary that could have been populated by previous export hooks and that
                     will be carried over into the subsequent export hooks.
                     This can be used by the hook to pass black box data around.

    """
    # first, get the toolkit engine
    import sgtk
    engine = sgtk.platform.current_engine()

    # check if there is a toolkit export session currently 
    # progressing - in that case dispatch it to the appropriate app
    session_id = userData.get("session_id")
    if session_id:
        engine.trigger_export_callback(session_id, "preExportAsset", info)        


 
def postExportAsset(info, userData):
    """    
    Hook called after an asset export ends. The export will be blocked
    until this function returns.
    
    :param info: Dictionary with a number of parameters:
    
       destinationHost: Host name where the exported files will be written to.
       destinationPath: Export path root.
       namePattern:     List of optional naming tokens.
       resolvedPath:    Full file pattern that will be exported with all the tokens resolved.
       name:            Name of the exported asset.
       sequenceName:    Name of the sequence the asset is part of.
       shotName:        Name of the shot the asset is part of.
       assetType:       Type of exported asset. ( 'video', 'audio', 'batch', 'openClip', 'batchOpenClip' )
       isBackground:    True if the export of the asset happened in the background.
       backgroundJobId: Id of the background job given by the backburner manager upon submission. 
                        Empty if job is done in foreground.
       width:           Frame width of the exported asset.
       height:          Frame height of the exported asset.
       aspectRatio:     Frame aspect ratio of the exported asset.
       depth:           Frame depth of the exported asset. ( '8-bits', '10-bits', '12-bits', '16 fp' )
       scanFormat:      Scan format of the exported asset. ( 'FILED_1', 'FIELD_2', 'PROGRESSIVE' )
       fps:             Frame rate of exported asset.
       sequenceFps:     Frame rate of the sequence the asset is part of.
       sourceIn:        Source in point in frame and asset frame rate.
       sourceOut:       Source out point in frame and asset frame rate.
       recordIn:        Record in point in frame and sequence frame rate.
       recordOut:       Record out point in frame and sequence frame rate.
       track:           ID of the sequence's track that contains the asset.
       trackName:       Name of the sequence's track that contains the asset.
       segmentIndex:    Asset index (1 based) in the track.       
       versionName:     Current version name of export (Empty if unversioned).
       versionNumber:   Current version number of export (0 if unversioned).
    
    :param userData: Dictionary that could have been populated by previous export hooks and that
                     will be carried over into the subsequent export hooks.
                     This can be used by the hook to pass black box data around.
    """
    # first, get the toolkit engine
    import sgtk
    engine = sgtk.platform.current_engine()

    # check if there is a toolkit export session currently 
    # progressing - in that case dispatch it to the appropriate app
    session_id = userData.get("session_id")
    if session_id:
        engine.trigger_export_callback(session_id, "postExportAsset", info)        
   
 
def postCustomExport(info, userData):
    """
    Hook called after a custom export ends. The export will be blocked
    until this function returns.
    
    :param info: Information about the export. Contains the keys      
                 - destinationHost: Host name where the exported files will be written to.
                 - destinationPath: Export path root.
                 - presetPath: Path to the preset used for the export.
    
    :param userData: Dictionary that could have been populated by previous export hooks and that
                     will be carried over into the subsequent export hooks.
                     This can be used by the hook to pass black box data around.
    """
    # first, get the toolkit engine
    import sgtk
    engine = sgtk.platform.current_engine()

    # check if there is a toolkit export session currently 
    # progressing - in that case dispatch it to the appropriate app
    session_id = userData.get("session_id")
    if session_id:
        engine.trigger_export_callback(session_id, "postCustomExport", info)

def getCustomExportProfiles(profiles):
    """
    Hook returning the custom export profiles to display to the user in the
    contextual menu.

    :param profiles: A dictionary of userData dictionaries where 
                     the keys are the name of the profiles to show in contextual menus.
    """
    import sgtk
    engine = sgtk.platform.current_engine()
    
    for preset_title in engine.get_export_presets(): 
        profiles[preset_title] = {"preset_title": preset_title}
    