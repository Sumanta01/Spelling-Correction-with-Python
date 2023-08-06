# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 04:03:37 2023

@author: KIIT
"""

from spellchecker import SpellChecker

def correct_spelling(text):
    spell = SpellChecker()
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    return ' '.join(corrected_words)

if __name__ == "__main__":
    input_text = input("Enter text with spelling errors: ")
    corrected_text = correct_spelling(input_text)
    print("Corrected text:")
    print(corrected_text)
