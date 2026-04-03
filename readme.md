# Transcrybe

Transcrybe is a small command-line tool that transcribes MP3 audio files into
text using Google Speech Recognition. It splits long audio into smaller chunks,
processes each chunk, and writes the result to `transcription.txt`.

## Features

- Transcribes MP3 files to text.
- Splits long audio into smaller chunks automatically.
- Supports a configurable language code.
- Cleans up temporary chunk files after processing.

## Requirements

- Python 3.7 or higher
- FFmpeg
- Python packages listed in [`requirements.txt`](requirements.txt)

## Installation

1. Install FFmpeg.

For macOS:

```bash
brew install ffmpeg
```

For Ubuntu or Debian:

```bash
sudo apt-get install ffmpeg
```

For Windows:

Install FFmpeg and make sure it is available on your `PATH`.

2. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line:

```bash
python transcriber.py <mp3_file_path> [--language <language_code>]
```

### Arguments

- `<mp3_file_path>`: Path to the MP3 file to be transcribed.
- `--language`: Language code for transcription. Defaults to `en-US`.

### Example

```bash
python transcriber.py my_audio.mp3 --language en-US
```

## Output

The transcribed text is saved to `transcription.txt` in the current directory.

## Notes

- Transcription quality depends on the clarity of the audio.
- If a chunk cannot be understood, the script writes `[Unintelligible]`.
- The script uses Google Speech Recognition through the `SpeechRecognition`
  Python package.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for
details.




