# Playlist Management System

class Song:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.artist}\nDuration: {self.duration}\nGenre: {self.genre}"

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class PlaylistManager:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.current_song = None

    def add_song(self, title, artist, duration, genre):
        # Create a new Song instance with the args
        new_song = Song(title, artist, duration, genre)
        # Create a node with the Song
        new_node = Node(new_song)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            new_node.prev = node

    def remove_song(self, title):
        if self.head is None:
            print(f"The playlist '{self.name}' is empty")
            return
        # If the first node is the node we are trying to removing
        if self.head.song.title == title:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            # If the new head is a node
            if self.head:
                self.head.prev = None
            return
        # Start at the first node
        current_node = self.head
        # While the current node is not None
        while current_node:
            # If the current node is the one we are trying to remove
            if current_node.song.title == title:
                # Adjust the pointers
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{title} is not in the '{self.name}' playlist.")

    def play_next(self):
        # If there is no current song
        if self.current_song is None:
            # Set the current song to the first song in the playlist
            self.current_song = self.head
        # if there is
        else:
            # Set the current song to the next song
            self.current_song = self.current_song.next
        # Make sure that the new current song exists
        if self.current_song is not None:
            song = self.current_song.song
            print(f"Currently Playing: {song}")
        # if self.current_song is None
        else:
            print(f"At the end of the '{self.name}' playlist")

    def go_back(self):
        if self.current_song is None:
            print('Cannot go back. At the beginning of the playlist')
        else:
            self.current_song = self.current_song.prev
            if self.current_song is not None:
                song = self.current_song.song
                print(f"Currently Playing: {song}")
            # if self.current_song is None
            else:
                print(f"At the beginning of the '{self.name}' playlist")


print('='*150)

workout_warriors = PlaylistManager("Workout Warriors")

# Add songs to the playlist
workout_warriors.add_song("Start Me Up", "The Rolling Stones", "3:33", "Rock")
workout_warriors.add_song("Thunderstruck", "AC/DC", "4:52", "Rock")
workout_warriors.add_song("Crank That (Soulja Boy)", "Soulja Boy", "3:41", "Hip-Hop")
workout_warriors.add_song("Seven Nation Army", "The White Stripes", "3:59", "Rock")


workout_warriors.play_next()
workout_warriors.play_next()
workout_warriors.play_next()

workout_warriors.go_back()
workout_warriors.go_back()
workout_warriors.go_back()