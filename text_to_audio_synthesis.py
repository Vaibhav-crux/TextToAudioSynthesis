import os
from google.cloud import storage
import boto3
from io import BytesIO
from datetime import datetime, timedelta
import nltk

# Set the relative path to your JSON key file
json_key_path = 'Your/Relative/Path/to/FileName.json'

# Set your AWS access key and secret key as environment variables
os.environ['AWS_ACCESS_KEY_ID'] = 'Your AWS KEY'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'Your AWS Secret Key'

# Set the AWS region (e.g., us-east-1)
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

# Set your Google Cloud Storage credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_key_path

def text_to_audio_aws(text, voice_id='Matthew', output_format='mp3', rate='soft', volume='medium'):
    polly_client = boto3.client('polly')

    ssml_text = f'<speak><prosody rate="{rate}" volume="{volume}">{text}</prosody></speak>'

    response = polly_client.synthesize_speech(
        TextType='ssml',
        Text=ssml_text,
        OutputFormat=output_format,
        VoiceId=voice_id,
        Engine='neural',
    )

    audio_data = response['AudioStream'].read()
    return audio_data

def split_and_synthesize_text(text, max_chunk_length=2955):
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

    audio_files = []

    for i, chunk in enumerate(chunks):
        audio_data = text_to_audio_aws(chunk, rate='medium', volume='medium')
        file_name = f'chunk_{i}.mp3'

        with open(file_name, 'wb') as audio_file:
            audio_file.write(audio_data)

        audio_files.append(file_name)

    return audio_files

text = """Your Text Here"""

audio_files = split_and_synthesize_text(text)

# Initialize the Google Cloud Storage client
storage_client = storage.Client()

bucket_name = 'mindverse'
folder_path = 'Audios/'

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
output_blob_name = f'output_{timestamp}.mp3'

blob_name = folder_path + output_blob_name

# Combine audio files into a single audio file
combined_audio_data = b''
for audio_file in audio_files:
    with open(audio_file, 'rb') as file:
        combined_audio_data += file.read()
    os.remove(audio_file)

# Upload the combined audio to Google Cloud Storage
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_string(combined_audio_data, content_type='application/octet-stream')

url = blob.public_url

print(f'File uploaded to folder {folder_path} in bucket {bucket_name} with blob name: {blob_name}')
print(f'Public URL of the file: {url}')
