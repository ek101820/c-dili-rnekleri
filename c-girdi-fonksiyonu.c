#include <stdio.h>
#include <stdlib.h>

int main()
{ //girdi fonksiyonu
    /*int sayi;
    printf(" sayi giriniz:");
    scanf("%d" , &sayi);
    printf("benim girdigim sayi %d" , sayi);
    return 0;*/

    /*dairenin çevresi ve alanı bulan program
    1-variables tanımla
    2-variables type bul
    3-formulu tanımla = pi*r*r  cevre=2*pi*r
    4-kullanıcıdan verileri al
    5-işlem yap
    6-cıktı ver*/
 // const float degişmez deger verilmez
    float r,cevre,alan;
    const float PI=3.1415;
    printf("dairenin yaricapini giriniz:");
    scanf("%f",&r);

    cevre=2*PI*r;
    alan=PI*r*r;
    printf("dairenin cevresi:%f\n",cevre);
    printf("dairenin alanı:%d",alan);
