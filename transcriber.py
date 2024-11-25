import os
import argparse
from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr

# Function to split MP3 file into smaller chunks
def split_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_mp3(file_path)
    chunks = make_chunks(audio, chunk_length_ms)
    chunk_files = []
    for i, chunk in enumerate(chunks):
        chunk_name = f"chunk{i}.wav"
        chunk.export(chunk_name, format="wav")
        chunk_files.append(chunk_name)
    return chunk_files

# Function to transcribe audio chunks to text in the specified language
def transcribe_audio(chunk_files, language="en-US"):
    recognizer = sr.Recognizer()

    for i, chunk_file in enumerate(chunk_files):
        with sr.AudioFile(chunk_file) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language=language)
                # Start transcription.txt from scratch
                if i == 0:
                    mode = 'w'  # overwrite file
                # Append to existing file
                else:
                    mode = 'a'  # append to file
                
                with open("transcription.txt", mode) as file:
                    file.write(text + ' ')
                print(f'Transcribed audio chunk {i} to file')

            except sr.UnknownValueError:
                with open("transcription.txt", "a") as file:
                    file.write("[Unintelligible] ")
            except sr.RequestError as e:
                print(f"Could not obtain results; {e}")

# Main logic
if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Audio transcription tool")
    parser.add_argument("mp3_file_path", help="Path to the MP3 file to be transcribed")
    parser.add_argument("--language", default="en-US", help="Language for transcription (default: 'en-US')")
    args = parser.parse_args()

    mp3_file_path = args.mp3_file_path  # Path to the MP3 file
    language = args.language  # Language for transcription

    print("Splitting the audio file...")
    chunks = split_audio(mp3_file_path)
    
    print("Transcribing the audio...")
    transcribe_audio(chunks, language=language)
    
    print("Transcription completed.")
    
    # Cleanup temporary chunk files
    for chunk in chunks:
        os.remove(chunk)
    print("Done.")
