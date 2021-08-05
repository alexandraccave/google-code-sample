"""A playlist library class"""

from .video_library import VideoLibrary
from .video import Video


class PlaylistLibrary :

    def __init__(self) :

        playlists = []

    def get_playlist(self, playlist_name)
        for i in self :
            if playlist_name == self.playlists[i].name() :
                print("Found playlist")
                return self.playlists[i]
            else :
                print("Could not find playlist")
