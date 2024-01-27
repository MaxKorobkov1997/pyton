from googletrans import Translator

translator = Translator()


def translate_text(text, yas):
    translated_text = translator.translate(text, dest=yas)
    return translated_text.text


def yax(text):
    a = translator.detect(text)
    return a.lang
