from gtts import gTTS


def chat_vosi(text, save):
    vois = gTTS(text)
    vois.save(save)
