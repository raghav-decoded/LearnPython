'''
https://pypi.org/project/pyttsx3/
 to run the speech we use runAndWait() 
 All the say() texts won’t be said unless the interpreter encounters runAndWait().
'''
# def speak(str):
#       from win32com.client import Dispatch
#       speak=Dispatch(“SAPI.SpVoice”)
#       speak.Speak(str)
# if __name__= ’__main__’:
#      speak(“You are the best my friend”)

# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

#setting apple voice
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# newVoiceRate ~ Slow rate 
newVoiceRate = 155
engine.setProperty('rate',newVoiceRate)

# testing
def speak(str):
      engine.say(str)
      engine.runAndWait()

if __name__ == '__main__':
      speak("Hello, my name is python and I hate C++")
