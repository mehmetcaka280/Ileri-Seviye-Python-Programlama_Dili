def double(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)

    return inner


@double
def merhaba():
    print("Merhaba")


@double
def selam(isim):
    print(f"Selam, {isim}")


@double
def ıyı_gunler():
    return "İyi günler"


merhaba()
selam("Mehmet")
print(ıyı_gunler())
