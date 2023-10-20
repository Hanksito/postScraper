from googletrans import Translator


def traducir(texto):
    translator = Translator()
    translation = translator.translate(texto, src='auto', dest='es')
    return translation.text

