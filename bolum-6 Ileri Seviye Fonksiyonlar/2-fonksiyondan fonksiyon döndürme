def us_alma(taban):
    def inner(us):
        return taban**us

    return inner


# sonuc=us_alma(2)(3)
# fn=us_alma(2)
# sonuc=fn(4)


# def yetki_sorgulama(sayfa):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} rolü {sayfa} sayfasına ulaşabilir."
#         else:
#             return f"{role} rolü {sayfa} sayfasına ulaşamaz."

#     return inner


# yetki = yetki_sorgulama("ürün güncelleme")
# sonuc = yetki("Müşteri")
# print(sonuc)


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi=="toplama":
        return toplam
    else:
        return carpim


toplama = islem("toplama")
carpma = islem("carpma")

sonuc=toplama(10,20)
sonuc=carpma(10,20)

print(sonuc)