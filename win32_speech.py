import win32com.client

# Calling the Dispatch method of the module which
# interact with microsoft SPeech SDK to speech
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
	print("Enter the word you want to speak")
	s = input()
	while s == 100:
		print(s)
	if s == "exit":
		break
	else:
		speaker.Speak(s)