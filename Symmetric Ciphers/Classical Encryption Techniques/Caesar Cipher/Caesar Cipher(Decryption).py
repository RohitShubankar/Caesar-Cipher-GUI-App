'''
    Caesar DeCipher: The Caesar DeCipher involves replacing the each letter in
    the given plain text with the letter standing three places further up
    the Alphabet.

    Example : Cipher Text - KhoorZruog
              Plain Text -  HelloWorld
    Encryption Algorithm : P = D(K,C) = (C-K)mod26
    where C: Cipher text
          K: Key = 3
          P: Plain text
'''
def CaesarCipher_Decryption(cipher_text,key):
    plain_text = ""
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
            plain_text+=chr((ord(letter)-key-97)%26+97)
    return plain_text
cipher_text = input("Enter the Cipher Text without any space:")
key = 3
print("The Cipher Text is:",cipher_text)
print("The Plain Text is:",CaesarCipher_Decryption(cipher_text,key))
