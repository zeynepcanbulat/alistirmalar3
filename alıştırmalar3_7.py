liste = []
kaç = int(input("Kaç sayı girmek istiyorsunuz?: "))

for a in range(0,kaç):
    a = int(input(" {}. Veriyi giriniz: ".format(a+1)))
    liste.append(a)

print("liste: {}".format(liste))
for n in range (1,kaç):
    for i in range (0,len(liste)-1):
        if int(liste[i]) > int(liste[i+1]):
            temp = liste[i+1]
            liste[i+1] = liste[i]
            liste[i] = temp
        
        print(liste)
    print(liste)


        
