def decode_word(encrypted_word, cipher):
    result = ""
    for ch in encrypted_word:
        for key in cipher:
            if ch == cipher[key]:
                result += key
    return result

