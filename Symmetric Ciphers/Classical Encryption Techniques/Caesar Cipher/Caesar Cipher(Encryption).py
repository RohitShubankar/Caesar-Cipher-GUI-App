''' Caesar Cipher: One of the earliest and the simplest encryption technique.
    The Caesar Cipher involves replacing the each letter in the given plain text
    with the letter standing three places further down the Alphabet.

    Example : Plain Text -  Hello World.
              Cipher Text - Khoor zruog
    Encryption Algorithm : C = E(K,P) = (P+K)mod26
    where C: Cipher text
          K: Key = 3
          P: Plain text
'''
def CaesarCipher_Encryption(plain_text,key):
    cipher_text = ""
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
            cipher_text+=chr((ord(letter)+key-97)%26+97)
    return cipher_text
plain_text = input("Enter the Plain Text:")
key = 3
print("The Plain Text is:",plain_text)
print("The Cipher Text is:",CaesarCipher_Encryption(plain_text,key))
