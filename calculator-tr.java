import java.util.Scanner;

public class HesapMakinesi {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.println("----------HESAP MAKİNESİ----------");

            System.out.print("İlk rakamı giriniz: ");
            int a = input.nextInt();

            System.out.print("İkinci rakamı giriniz: ");
            int b = input.nextInt();

            System.out.print("Yapmak istedeğiniz islem türünü seçiniz (+,-,*,/): ");
            String islem = input.next();

            if (islem.equals("+")) {
                System.out.println("Sonuc: " + (a + b));
            } else if (islem.equals("-")) {
                System.out.println("Sonuc: " + (a - b));
            } else if (islem.equals("*")) {
                System.out.println("Sonuc: " + (a * b));
            } else if (islem.equals("/")) {
                System.out.println("Sonuc: " + ((float)a / b));
            } else {
                System.out.println("Geçersiz islem");
            }

            System.out.println("İslem tamamlandı.\n");
        }
    }
}   
