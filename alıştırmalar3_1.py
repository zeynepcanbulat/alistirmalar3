liste = []
t = 0

while t == 0 :
    tercih = input("Veri çekmek istiyorsanız 'Ç', veri girmek istiyorsanız 'G', işlem yapmak istemiyorsanız 'L' yazınız: ")
    if tercih == "Ç" and len(liste)==0:
        print("Listede çekilecek veri yok!")
    if tercih == "G":
        veri = input("Eklemek istediğiniz veriyi giriniz: ")
        liste.append(veri)
        print(liste)
    if tercih == "Ç" and len(liste)!=0:
        kaç = int(input("Kaç veri çekmek istiyorsunuz?: "))
        for i in range(len(liste)-1,kaç,-1):
            a = liste[i]
            liste.remove(a)
            print("Çektiğiniz veri: {}".format(a))
            print(liste)
    if tercih == "L":
        t = 1

print(liste)
    

            
            
    
    
