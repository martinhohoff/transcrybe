# Transcrybe - Audio Transcription Tool

Transcrybe is a script to transcribe audio from MP3 files into text using 
Google Speech Recognition. It splits the audio into smaller chunks for 
processing and saves the transcription to a text file.

## Features
- Split MP3 files into smaller chunks.
- Transcribe audio to text using Google Speech Recognition.
- Support for multiple languages.
- Automatic cleanup of temporary files.

## Requirements
- Python 3.7 or higher
- Required libraries: `pip-tools`, `pyaudio`, `pydub`, `speechrecognition`, `portaudio`, 

## Installation

1. Ensure you have portaudio installed for audio processing:
    - For Windows: Download portaudio and add it to your system's PATH.
    - For macOS: Install using Homebrew:
    ```bash
    brew install portaudio
    ```
    - For Linux: Install via package manager:
    ```bash
    sudo apt-get install portaudio
    ```
2. Ensure you have FFmpeg installed for audio processing:
    - For Windows: Download FFmpeg and add it to your system's PATH.
    - For macOS: Install using Homebrew:
    ```bash
    brew install ffmpeg
    ```
    - For Linux: Install via package manager:
    ```bash
    sudo apt-get install ffmpeg
    ```
3. Clone the repository or download the script.
4. Install pip-tools for package handling:
   ```bash
   pip install pip-tools
   ```
5. Install the required libraries using pip-tools:
   ```bash
   pip-compile && pip-sync
   ```


# Usage
Run the script from the command line:

```bash
python transcriber.py <mp3_file_path> [--language <language_code>]
```

## Arguments
- <mp3_file_path>: Path to the MP3 file to be transcribed.
- --language: Language code for transcription (default: en-US).

## Example

```bash
python script.py my_audio.mp3 --language en-US
```

# Output
- The transcribed text will be saved in `transcription.txt` in the current directory.

# Cleanup
Temporary audio chunks created during processing are automatically deleted after transcription.

# Notes
- The quality of transcription depends on the clarity of the audio and the accuracy of Google Speech Recognition.
- Some portions of audio may result in `[Unintelligible]` if the speech is not clear.

# License
This project is licensed under the MIT License.





