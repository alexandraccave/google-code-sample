"""A video playlist class."""

from .video_library import VideoLibrary
from .video import Video


class VideoPlaylist:

    def __init__(self, playlist_name) :

        self.name = playlist_name
        self.playlist = []

    @property
    def video_playlist(self) :
        return self

    @property
    def name(self) :
        return self.name

    def get_playlist(self, video_id):
        """Returns the video object (title, url, tags) from the video library.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self.videos.get(video_id, None)

    def get_video_from_playlist(self, video_id) :

        return self.video.get(video_id, None)

    def get_all_videos(self) :

        return self.playlist

    def add_to_playlist(self, video) :
        self.playlist.append(video)
        print("Added video to playlist")
