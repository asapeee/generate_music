# from audiocraft.models import musicgen
# from audiocraft.utils.notebook import display_audio
import torch
import scipy
import datetime
from weather_api import get_weather
from chatgpt_api import get_chatgpt_response
from playsound import playsound
import glob, re, os, shutil


def play_music(playlist):
    for music in playlist:
        playsound(music)



if __name__ == '__main__':
    shutil.rmtree("G:\マイドライブ\generate_music\playlist") 
    os.mkdir("G:\マイドライブ\generate_music\playlist")
    while 1:
        print(f'The number of music is {len(os.listdir("G:/マイドライブ/generate_music/playlist"))}')
        if len(os.listdir("G:/マイドライブ/generate_music/playlist")):
            playlist = glob.glob("G:/マイドライブ/generate_music/playlist/*.mp3")
            playlist = sorted(playlist, key=str.lower, reverse=True)
            print(playlist)
            play_music(playlist)
        else:
            print("There is no playlist.")