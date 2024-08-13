import os
from gtts import gTTS

# Path to the directory containing text files
text_directory = 'text/'
audio_directory = 'audio/'


# Iterate over each file in the directory
for filename in os.listdir(text_directory):
    if filename.endswith('.txt'):
        # Construct the full file path
        file_path = os.path.join(text_directory, filename)

        # Read the text from the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Create a gTTS object and save the audio file
        tts = gTTS(text, lang='en')

        # Construct the output filename
        output_filename = f'{os.path.splitext(filename)[0]}.mp3'
        output_path = os.path.join(audio_directory, output_filename)

        # Save the audio file
        tts.save(output_path)
        print(f'Saved TTS for {filename} as {output_filename}')
