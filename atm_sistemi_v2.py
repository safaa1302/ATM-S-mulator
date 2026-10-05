def para_cekme(bakiye):
    while True:
        try:
            print("1-200\n2-400\n3-500\n4-Farklı tutar\n5-Ana menü")
            choice = int(input("Seçiminiz: "))
            if choice <1 or choice >5:
                print("Lütfen 1-5 arasında tuşlama yapın.")
                continue

            if choice == 1:
                if bakiye < 200:
                    print("Bakiyeniz yetersiz.")
                    continue
                else:
                    bakiye -= 200
                    print("Paranız çekildi. Bakiyeniz: ", bakiye)

            elif choice == 2:
                if bakiye < 400:
                    print("Bakiyeniz yetersiz.")
                    continue
                else:
                    bakiye -= 400
                    print("Paranız çekildi. Bakiyeniz: ", bakiye)

            elif choice == 3:
                if bakiye < 500:
                    print("Bakiyeniz yetersiz.")
                    continue
                else:
                    bakiye -= 500
                    print("Paranız çekildi. Bakiyeniz: ", bakiye)

            elif choice == 4:
                miktar = int(input("Tutarı girin: "))
                if miktar <= 0:
                    print("Tutar 0 veya daha küçük olamaz.")
                    continue
                elif bakiye < miktar:
                    print("Bakiyeniz yetersiz.")
                    continue
                bakiye -= miktar
                print("Paranız çekildi. Bakiyeniz: ", bakiye)

            elif choice == 5:
                break

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen rakamları kullanın.")
    return bakiye


def para_yatirma(bakiye):
    while True:
        try:
            print("1-200\n2-400\n3-500\n4-Farklı tutar\n5-Ana menü")
            choice = int(input("Seçiminiz: "))
            if choice < 1 or choice > 5:
                print("Lütfen 1-5 arasında rakamları kullanın.")
                continue

            if choice == 1:
                bakiye += 200
                print("Paranız yatırıldı. Bakiyeniz: ", bakiye)

            elif choice == 2:
                bakiye += 400
                print("Paranız yatırıldı. Bakiyeniz: ", bakiye)

            elif choice == 3:
                bakiye += 500
                print("Paranız yatırıldı. Bakiyeniz: ", bakiye)

            elif choice == 4:
                miktar = int(input("Tutarı girin: "))
                if miktar <= 0:
                    print("Tutar 0 veya daha küçük olamaz.")
                    continue
                bakiye += miktar

            elif choice == 5:
                break

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen rakamları kullanın.")
    return bakiye

def pin_kontrol():
    hak = 3

    while hak > 0:
        try:
            pin = int(input("Şifreyi girin: "))
            if pin == 1234:
                return True
            elif pin != 1234:
                hak -= 1
                print("Yanlış şifre. Kalan hak: ", hak)

        except ValueError:
            print("Lütfen rakam kullanın.")
    return False

def ana_menu(bakiye):
    while True:
        try:
            print("1-Bakiye\n2-Para çekme\n3-Para yatırma\n4-Çıkış")
            choice = int(input("Seçiminiz: "))
            if choice < 1 or choice > 4:
                print("Lütfen 1-4 arasında tuşlama yapın.")
                continue

            if choice == 1:
                print(bakiye)

            elif choice == 2:
                bakiye = para_cekme(bakiye)

            elif choice == 3:
                bakiye = para_yatirma(bakiye)

            elif choice == 4:
                break

        except ValueError:
            print("Lütfen rakamları kullanın.")

bakiye = 0
if pin_kontrol():
    ana_menu(bakiye)
else:
    print("Kartın bloke oldu.")
