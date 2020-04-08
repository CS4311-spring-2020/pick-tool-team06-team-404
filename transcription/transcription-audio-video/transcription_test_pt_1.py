import os
import moviepy.editor as mp #pip install moviepy

path=r'C:/Users/Null/Desktop/SWE2222/vid2txt/trumpcovid.mp4'
##fets a video then outputs the audio to the same folder audio was in
videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
##the line below has something to do with output of the audio file
audioclip.write_audiofile("{}""wav.wav".format(path))