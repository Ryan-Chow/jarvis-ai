# JARVIS Voice Assistant

A Python-based voice assistant inspired by JARVIS from Iron Man, using OpenAI's ChatGPT for natural language processing.

## Features

- Voice input and output
- British accent (like JARVIS)
- ChatGPT-powered responses
- Natural conversation flow
- Simple wake word detection

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. For macOS users, you might need to install portaudio:
```bash
brew install portaudio
```

3. Replace the API key in `main.py`:
   - Find the line with `client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")`
   - Replace `YOUR_API_KEY_HERE` with your OpenAI API key

## Usage

1. Run the script:
```bash
python main.py
```

2. Speak to JARVIS when you see "Listening..."
3. Say "goodbye" or "exit" to end the conversation

## Requirements

- Python 3.7+
- Microphone
- Speakers
- Internet connection
- OpenAI API key

## Note

This is a basic implementation of a voice assistant. The voice recognition uses Google's speech recognition service, and the responses are powered by OpenAI's GPT-3.5-turbo model.
