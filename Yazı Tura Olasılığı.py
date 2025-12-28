import random 

yazitura= ["yazı","tura"]

bilgisayar_secimi= ["yazı","tura"]
random.choice (bilgisayar_secimi)

el_adedi= 1_000_000

tura=0

yazi=0

for i in range(0,el_adedi):

    if random.choice (bilgisayar_secimi)=="tura":

        tura = tura +1

    else:

        yazi=yazi+1

print (f"tura gelme olasılığı: {tura/el_adedi:.2%}")
print (f"yazı gelme olasılığı: {yazi/el_adedi:.2%}")

    





