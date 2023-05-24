from transformers import AutoProcessor, SpeechT5ForTextToSpeech
import torch
from transformers import SpeechT5HifiGan
from IPython.display import Audio
import streamlit as st
import time

def gen(prompt,emo,model,speaker_embeddings):
    text=prompt+" [emotion] "+emo
    inputs = processor(text=text, return_tensors="pt")
    spectrogram = model.generate_speech(inputs["input_ids"].to('cpu'), speaker_embeddings.to('cpu'))
    with torch.no_grad():
            speech=vocoder(spectrogram)
    return Audio(speech.cpu().numpy(),rate=16000,autoplay=True)


if __name__ == '__main__':
    text = st.text_input("Enter your text")
    emo = st.sidebar.radio("Select an emo!", ('Frustration','Excitement','Neutral','Anger','Sadness','Happiness','Surprise','Fear','Other','Disgust'))
    apply = st.button('generate speech')
    if apply:
        with st.spinner("getting model from 🤗..."):
            processor = AutoProcessor.from_pretrained("theothertom/emo_t5_speech_chkpt")
            model = SpeechT5ForTextToSpeech.from_pretrained("theothertom/emo_t5_speech_chkpt")
            vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan") 
        st.success('model ready!')

        with st.spinner("generating speech..."):
            start_time = time.time()
            speech=gen(text,emo,model.to('cpu'),torch.load('speaker_embeddings.pt'))
            response_time = time.time() - start_time

        st.success(f"""Success!~Elapsed Time: {response_time:.2f} seconds""")
        st.write(speech)
