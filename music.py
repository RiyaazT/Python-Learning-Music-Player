import sys
from os import path
from pygame import mixer
import dearpygui.dearpygui as dpg


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)
    

#Defines the button functions
def play_song(sender, app_data, user_data):
    mixer.music.play()

def pause_song(sender, app_data, user_data):
    mixer.music.pause()

def resume_song(sender, app_data, user_data):
    mixer.music.unpause()

def set_volume(sender, app_data, user_data):
    mixer.music.set_volume(app_data)

def exit_app(sender, app_data, user_data):
    mixer.music.stop()
    dpg.stop_dearpygui()

#Starts the music player, loads the song, and starts it at a half volume because my computer is loud
#The load function reads from music stored in the 'Songs' folder, future versions will have the ability to browse and add folders
mixer.init()
song_path = resource_path("Songs/music.mp3")
mixer.music.load(song_path)
mixer.music.set_volume(0.5)

#creates the dearpygui window, and adds buttons. Future versions will have Play/Resume work on the same function without restarting the song
dpg.create_context()

with dpg.window(label="Winamp v1"):
    dpg.add_button(label="Play", callback=play_song)
    dpg.add_button(label="Pause", callback=pause_song)
    dpg.add_button(label="Resume", callback=resume_song)
    dpg.add_slider_float(label="Volume", default_value=0.5, min_value=0.0, max_value=1.0, callback=set_volume)
    dpg.add_button(label="Exit", callback=exit_app)    

dpg.create_viewport(title='This is not a rickroll', width=800, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
