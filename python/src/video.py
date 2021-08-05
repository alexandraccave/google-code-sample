"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_name: str, video_id: str, video_tags: Sequence[str]) :

        self.name = video_name # This does not work
        self.id = video_id # This fucking works for some reason

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self.tags = tuple(video_tags) # This also does not work

    @property
    def video_name(self) -> str:
        """Returns the name of a video."""
        return self.name

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self.id

    @property
    def video_tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self.tags

    @property
    def get_tags(self) -> str:
        tags = ''.join(self.tags)
        return tags
