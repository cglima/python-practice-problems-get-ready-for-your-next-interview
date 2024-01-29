""" Caesar Cipher
    A caesar cipher is a simple substitution cipher where each letter of the
    plain text is substituted with a letter found by moving 'n' places down the
    alphabet. For an example, if the input plain text is:

        abcd xyz

    and the shift value, n, is 4. The encrypted text would be:

        efgh bcd

    You are to write a function which accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters being transformed while all
    punctuation and whitespace remains unchanged.

    Note: You can assume the plain text is all lowercase ascii, except for
    whitespace and punctuation.
"""

def caesar(plain_text, n):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            cipher_text += chr((ord(char) - start + n) % 26 + start)
        else:
            cipher_text += char
    return cipher_text


def test_cifra_cesar_com_deslocamento_zero():
    assert caesar("abc", 0) == "abc"
    assert caesar("xyz", 0) == "xyz"
    assert caesar("Hello, World!", 0) == "Hello, World!"


def test_cifra_cesar_com_deslocamento_positivo():
    assert caesar("abc", 3) == "def"
    assert caesar("xyz", 3) == "abc"
    assert caesar("Hello, World!", 5) == "Mjqqt, Btwqi!"


def test_cifra_cesar_com_deslocamento_negativo():
    assert caesar("abc", -3) == "xyz"
    assert caesar("xyz", -3) == "uvw"
    assert caesar("Hello, World!", -5) == "Czggj, Rjmgy!"


def test_cifra_cesar_com_texto_nao_alfabetico():
    assert caesar("123", 3) == "123"
    assert caesar("@#$%", 5) == "@#$%"
    assert caesar(" ", 2) == " "
