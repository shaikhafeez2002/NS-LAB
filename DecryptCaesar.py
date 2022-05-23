def encypt_func(txt, s):  
    result=""  

  
# transverse the plain txt

    for i in range(len(txt)):  
        char = txt[i]
        
        # decrypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) - s - 65) % 26 + 65)
            
        # decypt_func lowercase characters in plain txt
        
        else:  
            result += chr((ord(char) - s - 97) % 26 +97)
            
    return result

# check the above function

txt = input() 
s = int(input())  
  
print("Plain txt : ",txt)  
print("Shift pattern : ",str(s))  
print("Cipher: ",encypt_func(txt, s)) 
