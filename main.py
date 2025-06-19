from tkinter import *
from deep_translator import GoogleTranslator
import pyttsx3
import speech_recognition as sr

# Supported languages
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Spanish (Mexico)": "es",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

# Text-to-Speech
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Translate function
def translate_text():
    input_text = input_box.get("1.0", END).strip()
    target_lang = lang_choice.get()

    if not input_text or target_lang not in language_codes:
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, "Please enter valid text and select a language.")
        output_box.config(state=DISABLED)
        return

    try:
        code = language_codes[target_lang]
        translated = GoogleTranslator(source='auto', target=code).translate(input_text)
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, translated)
        output_box.config(state=DISABLED)
    except Exception as e:
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, f"Error: {str(e)}")
        output_box.config(state=DISABLED)

# Voice Input
def use_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        input_box.delete("1.0", END)
        input_box.insert(END, "Listening... Please speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
            input_text = recognizer.recognize_google(audio)
            input_box.delete("1.0", END)
            input_box.insert(END, input_text)
        except sr.UnknownValueError:
            input_box.delete("1.0", END)
            input_box.insert(END, "Sorry, couldn't understand audio.")
        except sr.RequestError:
            input_box.delete("1.0", END)
            input_box.insert(END, "Speech Recognition service error.")
        except sr.WaitTimeoutError:
            input_box.delete("1.0", END)
            input_box.insert(END, "No speech detected. Try again.")

# Speak Translated Text
def speak_translation():
    translated_text = output_box.get("1.0", END).strip()
    if translated_text:
        speak_text(translated_text)

# GUI setup
root = Tk()
root.title("Smart Language Translator")
root.geometry("600x500")
root.resizable(False, False)

Label(root, text="Enter Text or Use Microphone:", font=("Arial", 12)).pack(pady=5)
input_box = Text(root, height=4, width=70, font=("Arial", 10))
input_box.pack()

mic_button = Button(root, text="🎤 Speak", command=use_microphone, bg="#FFC107", fg="black", font=("Arial", 10, "bold"))
mic_button.pack(pady=5)

Label(root, text="Select Target Language:", font=("Arial", 12)).pack()
lang_choice = StringVar(root)
lang_choice.set("Hindi")
OptionMenu(root, lang_choice, *language_codes.keys()).pack()

Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

Label(root, text="Translated Text:", font=("Arial", 12)).pack()
output_box = Text(root, height=5, width=70, font=("Arial", 10))
output_box.pack()
output_box.config(state=DISABLED)

Button(root, text="🔊 Speak Translation", command=speak_translation, bg="#2196F3", fg="white", font=("Arial", 10)).pack(pady=10)

root.mainloop()
