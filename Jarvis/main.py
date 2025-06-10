import os
import speech_recognition as sr
import pyttsx3
import openai
from datetime import datetime

# Initialize OpenAI client
client = openai.OpenAI(api_key="YOUR-API-KEY")  # Replace with your API key

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()
# Remove custom voice selection to use the default system voice
# voices = engine.getProperty('voices')
# for voice in voices:
#     if voice.id == 'com.apple.eloquence.en-GB.Rocko':
#         engine.setProperty('voice', voice.id)
#         break

# Set speaking rate (default is 200)
engine.setProperty('rate', 150)

def speak(text):
    """Convert text to speech"""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input and convert to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("I'm sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        speak("I'm having trouble accessing the speech recognition service.")
        return ""

def get_jarvis_response(user_input):
    """Get response from ChatGPT"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are JARVIS, Tony Stark's AI assistant. You are helpful, witty, and speak in a British accent. Keep responses concise and natural."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I'm experiencing some technical difficulties: {str(e)}"

def control_computer():
    """Simulate controlling the computer (e.g. print a message). In a real implementation, integrate with a library such as pyautogui or a browser automation tool to control your computer or 'look at' tabs."""
    speak('I\'m simulating controlling your computer (or "looking at" tabs). In a real implementation, you\'d integrate a library such as pyautogui or a browser automation tool to do that.')

def main():
    speak("Hello! I am JARVIS, your personal AI assistant. How may I help you today?")
    
    while True:
        user_input = listen()
        
        if not user_input:
            continue
            
        if "goodbye" in user_input or "bye" in user_input or "exit" in user_input:
            speak("Goodbye! Have a wonderful day!")
            if "control" in user_input or "control my computer" in user_input:
                speak("Activating computer control mode.")
                control_computer()
            break
            
        response = get_jarvis_response(user_input)
        speak(response)

if __name__ == "__main__":
    main()
