#developed by Mr N4T1ON
#version 1.00

import random
import time

print("* Selamat datang di calculator cinta*")
print("memulai....")

#creating loop until user exits
while True:
  time.sleep(1)
  name1 = input("masukan nama cowo:-")
  name2 = input("masukan nama cewe:-\n")
  
#knowing wheather user entered same name or not
  if name1 == name2:
    print("Itu bukan nama seseorang kan_- beri yang bener")
    continue 
  
  elif name1 != name2:
    print(" persentase cinta adalah ")
    percentage = random.randint(0,100)
    time.sleep(1)
    print(percentage,"%\n")

 #adding a quote  
    quote = ['  hari-Hidup tanpa cinta itu seperti\na pohon tanpa bunga atau buah\n','kutipan hari ini-Hal terbaik untuk dipegang dalam hidup\nis satu sama lain ❤️\n','kutipan hari ini-Dalam hidupmu\nmy mimpi tak terbatas hidup😍\n','quote-Cinta sejati adalah 20% perhatian dan 80% pengertian💚\n','kutipan-Persentase hanya dari 1 hingga 100 tetapi\n cintaku tidak terbatas💖\n']
    print(random.choice(quote))
    
    q = input(r"keluar?,(Y\N)")
    quit = q.upper()
    
#asking wheather user wants to exit or not
    if quit == 'Y':
      print("Terimakasih ")
      print('❤')
      break
    
    elif quit == 'N':
      continue
       
    else:
      print("ketik Y atau N ")
        
      

print("python3 by MR N4T1ON")

