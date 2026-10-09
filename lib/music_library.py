class MusicLibrary:
    def __init__(self):
        self.tracks = []
        # Parameters:
        #   name: string
        # Side effects:
        #   none
        # No code here yet

    def add_track(self, track):
        if type(track) != str:
            raise TypeError("String expected for track")
        
        self.tracks.append(track)

        
        # Parameters:
        #   tracks: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self.tracks list
        # No code here yet

    def see_tracks(self):
        # Returns:
        #   A list of all tracks in the tracks library
        # Side-effects:
        #   none
         # No code here yet
         return self.tracks
