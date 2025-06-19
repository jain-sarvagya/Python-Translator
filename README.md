# 🌐 Smart Language Translator (GUI App)

A simple and powerful desktop language translator built with **Python**, using **Tkinter** for GUI, **deep-translator** for translation, and support for **voice input (speech recognition)** and **text-to-speech output**.

---

## ✨ Features

- ✅ Translate text to 15+ supported languages
- 🎤 Voice input via microphone
- 🔊 Text-to-speech for translated output
- 🖥️ User-friendly graphical interface (Tkinter)
- 🌍 Auto-detects source language
- 🔒 Offline-capable for speech synthesis

---

## 🚀 Tech Stack

- Python 3.x
- [deep-translator](https://pypi.org/project/deep-translator/)
- tkinter (built-in)
- pyttsx3 (text-to-speech)
- SpeechRecognition (voice input)
- pyaudio (microphone support)

---

## 📦 Installation

### 1. Clone the repository (if using GitHub):

```bash
git clone https://github.com/your-username/language-translator-app.git
cd language-translator-app
2. Install dependencies
bash
Copy
Edit
pip install deep-translator pyttsx3 SpeechRecognition pyaudio
⚠️ On Windows, if pyaudio gives error, try:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
▶️ Usage
Run the app using:

bash
Copy
Edit
python translator_gui.py
Then:
Type or speak the sentence

Choose your target language (like Hindi, French, Spanish etc.)

Click Translate

Click Speak Translation to hear the output

🌐 Supported Languages
English, Hindi, French, German, Gujarati, Marathi, Bengali, Punjabi, Spanish, Tamil, Telugu, Urdu, Chinese, Japanese, Korean, Arabic

You can add more by modifying the language_codes dictionary in the script.

🧠 Future Features (Optional Ideas)
Save translated text to file

Copy to clipboard button

Source language dropdown

Dark mode support

🛡️ License
This project is free to use for learning and educational purposes.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

🙋‍♂️ Author
Sarvagya Jain
GitHub Profile