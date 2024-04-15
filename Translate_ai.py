import openai
from google.cloud import translate_v2 as translate

def openai_translate(text, target_language):
    openai.api_key = 'Api Key'  # Replace with your OpenAI API key
    response = openai.Completion.create(
        engine="davinci",
        prompt="Translate the following English text into " + target_language + ":\n\"" + text + "\"",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def google_translate(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def main():
    text = input("Enter text to translate: ")
    target_language = input("Enter target language code (e.g., 'fr' for French): ")
    
    # Translate using OpenAI
    intermediate_translation = openai_translate(text, target_language)
    
    # Translate the intermediate translation to the final target language using Google Translate
    final_translation = google_translate(intermediate_translation, target_language)
    
    print("Translated text:", final_translation)

if __name__ == "__main__":
    main()