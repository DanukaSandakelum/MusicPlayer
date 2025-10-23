import pygame
import os
import time
from player_structures import CircularLinkedList, Stack, HuffmanTree




class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = CircularLinkedList()
        self.history = Stack()
        self.is_playing = False
        self.current_song = None

    def load_songs_from_folder(self, folder_path):
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist")
            return
        
        supported_formats = ('.mp3', '.wav', '.ogg')
        songs = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                if f.endswith(supported_formats)]
        
        for song in songs:
            self.playlist.add_song(song)
        
        print(f"Loaded {len(songs)} songs from {folder_path}")
    
    def play(self):
        if self.playlist.get_current_song() is None:
            print("No songs in playlist")
            return
        
        if self.is_playing and self.current_song == self.playlist.get_current_song():
            print("Already playing the current song")
            return
        
        self.current_song = self.playlist.get_current_song()
        pygame.mixer.music.load(self.current_song)
        pygame.mixer.music.play()
        self.is_playing = True
        print(f"Now playing: {os.path.basename(self.current_song)}")
    def pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            print("Music paused")
        else:
            print("No music is playing")


    def unpause(self):
        if not self.is_playing and pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
            self.is_playing = True
            print("Music resumed")
        else:
            print("No music is paused")
    
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        print("Music stopped")
    
    def next_track(self):
        self.history.push(self.playlist.get_current_song())
        next_song = self.playlist.next_song()
        if next_song:
            self.stop()
            self.current_song = next_song
            self.play()
        else:
            print("No next song available")
    
    def previous_track(self):
        if not self.history.is_empty():
            prev_song = self.history.pop()
           
            current = self.playlist.head
            while current.data != prev_song and current.next != self.playlist.head:
                current = current.next
            
            if current.data == prev_song:
                self.playlist.current = current
                self.stop()
                self.current_song = prev_song
                self.play()
            else:
                print("Previous song not found in playlist")
        else:
            print("No previous song in history")
    
    def show_playlist(self):
        print("\nCurrent Playlist:")
        self.playlist.display_playlist()
    
    def show_history(self):
        print("\nPlay History:")
        if self.history.is_empty():
            print("No history available")
        else:
            for i, song in enumerate(reversed(self.history.items)):
                print(f"{i+1}. {os.path.basename(song)}")
    
    def compress_song_name(self, song_path):
        song_name = os.path.basename(song_path)
        huffman = HuffmanTree(song_name)
        compressed = huffman.encode()
        
        original_size = len(song_name) * 8  
        compressed_size = len(compressed)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"\nSong: {song_name}")
        print(f"Original size: {original_size} bits")
        print(f"Compressed size: {compressed_size} bits")
        print(f"Compression ratio: {compression_ratio:.2f}%")
        print(f"Huffman codes: {huffman.codes}")
        
        return compressed