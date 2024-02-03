alphabet = 'abcdefghijklmnopqrstuvwxyz'
key =      'jsuyfhkpicomxrqatlbvznewgd'


def substitute(text, substitute_what, substitute_by):
    result = ''
    for symbol in text.lower():
        if symbol in substitute_what:
            result += substitute_by[substitute_what.index(symbol)]
        else:
            result += symbol

    return result


def encode(plaintext):
    return substitute(plaintext, alphabet, key)


def decode(ciphertext):
    return substitute(ciphertext, key, alphabet)


message = 'the quick brown fox jumps over the lazy dog'
code = encode(message)
print(code)
print(decode(code))