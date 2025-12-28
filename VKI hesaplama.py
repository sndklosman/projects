boy = float(input("boyunuzu giriniz"))
kilo =float(input("kilonuzu kg cinsinden giriniz"))

if boy>100:
     
     indeks = (kilo/(boy/100)**2)

elif boy<100:
       
       indeks = (kilo/(boy**2))

else:
        
        print("lütfen adam akıllı", boy , "ten başka birşey giriniz")

        exit()

print (f"{indeks:.1f}")


if indeks < 18.5:
                
                print("ZAYIF\n" , "ideal kilonuz", boy - 100)
                

if indeks >= 18.5 and indeks <25:

                print("NORMAL\n", "ideal kilonuz", boy - 100)
                

if indeks >= 25 and indeks <30:

                print("FAZLA KİLOLU\n", "ideal kilonuz", boy - 100)
    
if indeks >= 30 and indeks < 35:
   
                print("1.DERECE OBEZİTE\n", "ideal kilonuz", boy - 100)

if indeks >= 35 and indeks <40:

                print("2.DERECE OBEZİTE\n", "ideal kilonuz", boy - 100)

if indeks >= 40:
  
                print("3.DERECE OBEZ\n", "ideal kilonuz", boy - 100)




