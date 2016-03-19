#-*- encoding: utf-8 -*-
"""
Speech Recognition Modul for MirrorOS
using the Python Libary SpeechRecognition
you must install SpeechRecognition and pyAudio
- pip install SpeechRecognition
- pip install pyaudio
Autor: Bastian Schroll
"""

from tkinter import *
import logging
import speech_recognition as sr

from inc.modul import modul

class speech(modul):
    def __init__(self, window, config, xPos, yPos, anc="nw"):
        modul.__init__(self, __name__) #load modul container
        self.window = window
        self.config = config

        try:

            ##############
            # init section

            pass

            # init section
            ##############

        except:
            logging.exception("cannot load %s", __name__)


    def main(self):

        while 1: #infinite loop from thread - on exit, thread dies
            try:

                ##############
                # code section

                r = sr.Recognizer()

                with sr.Microphone() as source:
                    #r.adjust_for_ambient_noise(source)
                    #r.pause_threshold = 0.5
                    logging.debug("listen for speech")
                    audio = r.listen(source)

                # recognize speech using Google Speech Recognition
                try:
                    logging.debug("process spech")
                    self.speech_data = r.recognize_google(audio, show_all=False, language = "de-DE")
                    logging.debug("You said: "+ self.speech_data)

                    if self.speech_data == "beenden" or self.speech_data == "ende":
                        self.window.quit()

                except sr.UnknownValueError:
                    logging.debug("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    logging.error("Could not request results from Google Speech Recognition service; {0}".format(e))

                # code section
                ##############

            except:
                logging.exception("cannot update %s", __name__)
            finally:
                #self.wait(1)
                pass
