"""
This module defines data analyzers.
"""
import string

from nltk.corpus import stopwords

def noise_reduction(message):
    """
    This function defines a noise reducing
    analyzer.

    Args:
        message (str): The message to be analyzed.
    """
    no_punc_msg = _remove_puncutuations(message)
    return _remove_stopwords(no_punc_msg)

def _remove_puncutuations(message):
    message_without_punctuation = [
        char for char in message
            if char not in string.punctuation
    ]

    return ''.join(message_without_punctuation)

def _remove_stopwords(message):
    clear_text = [
        word for word in message.split()
            if word.lower() not in stopwords.words('english')
    ]

    return clear_text
