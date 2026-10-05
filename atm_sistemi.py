bakiye = 0
def para_cekme(bakiye):
    while True:
        try:
            print("1-200\n2-400\n3-500\n4-Ana menü")

            choice = int(input("İşleminizi seçin: "))

            if choice == 1:
                if bakiye >= 200:
                    bakiye -= 200
                    print("200 TL çekildi. Bakiyeniz:", bakiye)
                else:
                    print("Bakiyeniz yetersiz.")

            elif choice == 2:
                if bakiye >= 400:
                    bakiye -= 400
                    print("400 TL çekildi. Bakiyeniz:", bakiye)
                else:
                    print("Bakiyeniz yetersiz.")

            elif choice == 3:
                if bakiye >= 500:
                    bakiye -= 500
                    print("500 TL çekildi. Bakiyeniz:", bakiye)
                else:
                    print("Bakiyeniz yetersiz.")

            elif choice == 4:
                print("Ana menüye dönülüyor...")
                return bakiye

            else:
                print("Lütfen 1-4 arasında bir seçim yapın.")

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen verilen sayıları kullanın.")
            continue

def para_yatirma(bakiye):
    while True:
        try:
            print("1-200\n2-400\n3-500\n4-Çıkış.")
            choice = int(input("Seçiminiz: "))

            if choice == 1:
                bakiye += 200
                print("200 tl yatırıldı. Bakiyeniz: ", bakiye)

            elif choice == 2:
                bakiye += 400
                print("400 tl yatırıldı. Bakiyeniz: ", bakiye)

            elif choice == 3:
                bakiye += 500
                print("500 tl yatırıldı. Bakiyeniz: ", bakiye)

            elif choice == 4:
                print("Ana menüye dönülüyor.")
                return bakiye

        except ValueError:
            print("Yanlış tuşlama yaptınız. Lütfen verilen sayıları kullanın.")
            continue

def ana_menu(bakiye):
    while True:
        try:
            print("1-Para çekme\n2-Para yatırma\n3-Bakiye görüntüle\n4-Çıkış")

            secim = int(input("Seçiminiz: "))

            if secim == 1:
                bakiye = para_cekme(bakiye)
            elif secim == 2:
                bakiye = para_yatirma(bakiye)
            elif secim == 3:
                print(bakiye)
            elif secim == 4:
                print("Çıkış yapılıyor.")
                break

        except ValueError:
            print("Yanlış seçim yaptınız. Lütfen verilen sayıları kullanın.")
            continue