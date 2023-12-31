import os
import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
from pygame import mixer

col1 = "#ffffff"
col2 = "#3C1DC6"
col3 = "#333333"
col4 = "#CFC7F8"

window = tk.Tk()
window.title("Music Player")
window.geometry("352x255")
window.configure(background=col1)
window.resizable(width=False, height=False)

def play_music():
    running = listbox.get(tk.ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def cont_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    if new_index >= len(songs):
        new_index = 0  # Loop to the beginning if at the end of the list
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.selection_clear(0, tk.END)
    listbox.select_set(new_index)
    running_song['text'] = playing

def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    if new_index < 0:
        new_index = len(songs) - 1  # Loop to the end if at the beginning of the list
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.selection_clear(0, tk.END)
    listbox.select_set(new_index)
    running_song['text'] = playing

left_frame = tk.Frame(window, width=150, height=150, bg=col1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = tk.Frame(window, width=250, height=150, bg=col3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = tk.Frame(window, width=400, height=100, bg=col4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

listbox = tk.Listbox(right_frame, selectmode=tk.SINGLE, font=("Arial 9 bold"), width=22, bg=col3, fg=col1)
listbox.grid(row=0, column=0)

w = tk.Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

img_1 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-music-100.png")
img_1 = img_1.resize((130, 130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = tk.Label(left_frame, height=130, image=img_1, padx=10, bg=col1)
app_image.place(x=10, y=15)

img_2 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-circled-play-100.png")
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = tk.Button(down_frame, width=40, height=40, image=img_2, padx=10, bg=col1, font=('Ivy 10'), command=play_music)
play_button.place(x=56 + 28, y=35)

img_3 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-rewind-100.png")
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = tk.Button(down_frame, width=40, height=40, image=img_3, padx=10, bg=col1, font=('Ivy 10'), command=previous_music)
prev_button.place(x=10 + 28, y=35)

img_4 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-fast-forward-100.png")
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = tk.Button(down_frame, width=40, height=40, image=img_4, padx=10, bg=col1, font=('Ivy 10'), command=next_music)
next_button.place(x=102 + 28, y=35)

img_5 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-pause-100.png")
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = tk.Button(down_frame, width=40, height=40, image=img_5, padx=10, bg=col1, font=('Ivy 10'), command=pause_music)
pause_button.place(x=148 + 28, y=35)

img_6 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-resume-button-100.png")
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
cont_button = tk.Button(down_frame, width=40, height=40, image=img_6, padx=10, bg=col1, font=('Ivy 10'), command=cont_music)
cont_button.place(x=194 + 28, y=35)

img_7 = Image.open("C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\code\\icons8-stop-circled-100.png")
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = tk.Button(down_frame, width=40, height=40, image=img_7, padx=10, bg=col1, font=('Ivy 10'), command=stop_music)
stop_button.place(x=240 + 28, y=35)

line = tk.Label(left_frame, width=200, height=1, padx=10, bg=col3)
line.place(x=0, y=1)

line = tk.Label(left_frame, width=200, height=1, padx=10, bg=col1)
line.place(x=0, y=3)

running_song = tk.Label(down_frame, text='Choose a song!', font=('Ivy 10'), width=44, height=1, padx=10, bg=col1, fg=col3, anchor=tk.NW)
running_song.place(x=0, y=1)

# Change the directory to the location of your music files
os.chdir(r"C:\\Users\\Abhiram Kurra\\Desktop\\Internship\\Code_Clause\\Music Player_Demo\\Music")
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(tk.END, i)

show()

mixer.init()
music_state = StringVar()
music_state.set("Choose One!")


window.mainloop()
