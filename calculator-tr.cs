using System;

class Program {
    static void Main() {
        while (true) {
            Console.WriteLine("----------HESAP MAKİNESİ----------");

            Console.Write("İlk rakamı giriniz: ");
            int a = int.Parse(Console.ReadLine());

            Console.Write("İkinci rakamı giriniz: ");
            int b = int.Parse(Console.ReadLine());

            Console.Write("Yapmak istedeğiniz islem türünü seçiniz (+,-,*,/): ");
            string islem = Console.ReadLine();

            if (islem == "+") {
                Console.WriteLine("Sonuc: " + (a + b));
            } else if (islem == "-") {
                Console.WriteLine("Sonuc: " + (a - b));
            } else if (islem == "*") {
                Console.WriteLine("Sonuc: " + (a * b));
            } else if (islem == "/") {
                Console.WriteLine("Sonuc: " + ((float)a / b));
            } else {
                Console.WriteLine("Geçersiz islem");
            }

            Console.WriteLine("İslem tamamlandı.\n");
        }
    }
}
