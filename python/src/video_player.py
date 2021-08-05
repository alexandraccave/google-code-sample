"""A video player class."""

import random
from .video_library import VideoLibrary
from .video_playlist import VideoPlaylist


class VideoPlayer:

    def __init__(self):

        self.video_library = VideoLibrary()
        self.playlists = []
        self.video_playing = None
        self.is_paused = False

    def number_of_videos(self):
        num_videos = len(self.video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        all_videos = self.video_library.get_all_videos()

        all_videos_sorted = sorted(self.video_library.get_all_videos(), key=lambda video: video.name)

        print("Here's a list of all available videos:")

        for i in range(len(all_videos_sorted)) :
            # print(all_videos_sorted[i].name, "(" + all_videos_sorted[i]._video_id + ")", all_videos_sorted[i]._tags)
            print("\t" + all_videos_sorted[i].name, "(" + all_videos_sorted[i].id + ")", "[" + " ".join(all_videos_sorted[i].tags) + "]")
            ++i

    def play_video(self, video_id):
        """Plays the respective video."""

        video_id_selected = video_id
        all_videos = self.video_library.get_all_videos()

        """Compare video_id_selected against video library"""
        video_exists = False
        for i in range(len(all_videos)) :
            if video_id_selected == all_videos[i].id :
                video_exists = True
                break

        if video_exists == False :
            print("Cannot play video: Video does not exist")
            return

        """Fetch the video from the library"""
        video_selected = self.video_library.get_video(video_id)

        """Set the video playing to the video selected"""
        if self.video_playing != None :
            print("Stopping video: " + self.video_playing.name)

        self.video_playing = video_selected
        self.is_paused = False
        print("Playing video: " + self.video_playing.name)

    def stop_video(self):
        """Stops the current video."""

        if self.video_playing == None :
            print("Cannot stop video: No video is currently playing")
        else :
            print("Stopping video: " + self.video_playing.name)
            self.video_playing = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        all_videos = self.video_library.get_all_videos()

        video_selected = all_videos[random.randint(0, len(self.video_library.get_all_videos()))]

        self.play_video(video_selected.id)

    def pause_video(self):
        """Pauses the current video."""

        if self.video_playing == None :
            print("Cannot pause video: No video is currently playing")
            return
        else :
            if self.is_paused == False :
                print ("Pausing video: " + self.video_playing.name)
                self.is_paused = True
                return
            if self.is_paused == True :
                print ("Video already paused: " + self.video_playing.name)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_playing == None :
            print("Cannot continue video: No video is currently playing")
            return
        else :
            if self.is_paused == False :
                print("Cannot continue video: Video is not paused")
                return
            if self.is_paused == True :
                print("Continuing video: " + self.video_playing.name)
                self.is_paused = False
                return

    def show_playing(self):
        """Displays video currently playing."""
        if self.video_playing != None :
            if self.is_paused == False :
                print("Currently playing: " + self.video_playing.name + " "
                                            + "(" + self.video_playing.id + ")" + " "
                                            + "[" + " ".join(self.video_playing.tags) + "]" )
            if self.is_paused == True :
                print("Currently playing: " + self.video_playing.name + " "
                                            + "(" + self.video_playing.id + ")" + " "
                                            + "[" + " ".join(self.video_playing.tags) + "]" + " "
                                            + "- PAUSED" )

        if self.video_playing == None :
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name."""

        # Checks whether a playlist has already been created yet
        if self.playlists != None :

            # Checks whether a playlist with the same name already exists
            for i in range(len(self.playlists)) :
                if playlist_name.casefold() == self.playlists[i].name.casefold() :
                    print("Cannot create playlist: A playlist with the same name already exists")
                    return

        # Create new playlist
        new_playlist = VideoPlaylist(playlist_name)

        # Adds the new playlist to the list of playlists
        self.playlists.append(new_playlist)
        print ("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):

        # 1. Find video
        video = self.video_library.get_video(video_id)
        if video == None :
            print("Cannot add video to " + playlist_name + ": Video does not exist")
            return

        # Find playlist
        for i in range(len(self.playlists)) :
            if self.playlists[i].name == playlist_name :

                # Check if playlist is empty
                if self.playlists[i] != None :

                    # If playlist is not empty check if video is already in playlist
                    for j in range(len(self.playlists[i].playlist)) :
                        if video.name == self.playlists[i].playlist[j].name :
                            print("Cannot add video to " + playlist_name + ": Video already added")
                            return

                # Otherwise add video to playlist
                self.playlists[i].playlist.append(video)
                print("Added video to " + playlist_name + ": " + video.name)

            else :
                print("Cannot add video to " + playlist_name + ": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        # Check whether playlists exist yet
        if self.playlists == None :
            print("No playlists exist yet")

        else :

            ordered_playlists = sorted(self.playlists, key=lambda playlist: playlist.name)

            print("Showing all playlists:")
            for i in range(len(self.playlists)) :
                print("\t" + ordered_playlists[i].name)
                ++i

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name."""

        if self.playlists == None :
            print("No playlists exist yet")
            return

        if self.playlists != None :
            for i in range(len(self.playlists)) :
                if playlist_name == self.playlists[i].name :
                    print("Showing playlist:" + self.playlists[i].name)
                    selected_playlist = self.playlists[i]
                    # Iterate through playlist names
                    for j in range(len(selected_playlist.playlist)) :
                        print("\t" + selected_playlist.playlist[j].name)


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose names contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
