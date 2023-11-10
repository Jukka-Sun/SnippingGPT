import os
from voiceover import create_voiceover, save_mp3, play_mp3
from image import analyze_image_with_gpt4, encode_image
from snipping import capture_screenshot

# Your OpenAI API key
api_key = "OPENAI-API_KEY" # Replace with your API key

if __name__ == "__main__":
    screenshot_path = capture_screenshot()
    if screenshot_path:
        analysis_result = analyze_image_with_gpt4(screenshot_path, api_key)
        text_description = analysis_result['choices'][0]['message']['content']
        audio_data = create_voiceover(text_description, api_key)

        voiceovers_dir = '/Users/jukson/Documents/GPT/SnippingGPT/voiceovers'
        if not os.path.exists(voiceovers_dir):
            os.makedirs(voiceovers_dir)
        audio_file_path = os.path.join(voiceovers_dir, 'voiceover.mp3')
        
        save_mp3(audio_data, audio_file_path)
        play_mp3(audio_file_path)
