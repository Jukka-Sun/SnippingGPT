import requests
import pygame

# Function to create a voiceover from the text response
def create_voiceover(text, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "tts-1",
        "input": text,
        "voice": "onyx",
    }

    response = requests.post("https://api.openai.com/v1/audio/speech", headers=headers, json=payload)
    return response.content

# Function to save the MP3 data to a file
def save_mp3(data, file_path):
    with open(file_path, 'wb') as file:
        file.write(data)

# Function to play the MP3 file
def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
