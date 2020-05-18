import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	print('Speak Anything: ')
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		print('You said: {}'.format(text))
	except:
		print('Sorry could not recognize your voice')	
		
		
		
song = AudioSegment.from_wav(path)
fh = open('recognized.txt', 'w')
silence = AudioSegment.silent(duration = 10)
audio = silence + song + silence

r = sr.Recognizer()

with sr.AudioFile(path) as source:

	r.adjust_for_ambient_noise(source)
    audio_listened = r.listen(source)

	try:
		text = r.recognize_google(audio)
		print('You said: {}'.format(text))
		th.write(text + '.')
	except:
		print('Sorry could not recognize your voice')	
