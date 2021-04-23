alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
kunci = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM '

def encrypt():
    for i in kalimat:
        count=0
        for j in alfabet:
            if i == j:
                print(kunci[count], end = "")
            count+=1
class user:
    def decrypt(self):
        for i in kalimat:
            count=0
            for j in kunci:
                if i == j:
                    print(alfabet[count], end ="")
                count+=1

pil=int(input("Pilih layanan\n1. Enkripsi\n2. Dekripsi\n"))
if pil == 1 :
    kalimat = input('Masukkan teks: ')
    encrypt()
elif pil == 2 :
    kalimat = input('Masukkan teks: ')
    name = user()
    name.decrypt()
