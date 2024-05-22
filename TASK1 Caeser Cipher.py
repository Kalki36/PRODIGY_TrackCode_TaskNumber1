import string
def csar_cpher(msg,sft):
    result=""
    for char in msg:
        if char in string.ascii_lowercase:
            result+=chr((ord(char)-ord('a')+sft)%26+ord('a'))
        elif char in string.ascii_uppercase:
            result+=chr((ord(char)-ord('A')+sft)%26+ord('A'))
        else:
            result+=char
    return result

msg = input("Enter the message to encrypt: ")
sft = int(input("Enter the shift value: "))

enc_msg = csar_cpher(msg, sft)
print("Encrypted message:", enc_msg)

dec_msg = csar_cpher(enc_msg, -sft)
print("Decrypted message:", dec_msg)