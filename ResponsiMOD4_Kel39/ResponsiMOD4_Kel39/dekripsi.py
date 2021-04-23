class method():
    def encrypt(string, shift):
        
    arti = ''
    for char in string: 
     if char == ' ':
          arti = arti + char
        elif  char.isupper():
          arti = arti + chr((ord(char) - shift - 65) % 26 + 65)
        else:
          arti = arti + chr((ord(char) - shift - 97) % 26 + 97)
  
     return arti
