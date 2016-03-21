# import pyttsx
# engine = pyttsx.init()
# engine.say('Sally sells seashells by the seashore.')
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


# from gtts import gTTS
# tts = gTTS(text='Das ist ein Google TTS Test um zu prüfen wie gut das ganze funktioniert, wenn man auch mal einen längeren text lesen muss. Wie es aussieht schein das ganze aber absolut überhaupt kein Problem darzustellen, es seidenn man lädt das falsche püthon Packet herunter.', lang='de')
# tts.save("hello.mp3")

#need pip install gTTS

from gtts import gTTS


tts = gTTS(text='Das ist ein Test zur direkt Ausgabe', lang='de')
tts.save("temp.mp3")
