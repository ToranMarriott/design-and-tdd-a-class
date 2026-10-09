from lib.music_library import *
import pytest

def test_music_library_initialises_with_empty_list():
    library = MusicLibrary()
    assert library.tracks == []

def test_add_song_appends_track_to_tracks_list():
    library = MusicLibrary()
    library.add_track("Thriller")
    assert library.tracks == ["Thriller"]

def test_error_when_add_perameter_not_a_string():
    library = MusicLibrary()
    with pytest.raises(TypeError) as e:
        library.add_track(5)
    assert str(e.value) == "String expected for track"

def test_add_song_appends_multiple_tracks():
    library = MusicLibrary()
    library.add_track("Thriller")
    library.add_track("Dancin' in the Rain")
    library.add_track("Man in the Mirror")
    assert library.tracks  == ["Thriller", "Dancin' in the Rain", "Man in the Mirror"]

def test_see_tracks_returns_list_of_tracks():
    library = MusicLibrary()
    assert library.see_tracks() == []
    library.add_track("Thriller")
    library.add_track("Dancin' in the Rain")
    library.add_track("Man in the Mirror")
    assert library.see_tracks()  == ["Thriller", "Dancin' in the Rain", "Man in the Mirror"]