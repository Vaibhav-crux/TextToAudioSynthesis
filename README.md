# Text-to-Audio Synthesis

This Python script demonstrates text-to-audio synthesis using AWS Polly and Google Cloud Storage. The script splits the input text, converts it into audio chunks, and uploads the synthesized audio to a Google Cloud Storage bucket.

## Getting Started

### Prerequisites

Before running the script, make sure you have the following:

- [AWS Access Key and Secret Key](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
- [Google Cloud Storage JSON Key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
- Python environment with required packages (install using `pip install -r requirements.txt`)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Set up your environment variables:

    - `AWS_ACCESS_KEY_ID`: Your AWS Access Key
    - `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Key
    - `AWS_DEFAULT_REGION`: AWS region (e.g., `us-east-1`)
    - `GOOGLE_APPLICATION_CREDENTIALS`: Relative path to your Google Cloud Storage JSON key file (`Your/Relative/Path/to/FileName.json`)

3. Replace the placeholder text with your own input:

    - Update the `text` variable with your desired input text.
    - Modify the `json_key_path` variable with the relative path to your Google Cloud Storage JSON key file.

## Usage

Run the script:

```bash
python text_to_audio_synthesis.py
