# Kullanıcıların bilgileri kaydedileceği bir sözlük oluşturuluyor
kullanicilar = {}

while True:
    print("Lütfen yapmak istediğiniz işlemi seçin:")
    print("1- Sisteme üye olun")
    print("2- Sisteme giriş yapın")
    print("3- Şifremi unuttum")

    secim = input("Seçiminiz: ")

    # Sisteme üye olma işlemi
    if secim == "1":
        ad = input("Adınız: ")
        sifre = input("Şifreniz: ")
        kullanicilar[ad] = sifre
        print("Başarıyla üye oldunuz.")

    # Sisteme giriş yapma işlemi
    elif secim == "2":
        ad = input("Adınız: ")
        sifre = input("Şifreniz: ")
        if ad in kullanicilar and kullanicilar[ad] == sifre:
            print("Başarıyla giriş yaptınız.")
        else:
            print("Giriş bilgileriniz yanlış.")

    # Şifre sıfırlama işlemi
    elif secim == "3":
        ad = input("Adınız: ")
        if ad in kullanicilar:
            yeni_sifre = input("Yeni şifreniz: ")
            kullanicilar[ad] = yeni_sifre
            print("Şifreniz başarıyla güncellendi.")
        else:
            print("Böyle bir kullanıcı bulunamadı.")

    # Geçersiz seçim
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        