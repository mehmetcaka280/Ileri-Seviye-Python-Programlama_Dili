def selamlama(fn):
    def inner(ad):
        print("Hoşgeldiniz")
        fn(ad)
        print("Görüşmek üzere")

    return inner


@selamlama
def gunaydın(ad):
    print(f"Günaydın benim adım {ad}")


@selamlama
def ıyı_gunler(ad):
    print(f"İyi günler benim adım {ad}")


# g=selamlama(gunaydın)
# i=selamlama(ıyı_gunler)

# g()
# i()

gunaydın("Mehmet")
ıyı_gunler("Mehmet")
