while True:
        print("----------HESAP MAKİNESİ----------")
        a = int(input("İlk rakamı giriniz:")) #kullanıcın girdiği ilk sayıyı bir değişkene tanımla.
        b = int(input("İkinci rakamı giriniz:"))#kullanıcın girdiği ikinci sayıyı bir değişkene tanımla.
        islem = input("Yapmak istedeğiniz islem türünü seçiniz.(+,-,*,/)")#kullanıcının yapaçağı işlemi bir değişkene tanımla.
        if islem == "+": #eğer + yazarsa a ve b değişkenini toplayıp yaz.
            print("Sonuc:",a + b)
        elif islem == "-": #eğer - yazarsa a ve b değişkenini toplayıp yaz.
            print("Sonuc:",a - b)
        elif islem == "*": #eğer * yazarsa a ve b değişkenini toplayıp yaz.
            print("Sonuc:",a * b)
        elif islem == "/": #eğer / yazarsa a ve b değişkenini toplayıp yaz.
            print("Sonuc:",a / b)
        else:  #eğer bu dürdünden başka birşey yazarsa gerekli komutu yazdır.
            print("Geçersiz islem")
        print("İslem tamamlandı.") #işlemin tamamlandığına dair çıktı
