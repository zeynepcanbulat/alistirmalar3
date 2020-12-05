liste = []
kaç = int(input("Kaç sayı girmek istiyorsunuz?: "))
küçük = []

for a in range(0,kaç):
    a = int(input(" {}. Veriyi giriniz: ".format(a+1)))
    liste.append(a)

print(liste)

for n in range(0,kaç):
    for i in range(n+1,kaç):
        if int(liste[n])>int(liste[i]):
            küçük.append(liste[i])
    x = 0
    if len(küçük)==0:
        x=1
    else:
        en_küçük = min(küçük)
        print("Küçükler: {}".format(küçük))
        a = liste.index(en_küçük)
        temp = liste[a]
        liste[a] = liste[n]
        liste[n]=temp
        print("liste: {}".format(liste))
        küçük=[]
 
                
            
    
print(liste)
 
