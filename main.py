from gtts import gTTS
import os
import pygame

def text_to_speech(text, lang='en', download_only=False):
    try:
        tts = gTTS(text=text, lang=lang)
        if download_only:
            filename = input("Enter the filename to save: ")
            tts.save(filename + ".mp3")
            print(f"Speech saved as {filename}.mp3")
        else:
            tts.save("output.mp3")
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("output.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            pygame.mixer.quit()
            pygame.quit()
            os.remove("output.mp3")  # Remove the temporary audio file
    except Exception as e:
        print("Error occurred:", e)

while True:
    text = input("Enter text to convert to speech: ")
    option = input("Enter 'play' to play the speech or 'download' to save as an MP3 file. Enter 'exit' to quit: ").lower()

    if option == 'play':
        text_to_speech(text)
    elif option == 'download':
        text_to_speech(text, download_only=True)
    elif option == 'exit':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please enter 'play', 'download', or 'exit'.")
