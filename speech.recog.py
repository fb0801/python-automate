import speech_recognition as sr



testFile = "testspeech.WAV"

r=sr.Recognizer()


#take file
def recogniseFromFile(filename):
    with sr.AudioFile(filename) as source:
        audio_data =r.record(source)