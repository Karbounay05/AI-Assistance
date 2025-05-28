import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name} - {voice.id}")

# Choose a different voice here after seeing the list
engine.setProperty('voice', voices[1].id)

# Adjust rate and volume
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()
