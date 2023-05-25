# Fine-tuning a Text-to-Speech Model with Emotion Labels

This repository provides a guide on how to fine-tune a text-to-speech (TTS) model using a dataset that includes emotion labels for the speech. Fine-tuning a TTS model with emotion labels can enable the generation of emotionally expressive speech.

## Dataset

The [IEMOCAP dataset](https://www.kaggle.com/datasets/mouadriali/iemocap-transcriptions-english-french) is used for fine-tuning, consists of speech samples paired with corresponding emotion labels. Each sample in the dataset includes a text prompt and the corresponding audio waveform, along with an emotion label indicating the intended emotional expression of the speech.

## Model

The base TTS model used for fine-tuning is [microsoft/speecht5_tts](https://huggingface.co/microsoft/speecht5_tts), a state-of-the-art text-to-speech model.

## Webapp
[Try generating speech](https://blessontomjoseph-tts-with-emotion-app-jys0bs.streamlit.app/)

## Links
The [text_to_speech notebook](text-to-speech.ipynb) was trained on kaggle, for reproducing the results or for running, fork my notebook 👉 [notebook](https://www.kaggle.com/code/blessontomjoseph/text-to-speech/edit)

Find the fine tuned model on huggingface hub 👉 [model](https://huggingface.co/theothertom/emo_t5_speech_chkpt/tree/main)
