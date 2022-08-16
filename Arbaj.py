# importing required modules

from pygame import mixer
from tkinter import *
import os


def play_song():
    current_song = playlist.get(ACTIVE)
    print("now playing  :  " + current_song)
    mixer.music.load(current_song)
    song_status.set("Playing Music")
    mixer.music.play()


def pause_song():
    if (song_status.get() != "Music Paused"):
        song_status.set("Music Paused")
        print(song_status.get())
    mixer.music.pause()


def stop_song():
    if (song_status.get() != "Music Stopped"):
        song_status.set("Music stopped")
        print(song_status.get())
    mixer.music.stop()


def resume_song():
    if (song_status.get() != "Resuming Music"):
        song_status.set("Resuming Music")
        print(song_status.get())
    mixer.music.unpause()


# window for music playing

music_window = Tk()
music_window.geometry('800x400')
music_window.config(bg='SlateGray3')
music_window.resizable(1, 1)
music_window.title('Arbaj Music player project')

mixer.init()
song_status = StringVar()
song_status.set("choosing")

# playlist---------------

playlist = Listbox(music_window, selectmode=SINGLE, bg="white", fg="black", font=('arial', 15), height=10, width=100)
playlist.grid(columnspan=4)

#    accessing the music from local storage

os.chdir(r'C:\16.08.2022\songs')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

#      designing the buttons

play_button = Button(music_window, text="play", command=play_song)
play_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
play_button.grid(row=1, column=0)

pause_button = Button(music_window, text="Pause", command=pause_song)
pause_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
pause_button.grid(row=1, column=1)

stop_button = Button(music_window, text="Stop", command=stop_song)
stop_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
stop_button.grid(row=2, column=0)

Resume_button = Button(music_window, text="Resume", command=resume_song)
Resume_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
Resume_button.grid(row=2, column=1)

mainloop()
print("music interface Ended.")
