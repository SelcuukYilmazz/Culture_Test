#SKORLAR
A = 5
B = 10
C = 15
D = 20
E = 25
G = 15000
H = 0
#GEREKLİ FONKSİYON
def fonksiyon(cevap,a,b,c,d,e):
    if cevap == "a":
        cevap = int(a)
    elif cevap == "b":
        cevap = int(b)
    elif cevap == "c":
        cevap = int(c)
    elif cevap == "d":
        cevap = int(d)
    elif cevap == "e":
        cevap = int(e)
    else:
        print("DANGALAK")
    return cevap
#SORULAR
q1 = "soru1"
q2 = "soru2"
q3 = "soru3"
q4 = "soru4"
q5 = "soru5"
q6 = "soru6"
q7 = "soru7"
print(q1, ":", "En sevdiğin şarkı")
A1 = "a) Avicii-The Nights"
B1 = "b) Tarkan-Kuzu Kuzu"
C1 = "c) Manga-Dünyanın Sonuna Doğmuşum"
D1 = "d) Hooverphonic-Eden"
E1 = "e) Bahar Candan - Yaz Meyvesi"
print(A1,B1,C1,D1,E1)
cevap1 = input("cevabınız: ")
print(q2,":","En Sevdiğin Film")
A2 = "a)Interstaller"
B2 = "b)Esaretin Bedeli"
C2 = "c)The Great Gatsby"
D2 = "d)Inception"
E2 = "e)Yeşil Yol"
print(A2,B2,C2,D2,E2)
cevap2 = input("cevabınız: ")
print(q3,":","En Sevdiğin Aktivite")
A3 = "a)Uyumak"
B3 = "b)Yemek yemek"
C3 = "c)Oyun oynamak"
D3 = "d)Gezmek"
E3 = "e)Sosyalleşmek"
print(A3,B3,C3,D3,E3)
cevap3 = input("cevabınız: ")
print(q4,":","Hayat Amacın")
A4 = "a)Mutluluk"
B4 = "b)Statü"
C4 = "c)Yok"
D4 = "d)Para"
E4 = "e)Aşk"
print(A4,B4,C4,D4,E4)
cevap4 = input("cevabınız: ")
print(q5,":","Bir Müzik Aleti Seç")
A5 = "a)Piyano"
B5 = "b)Keman"
C5 = "c)Mızıka"
D5 = "d)Davul"
E5 = "e)Gitar"
print(A5,B5,C5,D5,E5)
cevap5 = input("cevabınız: ")
print(q6,":","Önceliklerin")
A6 = "a)Ailen"
B6 = "b)Mutluluğun"
C6 = "c)Başarıların"
D6 = "d)Kariyerin"
E6 = "e)Para"
print(A6,B6,C6,D6,E6)
cevap6 = input("cevabınız: ")
print(q7,":","GİZLİ OYUNA GİTMEK İÇİN E ŞIKKINI SEÇ")
A7 = "a)..."
B7 = "b)..."
C7 = "c)..."
D7 = "d)..."
E7 = "e)HARİKALAR DİYARI."
print(A7,B7,C7,D7,E7)
cevap7 = input("cevabınız: ")

fonksiyon(cevap1,A,B,C,D,E)
fonksiyon(cevap2,A,B,C,D,E)
fonksiyon(cevap3,A,B,C,D,E)
fonksiyon(cevap4,A,B,C,D,E)
fonksiyon(cevap5,A,B,C,D,E)
fonksiyon(cevap6,A,B,C,D,E)
fonksiyon(cevap7,H,H,H,H,G)

sonuc = int(fonksiyon(cevap1,A,B,C,D,E)) + int(fonksiyon(cevap2,A,B,C,D,E)) + int(fonksiyon(cevap3,A,B,C,D,E)) + int(fonksiyon(cevap4,A,B,C,D,E)) + int(fonksiyon(cevap5,A,B,C,D,E)) + int(fonksiyon(cevap6,A,B,C,D,E)) + int(fonksiyon(cevap7,H,H,H,H,G))
if sonuc == 150 :
    print("Sağlam trolsün he :D.")
elif sonuc >= 1000:
    print("KALANASA-Sonsuz döngüye girdin kurtuluş yolun saklı :D.Benim adım KALANASA bu arada")
    while 1:
        print("KALANASA-1. yol çok güzel onu seçsene")
        print("KALANASA-Ya da bilemedim 2. de çok güzel")
        print("KALANASA-Offf biliyo musun 4. yolun sonunda Charlie'nin Çikolata Fabrikası var hadi oraya gidelim hadi")
        print("1.Çiçekli Yol","2.Periler Ülkesinin Kapısı","3.Meyhane","4.Charlie'nin Çikolata Fabrikası")
        x = int(input("nerden gidelim nerden gidelim????"))
        if x == 1:
            print("Şekerden ev buldun içeri girecek misin yoksa geri mi döneceksin")
            print("1-İçeri Gir","2-Geri Dön","3-Bir daha mı gelcen dünyaya aq ye bütün evi")
            y = int(input("seçimin "))
            if y == 1:
                print("KALANASA-Olamaz cadıya yakalandın. En azından ölmeden önce baya yemek yiyebileceksin gülümse")
                break
            elif y == 2:
                print("KALANASA-AAA HADİ AMA. Cadının evinin içini görmek istiyordum senden nefret etmeye başladım sıkıcı :(")
                continue
            elif y == 3:
                print("KALANASA-Dostum beni korkutuyorsun umarım o midenin de bi sınırı vardır.")
                print("O kadar çok yedin ki cadı seni yakalamak için uğraşmadı bile şimdi bir kafeste oturmuş ölümü bekliyorsun")
                break
        elif x == 2:
            print("KALANASA-Dostum harikasın perilerle sonunda tanışabilicem")
            print("KALANASA-Biliyor musun perilerin çok iyi alkol yaptıklarını duymuştum")
            print("KALANASA-Sadece söylüyorum hemen tepki vermene gerek yok :)")
            print("KALANASA-Bak bir meyhane yanında da pek tekin durmayan 2 peri var ne yapalım dersin.")
            print("1-Meyhaneye Gir","2-Geri Dön","3-Biraz kan dökelim ne dersin")
            z = int(input("seçimin "))
            if z == 1:
                print("Kapıdaki periler burdan olmadığını anladı")
                print("Seni biraz tartaklayıp köle pazarına doğru götürüyorlar")
                print("KALANASA-Üzgünüm dostum köle olman üzücü ama bu bira için değerdi ama emin ol.")
                break
            elif z == 2:
                print("KALANASA-HADİ AMAAAAAA SEN TAM BİR YAŞLI CADISIN!!!!")
                print("KALANASA-Canım biralarım geri döncem bekleyin beni")
                continue
            elif z == 3:
                print("KALANASA-İşte bu dostum hepsini öldürdün sen harikasın")
                print("KALANASA-Şimdi cezanı çekme vaktin geldi seni lanet katil.")
                print("KALANASA-AĞLA")
                while 1:
                    print("AĞLA")
        elif x == 3:
            print("KALANASA-Dostum kurtuluşun kapısı her zaman alkolden geçiyor doğru seçim seni lanet olası")
            print("KALANASA-Seni sevmeye başlamıştım neyse elveda :*")
            break
        elif x == 4:
            print("KALANASA-WOHOOOOOO sonunda kendi fabrikama geldim")
            print("KALANASA-AHHH özür dilerim kendimi tanıtmadım ben KALANASA DE LA CHARLIE yim.")
            print("ne istersin seni genç çikolata mı şeker mi yoksa eve dönmeyi mi.")
            print("1-Çikolata","2-Şeker","3-Eve döneyim ben")
            k = int(input("seçimin "))
            if k == 1:
                print("KALANASA-O LA LA bir çikolatanın olmazsa olmazı bir gençtir")
                print("KALANASA- Seni birazdan çikolata yaparız canım eminim çok daha faydalı olucaksındır")
                break
            elif k == 2:
                print("KALANASA-Şeker mi ahh demek senin gibi şeker bir genç şeker istiyor")
                print("KALANASA-MARŞ MARŞ çalışanlarım hemen şeker getirin")
                print("şekerde ilaç vardır ve sonsuz komada kalırsın.")
                while 1:
                    print("YABANCILARDAN ŞEKER ALMA!!!")
            elif k == 3:
                print("KALANASA-Hadi amaaaaa senle biraz bile eğlenemeyecek miyiz biz lanet olsun.")
                continue

elif sonuc > 125:
    print("Hadi canım dalga geçiyorsun heralde.")
elif sonuc > 100:
    print("Hafiften bi kültür kokusu aldım hocam böyle devam.")
elif sonuc > 50:
    print("İlber Ortaylı girse bence tam böyle yapardı etkilendim.")
elif sonuc > 10:
    print("Bahse girerim Sherlock cosplayi yapan bir dahisin.")
print(sonuc)
input("kapatmak için enter'a basınız... ")


