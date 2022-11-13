# VIGENERE CIPHER
def generateKey(string, key): #inisialisasi kunci
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encrypt_vigenere(string, key): #proses enkripsi vigenere
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) + ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 

def decrypt_vigenere(encrypt_text, key): #proses dekripsi vigenere
  plain_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
    x += ord('A') 
    plain_text.append(chr(x)) 
  return("" . join(plain_text)) 


# CAESAR CIPHER
def encrypt_caesar(text,shift): #proses enkripsi caesar cipher
    encryption = ("")
    for x in text:
        if x.isupper(): 
            char_unicode = ord(x)
            char_index = char_unicode - ord("A")
            index_baru = (char_index + shift) % 26
            unicode_baru = index_baru + ord("A")
            karakter_baru = chr(unicode_baru)
            encryption = encryption + karakter_baru
        else:
            encryption += x
        
    print("Plain text : ",text)
    print("Ciphertext dari enkripsi vigenere + caesar : ",encryption)

def decrypt_caesar(text,shift): #proses dekripsi caesar cipher
    decryption = ("")
    for x in text:
        if x.isupper():  
            char_unicode = ord(x)
            char_index = char_unicode - ord("A")
            index_baru = (char_index - shift) % 26
            unicode_baru = index_baru + ord("A")
            karakter_baru = chr(unicode_baru)
            decryption = decryption + karakter_baru
        else:
            decryption += x

    print("Enkripsi vigenere + caesar yang akan di dekripsi : ",text)
    print("Hasil dekripsi dari caesar  : ",decryption)


# MAIN
def main():
  menu = "y" or "Y" #untuk perulangan program
  while menu == "y" or "Y":
    print("========================================================")
    print("|     UTS PRAK SKD - SEVYRA NANDA - V3921034 - TIE     |")
    print("|           PROGRAM CAESAR & VIGENERE CIPHER           |")
    print("========================================================")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Exit")
    menu = int(input("Silahkan pilih menu : "))

    if menu == 1: #enkripsi
      print("-------------------- Vigenere Cipher --------------------") #enkripsi tahap 1 menggunakan vigenere cipher
      string = input("Masukkan Plain text : ")
      keyword = input("Masukkan keyword : ")
      key = generateKey(string, keyword) 
      encrypt_text = encrypt_vigenere(string,key)
      print("Hasil enkripsi Vigenere : ",encrypt_text)
      print("-------------------- Caesar Cipher --------------------") #enkripsi tahap 2 menggunakan caesar cipher
      text = input("Masukkan enkripsi vigenere : ").upper()
      shift = int(input("Masukkan kunci geser : "))
      encrypt_caesar(text,shift)
    elif menu == 2: #dekripsi
      print("-------------------- Caesar Cipher --------------------") #dekripsi tahap 1 dimulai dari caesar cipher, karena proses enkripsi terakhir menggunakan metode caesar
      text = input("Masukkan hasil enkripsi vigenere + caesar : ").upper()
      shift = int(input("Masukkan kunci geser seperti pada enkripsi : "))
      decrypt_caesar(text,shift)
      print("-------------------- Vigenere Cipher --------------------") #dekripsi tahap 2 dengan vigenere cipher
      string = input("Masukkan hasil dekripsi dari caesar : ")
      keyword = input("Masukkan keyword seperti pada enkripsi : ")
      key = generateKey(string, keyword) 
      decrypt_text = decrypt_vigenere(string, key)
      print("Plain Text/Hasil Dekripsi dari vigenere + caesar : ", decrypt_text)
    elif menu == 3: #keluar program
      exit()
  
if __name__ == "__main__":
    main()