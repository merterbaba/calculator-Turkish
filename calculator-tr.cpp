#include <iostream>
using namespace std;

int main() {
    while (true) {
        int a, b;
        char islem;

        cout << "----------HESAP MAKİNESİ----------\n";
        cout << "İlk rakamı giriniz: ";
        cin >> a;
        cout << "İkinci rakamı giriniz: ";
        cin >> b;
        cout << "Yapmak istedeğiniz islem türünü seçiniz (+,-,*,/): ";
        cin >> islem;

        if (islem == '+') {
            cout << "Sonuc: " << a + b << endl;
        } else if (islem == '-') {
            cout << "Sonuc: " << a - b << endl;
        } else if (islem == '*') {
            cout << "Sonuc: " << a * b << endl;
        } else if (islem == '/') {
            cout << "Sonuc: " << (float)a / b << endl;
        } else {
            cout << "Geçersiz islem\n";
        }

        cout << "İslem tamamlandı.\n\n";
    }
    return 0;
}
