import speech_recognition as sr
import openai
import time

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Function to recognize speech
def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    response = {"success": True, "error": None, "transcription": None}

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response

# Function to get response from OpenAI
def get_openai_response(prompt):
    openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key
    response = openai.Completion.create(
        engine="gpt-3.5",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main loop
print("HELEX is ready! Speak to interact.")
while True:
    voice_input = recognize_speech_from_mic(recognizer, microphone)
    if voice_input["transcription"]:
        print(f"You said: {voice_input['transcription']}")
        response = get_openai_response(voice_input["transcription"])
        print(f"HELEX: {response}")
    elif voice_input["error"]:
        print(f"Error: {voice_input['error']}")
    time.sleep(0.1)
