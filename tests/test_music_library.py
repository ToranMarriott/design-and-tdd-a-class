from lib.music_library import *

def test_music_library_initialises_with_empty_list():
    library = MusicLibrary()
    assert library.tracks == []

def test_add_song_appends_track_to_tracks_list():
    library = MusicLibrary()
    library.add_track("Thriller")
    assert library.tracks == ["Thriller"]