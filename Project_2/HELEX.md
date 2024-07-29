# AI virtual assistant

To get started with the project, you have to have an account in OpenAi api, visit the website and create an account for yourself
```https://openai.com/index/openai-api/ ```

Create the account and then *add some money to your account* to your account to access the api models, to view the prices of the models, visit this link
```https://openai.com/api/pricing/```

After seeing th prices and adding some money to your account you have to integrate the model into your project, you can do all that with the below code!

``` python
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
        engine="gpt-3.5", # Replace with your model, or you can use this! 
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
```

## Troubleshooting

##### Note that the default model i am using in the code is GPT-3.5, you can also use lower model for lesser cost, just replace the name of your model with the GPT-3.5 to access the API.

When implementing this code, several types of errors can occur. Below are some common issues you might encounter, along with potential solutions:

### 1. **API Key Error**
   **Error:** The OpenAI API key is missing or invalid.
   **Solution:** Ensure that you have a valid API key from OpenAI and that it is correctly set in the code.
   ```python
   openai.api_key = 'YOUR_OPENAI_API_KEY'  # Ensure the API key is valid and correctly entered
   ```

### 2. **Microphone Access Error**
   **Error:** The microphone is not accessible or not working properly.
   **Solution:** Check that the microphone is properly connected and that your system allows microphone access.
   ```python
   microphone = sr.Microphone()  # Ensure the microphone is connected and accessible
   ```

### 3. **Speech Recognition Request Error**
   **Error:** The request to the speech recognition API fails.
   **Solution:** Handle the `sr.RequestError` exception by checking your internet connection and the availability of the Google Speech Recognition API.
   ```python
   except sr.RequestError:
       response["success"] = False
       response["error"] = "API unavailable"  # Check internet connection and API availability
   ```

### 4. **Unknown Value Error**
   **Error:** The speech is not recognized properly.
   **Solution:** Handle the `sr.UnknownValueError` exception by ensuring clear speech and proper microphone setup.
   ```python
   except sr.UnknownValueError:
       response["error"] = "Unable to recognize speech"  # Ensure clear speech and proper microphone setup
   ```

### 5. **OpenAI API Rate Limit Error**
   **Error:** Exceeding the rate limit of OpenAI API requests.
   **Solution:** Implement rate limiting and exponential backoff strategies to handle this gracefully.
   ```python
   response = openai.Completion.create(
       engine="gpt-3.5",
       prompt=prompt,
       max_tokens=150
   )  # Ensure compliance with OpenAI rate limits
   ```

### 6. **JSON Decode Error**
   **Error:** Invalid response format from OpenAI API.
   **Solution:** Ensure the response from OpenAI API is in the correct format and handle any potential parsing issues.
   ```python
   response = openai.Completion.create(
       engine="gpt-3.5",
       prompt=prompt,
       max_tokens=150
   )
   return response.choices[0].text.strip()  # Handle potential JSON decoding errors
   ```

### 7. **KeyError: 'transcription'**
   **Error:** The key `'transcription'` is missing in the response dictionary.
   **Solution:** Ensure the key exists before accessing it.
   ```python
   if "transcription" in voice_input:
       print(f"You said: {voice_input['transcription']}")
   else:
       print("No transcription found.")
   ```

### 8. **Microphone Recognition Timeout**
   **Error:** The recognizer might timeout if it takes too long to pick up audio.
   **Solution:** Increase the timeout period or handle the exception gracefully.
   ```python
   recognizer.listen(source, timeout=10)  # Adjust the timeout period as needed
   ```

### 9. **Handling Keyboard Interrupt**
   **Error:** User might want to exit the loop using a keyboard interrupt.
   **Solution:** Catch the `KeyboardInterrupt` exception to allow graceful exit.
   ```python
   try:
       while True:
           ...
   except KeyboardInterrupt:
       print("Exiting...")
       break
   ```

### Complete Code with Error Handling:
Here is the revised code with added error handling:


These adjustments should help handle common errors gracefully when implementing this code.
