# SnippingGPT

SnippingGPT is a Python-based tool that integrates screenshot capturing with OpenAI's powerful GPT-4 model to analyze images and generate descriptive voiceovers.

## Features

- **Screenshot Capture**: Allows users to select and capture any area on their screen.
- **Image Analysis**: Utilizes OpenAI's GPT-4 Vision API to analyze screenshots and provide context or descriptions of the captured image.
- **Voiceover Generation**: Leverages OpenAI's GPT-4 Text-to-Speech API to convert the image analysis text into a spoken voiceover.
- **Automatic Playback**: Plays the generated voiceover automatically upon creation.
- **Local Storage**: Saves both screenshots and voiceovers locally for easy access and reference.

## How to Use

To use SnippingGPT, follow these steps:

1. **Clone the repository**:

    ```
    git clone https://github.com/Jukka-Sun/SnippingGPT.git
    ```

2. **Navigate to the project directory**:

    ```
    cd SnippingGPT
    ```

3. **Install dependencies**:

    ```
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**:

    OpenAI API key is required to authenticate requests. Replace `YOUR_OPENAI_API_KEY` with your actual key in `main.py`.

    ```python
    # Your OpenAI API key
    api_key = "YOUR_OPENAI_API_KEY"
    ```

    Alternatively, you can set it as an environment variable:

    ```
    export OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
    ```

5. **Run the program**:

    ```
    python3 main.py
    ```

6. **Capture a screenshot**: Follow the on-screen instructions to select and capture a portion of the screen.

7. **Listen to the voiceover**: After the image analysis, the voiceover will automatically be played.

## Directory Structure

- `screenshots/`: This directory will contain all the screenshots captured using the tool.
- `voiceovers/`: This directory will store the generated voiceover files.

## Modules

- `main.py`: The entry point of the application which orchestrates the process.
- `voiceover.py`: Handles the voiceover generation using OpenAI's Text-to-Speech API.
- `snipping.py`: Manages the screen capturing functionality.
- `image.py`: Encodes images and interacts with OpenAI's Vision API for image analysis.

## License

This project is open-sourced under the [Apache 2.0 License](LICENSE).

## Contribution

Contributions to SnippingGPT are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## Support

For support and queries, raise an issue in the [GitHub issue tracker](https://github.com/Jukka-Sun/SnippingGPT/issues).

## Disclaimer

This tool is for educational and research purposes only. Do not use it to capture sensitive information. Always respect privacy and intellectual property rights.
