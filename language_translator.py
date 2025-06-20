from deep_translator import GoogleTranslator

# Input from user
text = input("Enter text to translate: ")
lang = input("Translate to which language? (e.g. Hindi, English, French): ").strip().lower()

# Set language code based on input
if lang == "english":
    code = "en"
elif lang == "hindi":
    code = "hi"
elif lang == "french":
    code = "fr"
elif lang == "german":
    code = "de"
elif lang == "gujarati":
    code = "gu"
elif lang == "marathi":
    code = "mr"
elif lang == "bengali":
    code = "bn"
elif lang == "punjabi":
    code = "pa"
elif lang == "tamil":
    code = "ta"
elif lang == "telugu":
    code = "te"
elif lang == "urdu":
    code = "ur"
elif lang == "chinese":
    code = "zh-CN"
elif lang == "japanese":
    code = "ja"
elif lang == "korean":
    code = "ko"
elif lang == "arabic":
    code = "ar"
elif lang == "mexico" or lang == "spanish":
    code = "es"
else:
    print("Sorry, language not supported.")
    exit()

# Translate using deep-translator
translated = GoogleTranslator(source='auto', target=code).translate(text)

# Output
print("Translated text:", translated)
