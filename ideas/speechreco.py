#needs: https://pypi.python.org/pypi/SpeechRecognition/
#and pyAudio

import speech_recognition as sr


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
    # instead of `r.recognize_google(audio, show_all=True)`
    from pprint import pprint
    print("Google Speech Recognition results:")
    pprint(r.recognize_google(audio, show_all=True, language = "de-DE")) # pretty-print the recognition result
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
