# -*- coding:utf-8 -*-
# pip install googletrans==3.1.0a0

from googletrans import Translator

translator = Translator()

text = input('Write something in english...\n>>> ')

lang = input('Select language Russian - ru\nUzbek - uz\n>>>')

translated = translator.translate(text, dest=lang, src='en')

print(translated.text)