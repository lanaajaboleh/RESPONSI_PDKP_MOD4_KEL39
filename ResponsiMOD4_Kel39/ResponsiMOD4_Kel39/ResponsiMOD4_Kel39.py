def encrypt(string, geser):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      arti = arti + char
    elif  char.isupper():
      arti = arti + chr((ord(char) + geser - 65) % 26 + 65)
    else:
      arti = arti + chr((ord(char) + geser - 97) % 26 + 97)
  
  return arti
 
layanan=input("Pilih layanan:\n1. Enkripsi\n2. Dekripsi")


if (layanan = 1)
text = input("\nMasukkan teks: ")
s = int(input("Masukkan pergeseran sesuai kelompok: "))
print("sebelum enkripsi: ", text)
print("setelah dekripsi: ", encrypt(text, s))





   

