
from gtts import gTTS
import os

# Read English text file
with open("speech.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Check input
if text.strip():

    # Convert English text to English speech
    audio = gTTS(text=text, lang="en", slow=False)

    # Generate MP3 file
    audio.save("speech.mp3")

    print("English audio generated successfully!")

else:
    print("Please enter some text in speech.txt")
