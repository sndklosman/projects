print("""Adam Asmaca Oyununa Hoş Geldiniz!\n toplam 6 canınız bulunmakta.
Yanlış harf tahmininde 1 canınızı\nyanlış kelime tahmininde 2 canınızı kaybedersiniz.\nİyi eğlenceler!!""")

print()

import getpass
kelime = getpass.getpass("Rakibinize tahmin ettirmek istediğiniz kelimeyi giriniz: ").lower()

print()
can = 6

kelime_2 = tuple(kelime)

print("Kelime", len(kelime), "harflidir")



while can >0:
 
 
        soru = input("Kelimeyi tahmin etmek istiyor musunuz?(e/h): ").lower()
        print()
        if soru== "e":
              cevap=input("Lütfen tahmininizi giriniz: ").lower()
              if cevap== kelime:
               print()
               print("TEBRİKLER DOĞRU CEVAP!! KAZANDINIZ!!🎉🥳")
               break
              
              else:
               
                  print("YANLIŞ CEVAP!!") 
                  can-=2
                  if can== 0 or can<0:
                   print("canlarınız tükendi")
                   break
                  else:
                   print(can, "can kaldı💔")
                  print()
       
        if soru=="h":
         
         
   
 
         harf = input("Lütfen tahmin etmek istediğiniz harfi giriniz:\t").lower()
         adet = kelime.count(harf)
       
         if harf in kelime:
             
             print("Doğru harf!! girdiğiniz harf kelimede", adet, "kere geçiyor!" )
         else:
             print("Yanlış harf")

             can-=1
             if can== 0 or can<0:
                 print("canlarınız tükendi")
                 break
             else:
                 print(can,"can kaldı💔") 
            


if can==0 or can < 0:
    print("OYUN BİTTİ!KAYBETTİNİZ😢\n doğru cevap:", kelime , "olacaktı")
      
        

