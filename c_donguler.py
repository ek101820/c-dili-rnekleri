/* while
do while
for*/

while =şifre beklemek gibi
koşul odaklı
koşul true olana kadar calısır
şifre dogru olana kadar sorulur
i++ yani artısı yapmazsan eger program durmaz

for 
Bi işlemiin kaç kere yapıldıgını biliyorsan kullanılırız yani 10 satır yazdır, 50 kere dön gibi...
Tekrar sayısı bellidir
Baslamgıc bitis ve artıs tek satırdadır

do while önce işlemi yap sonra bana sor
önce işi yapar sonra sartı kabul eder yani şart yanlıs olsa bile dongu en az 1 kere calısır

for: "Öğretmen 100 kere 'Ödevimi yapacağım' yaz dedi." (Sayı belli)

while: "Karnın doyana kadar yemek ye." (Önce karnın aç mı diye bakarsın, toksan hiç yemezsin)

do-while: "Yemeğin tadına bak, eğer tuzu azsa tuz ekle." (Önce tadına bakarsın, sonra kontrol edersin)

for döngüsü tekar sayısını biliyorsan 
Senaryo: "Ekrana 10 tane yıldız bas."
Senaryo: "Bir sınıftaki 30 öğrencinin notlarını hesapla."
Senaryo: "Dizideki (liste) 50 tane sayıyı ekrana yazdır."
Neden for? Çünkü başlangıcı (1), bitişi (10) ve artışı (birer birer) tek satırda görebilirsin.


while döngüsü
durum ve şart devam ettigi surece bir sey yapacaksan ama kac kez sürecegini bilmiyorsan
Senaryo: "Kullanıcı doğru şifreyi girene kadar sormaya devam et." (Belki 1. denemede bilecek, belki 100. denemede; bilemeyiz.)
Senaryo: "İnternet bağlantısı gelene kadar bağlanmayı dene."
Senaryo: "Karakterin canı 0'dan büyük olduğu sürece oyunu devam ettir."
Neden while? Çünkü odak noktan sayı değil, bir şartın (can > 0 gibi) bozulup bozulmamasıdır.

do while
işlemin en az bir kere yapılmasını istiyorsan
Senaryo: "Bir menü göster (1-Çıkış, 2-Hesapla). Kullanıcı 1'e basmadığı sürece menüyü göstermeye devam et."
Senaryo: "Kullanıcıdan bir sayı al. Eğer sayı negatifse tekrar iste." (Önce sayıyı bir kez almalısın ki sonra kontrol edebilesin.)
Neden do-while? Çünkü önce "yapıyorsun", sonra "devam edeyim mi?" diye soruyorsun.


Kaç kere döneceğini biliyor muyum?
Evet for kullan.
Dönüş sayısı belli değil ama bir şart mı var?
Evet  while kullan.
Şart ne olursa olsun bu kod en az bir kez çalışmalı mı?
Evet do-while kullan.




ÖRNEKLER
int main() {
    int tutulanSayi = 7;
    int tahmin;
    int i;

    printf("3 Hakkin var! 1 ile 10 arasinda bir sayi tuttum.\n");

    // i=1'den başla, 3 olana kadar devam et, her seferinde 1 artır.
    for (i = 1; i <= 3; i++) {
        printf("%d. denemen: ", i);
        scanf("%d", &tahmin);

        if (tahmin == tutulanSayi) {
            printf("Tebrikler! %d. denemede bildin.\n", i);
            break; // Doğru bildiği için döngüden hemen çık (3 hakkın bitmesini bekleme)
        } else {
            printf("Yanlis!\n");
        }
    }

    if (tahmin != tutulanSayi) {
        printf("Hakkin bitti! Sayi %d idi. Kaybettin.\n", tutulanSayi);
    }

    return 0;
}


int i=0;                                i:0 //i 5 den kucukse yazar.
while(i<5){                             i:1 
  printf("i:%d \n",i);                  i:2 
i++; // ya da i=i+1                     i:3
}                                       i:4


int main() {
   int j=0;
do
{
  printf("%d\n",j);
  j++;
}while(j<2);

    return 0;
}


continue //continue den sonra devamını yapmadan bir sonraki degere gecmesini saglar
if(k==2)
continue // yani ekrana 2 yazdırma bi sonrakine gec 1 den 3 gecer 
1
3
4
diye ekrana yazdırır.
break //döngüden cıkmayı saglar






















