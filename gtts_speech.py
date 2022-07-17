from gtts import gTTS
import os

# The text that you want to convert 
mytext = "Welcome to the Dark"

# Language in which you want to convert
language = "en"

# Saving the converted audio in a mp3 file
# named welcome
tts.save("welcome.mp3")

# playing the converted file
os.system("mpg321 welcome.mp3")