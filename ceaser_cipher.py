def encrypt_func(p_txt, s):  
    result = ""  
  
  
    for i in range(len(p_txt)):  
        char = p_txt[i]  
  
        if (char.isalpha()):
        
            if (char.isupper()):  
                result += chr((ord(char) + s - 65) % 26 + 65) 

            else:  
                result += chr((ord(char) + s - 97) % 26 + 97)  
        else:
            result += char

    return result  


def decrypt_func(d_txt, s):  
    result = ""  
  
  
    for i in range(len(d_txt)):  
        char = d_txt[i]  
  
        if (char.isalpha()):
        
            if (char.isupper()):  
                result += chr((ord(char) - s - 65) % 26 + 65) 

            else:  
                result += chr((ord(char) - s - 97) % 26 + 97)  
        else:
            result += char

    return result  

p_txt = "oderw"
d_txt = "oderw"  
s = 4
  
print("Plain txt : " + p_txt)  
print("Shift pattern : " + str(s))  
print("Cipher: " + encrypt_func(p_txt, s))  
print("DeCipher: " + decrypt_func(d_txt, s)) 