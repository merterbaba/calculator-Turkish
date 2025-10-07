const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function ask(soru) {
  return new Promise(resolve => rl.question(soru, cevap => resolve(cevap)));
}

async function hesapMakinesi() {
  while (true) {
    console.log("----------HESAP MAKİNESİ----------");

    const a = parseFloat(await ask("İlk rakamı giriniz: "));
    const b = parseFloat(await ask("İkinci rakamı giriniz: "));
    const islem = await ask("Yapmak istedeğiniz islem türünü seçiniz (+,-,*,/): ");

    if (islem === "+") {
      console.log("Sonuc:", a + b);
    } else if (islem === "-") {
      console.log("Sonuc:", a - b);
    } else if (islem === "*") {
      console.log("Sonuc:", a * b);
    } else if (islem === "/") {
      console.log("Sonuc:", a / b);
    } else {
      console.log("Geçersiz islem");
    }

    console.log("İslem tamamlandı.\n");
  }
}

hesapMakinesi();
