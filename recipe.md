# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicLibrary:

    def __init__(self):
        self.tracks = []
        # Parameters:
        #   name: string
        # Side effects:
        #   none
        pass # No code here yet

    def add_track(self, track):
        # Parameters:
        #   tracks: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self.tracks list
        pass # No code here yet

    def see_tracks(self):
        # Returns:
        #   A list of all tracks in the tracks library
        # Side-effects:
        #   none
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
test that tracks initialises an empty list as tracks
"""
library = MusicLibrary()
library.tracks # => empty list

"""
test that given a song, add_track() appends the song to the tracks list
"""
library = MusicLibrary()
library.add_track("Thriller")
library.tracks # => ["Thriller"]

"""
throw typeerror if track param is not string 
"""
library = MusicLibrary()
library.add_track(True)
assert error_message # => TypeError: string expected for track

"""
test that multiple tracks rendered into a longer list as a result of add_track being called multiple times
"""
library = MusicLibrary()
library.add_track("Thriller")
library.add_track("Dancin' in the Rain")
library.add_track("Man in the Mirror")
library.tracks # => ["Thriller", "Dancin' in the Rain", "Man in the Mirror"]

"""
test that multiple tracks rendered into a longer list as a result of add_track being called multiple times and then see_track called
"""
library = MusicLibrary()
library.see_tracks() => []
library.add_track("Thriller")
library.add_track("Dancin' in the Rain")
library.add_track("Man in the Mirror")
library.see_tracks() # => ["Thriller", "Dancin' in the Rain", "Man in the Mirror"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
