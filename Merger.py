#!usr/local/bin/python
import vlc
import playsound
import glob
import sys
import os
from pydub import AudioSegment

dirpath = "downloads/"
includeDir = dirpath + "/Liked from Radio/"
generatedFile = "combined_news_file.mp3"
headingsNewsDir = ""
filenameswithbeep = []
filenames = glob.glob('downloads/Liked from Radio/*.mp3')
combined = AudioSegment.empty()
for filename in filenames:
    audiofilename = AudioSegment.from_mp3(filename)
    filenameswithbeep.extend([audiofilename])

for fname in filenameswithbeep:
    combined += fname
combined.export(generatedFile, format="mp3")


p = vlc.MediaPlayer("combined_news_file.mp3")
p.play()
playsound.playsound('combined_news_file.mp3')
