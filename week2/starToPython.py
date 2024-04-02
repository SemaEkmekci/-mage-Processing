# Tek satırlık yorum
"""
birden fazla yorum
yazılabilir

a = 6
b = 20
c = a*b
print(c)

c = b/a
print(c)
c = b//a
print(c)

c = a*2
print(c)
c = a**2
print(c)
print("Pythona Giris")
print('Algoritma Programlama')
print('Algoritma Programlama\'ya Giris')
print("Python'a Giris")
c = 20
print("Goruntu Islemeye " + "Giris")
print("Goruntu Islemeye", "Giris")
print("Puan:" + str(c))
print("Goruntu", "Islemeye", "Giris", sep="-", end=".\n")
c = 10
s = int(input("Bir sayi giriniz:"))
b = c+s
print(b)

str1 = 'kare'
str1 = str1*2
print(str1)

print("ilk karakter:", str1[0])
print("Boyut: ", len(str1))
print("Aralık: ", str1[2:5])

dersler = ["AVP", "Tarih", "Web"]
print(dersler)
notlar = [15, 85, 65]
print(notlar)

dersler = dersler + ["Cografya"]
print(dersler)
dersler.append("Edebiyat")
print(dersler)
dersVeNot = ["Tarih", 45, "Cografya", 85]
print(dersVeNot)
print("Ilk ders", dersVeNot[0], " Not:", dersVeNot[1])
print("Boyut: ", len(dersVeNot))
dersVeNot=[]
print(dersVeNot)

dersler = ("Algoritma","Goruntu")
print(dersler)
print("Ilk ders: ", dersler[0])
dersler = ("Tarih","Goruntu")
print(dersler)

dersler = {"1":"Algoritma", "2":"Veritabani"}
print("Ilk eleman:",dersler["1"])
print("Boyut: ", len(dersler))

s1 = int(input("Ilk sayi:"))
s2 = int(input("Ikinci sayi:"))

if s1>s2:
    print("Buyuk sayi:", s1)
    print("Kucuk sayi:", s2)
elif s2>s1:
    print("Buyuk sayi:", s2)
else:
    print("Sayilar esit!")

# for
notlar = [45, 48, 75, 68, 12]
for x in notlar:
    print(x)
notlar = range(1, 100, 1)
print(notlar)
for x in notlar:
    if x%3 == 0 and x%4 == 0:
        continue
    print(x)

#while
i = 1
while (i%5) != 0:
    print(i)
    i = i+1

def toplam(s1,s2=1):
    t = s1+s2;
    # print("Toplam:", t)
    return t
a = 5
b = 8
tx = toplam(a)
print("Toplam:", tx)
"""
def faktoriyel(sayi):
    f = 1
    i = 2
    while i<=sayi:
        f = f*i
        i=i+1
    return f

x = int(input("Pozitif bir sayi:"))
sonuc = faktoriyel(x)
print("Sayinin faktoriyel degeri:", sonuc)
