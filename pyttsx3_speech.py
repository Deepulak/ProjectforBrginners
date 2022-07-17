import pyttsx3

# initialize pyttsx3 or create object
bot = pyttsx3.init()
# passing input text to be spoken in say method
bot.say("Hello World")
bot.say("Welcome to the Dark")
# run and wait method, processes the voice commands.
bot.runAndWait()