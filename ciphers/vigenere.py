def vigenere_cipher(text, key, encrypt=True):
    text = text.upper()
    key = key.upper()
    result = []
    
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if encrypt:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % key_length
        else:
            result.append(char)

    return ''.join(result)
