islem_gecmisi = []


def para_cekme(bakiye):
    while True:
        try:
            print("\n1-200\n2-400\n3-500\n4-Farklı tutar\n5-Ana menü")
            choice = int(input("Seçiminiz: "))

            if choice < 1 or choice > 5:
                print("Lütfen 1-5 arasında tuşlama yapınız.")
                continue

            if choice == 1:
                miktar = 200

            elif choice == 2:
                miktar = 400

            elif choice == 3:
                miktar = 500

            elif choice == 4:
                miktar = int(input("Tutarı girin: "))

                if miktar <= 0:
                    print("Tutar 0 veya daha küçük olamaz.")
                    continue

            else:
                break

            if bakiye < miktar:
                print("Bakiyeniz yetersiz.")
                continue

            bakiye -= miktar
            print("Paranız çekildi. Bakiyeniz:", bakiye)

            islem_gecmisi.append(f"-{miktar} TL çekildi.")

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen rakamları kullanın.")

    return bakiye


def para_yatirma(bakiye):
    while True:
        try:
            print("\n1-200\n2-400\n3-500\n4-Farklı tutar\n5-Ana menü")
            choice = int(input("Seçiminiz: "))

            if choice < 1 or choice > 5:
                print("Lütfen 1-5 arasında tuşlama yapınız.")
                continue

            if choice == 1:
                miktar = 200

            elif choice == 2:
                miktar = 400

            elif choice == 3:
                miktar = 500

            elif choice == 4:
                miktar = int(input("Tutarı girin: "))

                if miktar <= 0:
                    print("Tutar 0 veya daha küçük olamaz.")
                    continue

            else:
                break

            bakiye += miktar
            print("Paranız yatırıldı. Bakiyeniz: ", bakiye)

            islem_gecmisi.append(f"+{miktar} TL yatırıldı.")

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen rakamları kullanın.")

    return bakiye


def islem_gecmisini_goster():
    print("\n=============== İŞLEM GEÇMİŞİ ===============")

    if not islem_gecmisi:
        print("Henüz işlem yapılmadı.")
    else:
        for islem in islem_gecmisi:
            print(islem)

    print("=============================================")


def pin_kontrol():
    hak = 3

    while hak > 0:
        try:
            pin = int(input("Şifreyi girin: "))

            if pin == 1234:
                return True

            hak -= 1
            print("Şifreniz yanlış. Kalan hak:", hak)

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen rakamları kullanın.")

    return False


def ana_menu(bakiye):
    while True:
        try:
            print("\n1-Bakiye")
            print("2-Para çekme")
            print("3-Para yatırma")
            print("4-İşlem geçmişi")
            print("5-Çıkış")

            choice = int(input("Seçiminiz: "))

            if choice < 1 or choice > 5:
                print("Lütfen 1-5 arasında tuşlama yapınız.")
                continue

            if choice == 1:
                print("Bakiyeniz:", bakiye)

            elif choice == 2:
                bakiye = para_cekme(bakiye)

            elif choice == 3:
                bakiye = para_yatirma(bakiye)

            elif choice == 4:
                islem_gecmisini_goster()

            elif choice == 5:
                print("Çıkış yapılıyor...")
                break

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen rakamları kullanın.")


bakiye = 0

if pin_kontrol():
    ana_menu(bakiye)
else:
    print("Kartınız bloke oldu..........")