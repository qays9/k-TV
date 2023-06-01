def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(text)):
        char = text[i]
        key_char = key[i % key_length]
        
         
        ascii_code = ord(char)
        
         
        encrypted_ascii_code = ascii_code + ord(key_char)
        
         
        encrypted_char = chr(encrypted_ascii_code)
        
        
        encrypted_text += encrypted_char
    
    return encrypted_text

 
key = "XOX"
#text = ""
encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)
