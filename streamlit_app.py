import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

# Page config
st.set_page_config(
    page_title="VoiceScribe 🎤",
    page_icon="🎤",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #4CAF50;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #aaa;
    margin-bottom: 30px;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #1c1f26;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.result-box {
    background-color: #262730;
    padding: 15px;
    border-radius: 10px;
    color: white;
    font-size: 16px;
}
.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🎤 VoiceScribe</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert your audio into text instantly</div>', unsafe_allow_html=True)

# Card container
st.markdown('<div class="card">', unsafe_allow_html=True)

# Language selection
language = st.selectbox(
    "🌍 Select Language",
    ("en-IN (English - India)", "hi-IN (Hindi - India)")
)

lang_code = "en-IN" if "en-IN" in language else "hi-IN"

# File upload
uploaded_file = st.file_uploader("📂 Upload Audio File", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_audio_path = tmp_file.name

    # Convert to WAV if needed
    if not temp_audio_path.endswith(".wav"):
        sound = AudioSegment.from_file(temp_audio_path)
        wav_path = temp_audio_path + ".wav"
        sound.export(wav_path, format="wav")
    else:
        wav_path = temp_audio_path

    st.audio(wav_path)

    recognizer = sr.Recognizer()

    try:
        with st.spinner("🔍 Transcribing... Please wait"):
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language=lang_code)

        st.success("✅ Transcription Complete")

        # Styled output box
        st.markdown(f'<div class="result-box">{text}</div>', unsafe_allow_html=True)

        # Download button
        st.download_button(
            label="📥 Download as TXT",
            data=text,
            file_name="transcription.txt",
            mime="text/plain"
        )

    except sr.UnknownValueError:
        st.error("❌ Could not understand the audio.")
    except sr.RequestError:
        st.error("⚠️ API unavailable. Check your internet connection.")

    # Cleanup
    os.remove(temp_audio_path)
    if os.path.exists(wav_path):
        os.remove(wav_path)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<div style='text-align: center;'>

<p style="font-size:18px;">Made with ❤️ by <b>DWKR</b></p>

<a href="https://www.linkedin.com/in/diwakar-jha-064130229/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="35" style="margin:10px;">
</a>

<a href="https://github.com/Stfu-diwakar" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="35" style="margin:10px;">
</a>

</div>
""", unsafe_allow_html=True)
