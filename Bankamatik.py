hesaplar = [
    {
        "ad":"ufuk coz",
        "hesapNo": "12345",
        "bakiye": 20000,
        "ekHesap": 5000,
        "username":"ufuk",
        "password":"1234"
    },
    {
        "ad":" Turancan",
        "hesapNo": "12345",
        "bakiye": 30000,
        "ekHesap": 10000,
        "username":"turi",
        "password":"1234"
    }
]

def menu(hesap):
    print("\n")

    print(f"merhaba, {hesap["ad"]}")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")
    print("4- çıkış")

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    elif islem=="4":
        print("çıkış yapılıyor...")
    else:
        print("yanlış seçim")

    menu(hesap)

def paraYatirma(hesap):
    miktar=float(input("yatırmak istediğiniz miktar:  "))
    hesap["bakiye"]+=miktar
    print("paranız yatırıldı  " + str(hesap["bakiye"]))

def bakiyeSorgula(hesap):
    print(f"bakiye: {hesap["bakiye"]}")
    print(f"ek bakiye: {hesap["ekHesap"]}")

def paraCekme(hesap):
    miktar = float(input("çekmek istediğiniz miktar: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimIzni = input("ek hesap kullanılsın mı? (e/h): ")

            if ekHesapKullanimIzni == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("paranızı alabilirsiniz")
            else:
                print("üzgünüz bakiyeniz yetersiz")
        else:
                print("üzgünüz bakiyeniz yetersiz")

def login():
    username = input("username: ")
    password = input("parola: ")

    isLoggedIn = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not(isLoggedIn):
        print("username yada parola yanlış")

login()
