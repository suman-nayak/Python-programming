import speech_recognition as sr
import wikipedia

r = sr.Recognizer()

with sr.Microphone() as m:
    print("Speak...")
    topic = r.recognize_google(r.listen(m))

print("The Topic is:", topic)

print(wikipedia.summary(topic, sentences=3))