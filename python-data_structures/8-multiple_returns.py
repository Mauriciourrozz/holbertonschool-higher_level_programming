#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    if not sentence[0]:
        return None
    length = len(sentence)
    first = sentence[0]
    return length, first
