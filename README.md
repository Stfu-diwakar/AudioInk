# 🎤 AudioInk™

**AudioInk™** is a sleek and simple web app that converts your audio files into text instantly using speech recognition. Built with **Streamlit**, it supports multiple languages and provides an easy-to-use interface for quick transcription.

🌐 **Live App:** https://audioink-dwkr.streamlit.app/

---

## 🚀 Features

* 🎧 Upload audio files (`.wav`, `.mp3`, `.ogg`)
* 🌍 Multi-language support:

  * English (India)
  * Hindi (India)
* ⚡ Fast transcription using Google Speech Recognition
* 📄 Download transcription as a `.txt` file
* 🎨 Clean and modern UI with custom styling

---

## 🛠️ Tech Stack

* **Frontend & App Framework:** Streamlit
* **Speech Recognition:** SpeechRecognition (Google API)
* **Audio Processing:** Pydub
* **Language:** Python

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Stfu-diwakar/audioink.git
   cd audioink
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg (required for Pydub):

   * Windows: Download from https://ffmpeg.org/download.html
   * Linux:

     ```bash
     sudo apt install ffmpeg
     ```
   * Mac:

     ```bash
     brew install ffmpeg
     ```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📂 How It Works

1. Upload your audio file
2. Select your preferred language
3. Click to process
4. View the transcription
5. Download the result as a text file

---

## ⚠️ Limitations

* Requires an active internet connection (Google API)
* Accuracy depends on audio clarity and background noise
* Large files may take longer to process

---

## 📸 Preview

Try it live 👉 https://audioink-dwkr.streamlit.app/

---

## 👨‍💻 Author

**Diwakar Jha (DWKR)**

* 🔗 LinkedIn: https://www.linkedin.com/in/diwakar-jha-064130229/
* 💻 GitHub: https://github.com/Stfu-diwakar

---

## ❤️ Support

If you like this project, consider giving it a ⭐ on GitHub!
