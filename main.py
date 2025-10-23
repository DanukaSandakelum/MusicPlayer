from music_player import MusicPlayer
import os

def main():
    player = MusicPlayer()
    
    songs_folder = "songs"
    player.load_songs_from_folder(songs_folder)
    
    while True:
        print("\n" + "="*50)
        print("            MUSIC PLAYER")
        print("="*50)
        print("1. Play")
        print("2. Pause")
        print("3. Unpause")
        print("4. Stop")
        print("5. Next Track")
        print("6. Previous Track")
        print("7. Show Playlist")
        print("8. Show History")
        print("9. Compress Current Song Name (Huffman)")
        print("10. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-10): ").strip()
        
        if choice == '1':
            player.play()
        elif choice == '2':
            player.pause()
        elif choice == '3':
            player.unpause()
        elif choice == '4':
            player.stop()
        elif choice == '5':
            player.next_track()
        elif choice == '6':
            player.previous_track()
        elif choice == '7':
            player.show_playlist()
        elif choice == '8':
            player.show_history()
        elif choice == '9':
            current_song = player.playlist.get_current_song()
            if current_song:
                player.compress_song_name(current_song)
            else:
                print("No song selected")
        elif choice == '10':
            player.stop()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    if not os.path.exists("songs"):
        os.makedirs("songs")
        print("Created 'songs' folder. Please add some MP3 files to it.")
    
    main()