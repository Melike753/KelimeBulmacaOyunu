import pygame as pg
import sys,random

def kutu_koy():
    ekran.blit(harf_kutusu, (index*110+290,330))

pg.init()
ekran = pg.display.set_mode((1400,750))
zaman = pg.time.Clock()

sorular = [
    "1-Hamur kızartması",
    "2-Yaprakları salata olarak yenen baharlı bir bitki",
    "3-Bir emek sonucu ortaya konulan ürün , eser",
    "4-Futboldaki canlı barikat",
    "5-Kısa süreli, beklenmedik saldırı",
    "6-Halk ağzında küçük sıvı püskürteçlerine verilen isim",
    "7-Kandaki alkol miktarını gösteren birim",
    "8-Yıkanma,tıraş olma , giyinme, süslenme işi",
    "9-Sesi büyütüp , yükseltip uzaklara ileten koni biçiminde aygıt",
    "10-Hristiyan olmayan toplumlarda bu dini yaymaya çalışan kimse",
    "11-Endüstri Mühendisliği'nin en önemli alanlarından , ... araştırması",
    "12-Aralarında ya da parçaları arasında bakışım bulunan",
    "13-Yayılı aletler, bisiklet , araba parçaları, araba tekerliği ve aksamı",
    "14-X Y düzlemi , ikişerli 6 tane rakam , küp çizimi , dünya çizimi",
    "15-Boyları 1 milimetreyle 1 metre arasında değişen elektromanyetik salınım",
    "16-Belirsizlik ilkesini öne süren Alman Fizikçi",
    "OYUN BİTTİ"
]

cevaplar = [
    "PİŞİ","TERE","YAPIT","BARAJ","BASKIN","FISFIS","PROMİL","TUVALET","MEGAFON","MİSYONER","YÖNEYLEM","SİMETRİK","AMARTİSÖR","KOORDİNAT","MİKRODALGA","HEİSENBERG",""
]

arkaplan = pg.image.load("arkaplan.png")
harf_kutusu= pg.image.load("harf_kutusu.png")
soru_indexi = -1
oyun_fontu = pg.font.Font(None,45)
kutuları_yerleştir = False
harf_alayım = False
kelimeyi_goster = False
yazı_yüzeyleri = []
harf_dörtgenleri = []
yazı_yüzeyleri2 = []
harf_dörtgenleri2 = []
skor = 0
alinmayan_harf_sayisi = 0
alinan_harf_sayisi = 0
durdurulan_sure_soruluk = 0
toplam_durdurulan_sure = 0
sureyi_durdur = False

while True:
    gercek_zaman = pg.time.get_ticks()
    ekran.blit(arkaplan,(0,0))
    for olay in pg.event.get():
        if olay.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if olay.type == pg.KEYDOWN:
            if olay.key == pg.K_RETURN: # Enter tuşuna basmak anlamına geliyor.
                soru_indexi += 1
                kutuları_yerleştir = True
                alınan_harf_indexi = []
                yazı_yüzeyleri = []
                harf_dörtgenleri = []
                skor += (100*alinmayan_harf_sayisi)
                alinan_harf_sayisi = 0
                yazı_yüzeyleri2 = []
                harf_dörtgenleri2 = []
                kelimeyi_goster = False
                toplam_durdurulan_sure += durdurulan_sure_soruluk
                durdurulan_sure_soruluk = 0
                sureyi_durdur = False

            if olay.key == pg.K_SPACE:
                harf_alayım = True

            if olay.key == pg.K_RSHIFT: # Sağdaki Shift tuşu
                kelimeyi_goster = True

            if olay.key == pg.K_BACKSPACE:
                sureyi_durdur = True
                surenin_durduruldugu_an = gercek_zaman

    
    if kutuları_yerleştir == True:
        for index in range(len(cevaplar[soru_indexi])):
            kutu_koy()
        
        soru_yüzeyi = oyun_fontu.render(sorular[soru_indexi],True,(255,255,255))
        soru_dörtgeni = soru_yüzeyi.get_rect(topleft=(250,550))
        ekran.blit(soru_yüzeyi,soru_dörtgeni)
        kutuları_yerleştir == False

    if harf_alayım == False:
        alinmayan_harf_sayisi = len(cevaplar[soru_indexi]) - alinan_harf_sayisi
   
    if harf_alayım == True:
        harf_yeri = "a"
        uygun_harf = True
        alinmayan_harf_sayisi = len(cevaplar[soru_indexi]) - alinan_harf_sayisi
        while uygun_harf:
            if len(alınan_harf_indexi) != len(cevaplar[soru_indexi]):
                harf_yeri = random.randint(0, len(cevaplar[soru_indexi])-1)
                if not harf_yeri in alınan_harf_indexi: # Eğer daha önce bu harfi almadıysak
                    alınan_harf_indexi.append(harf_yeri)
                    uygun_harf = False 
                    alinan_harf_sayisi += 1

            if len(alınan_harf_indexi) == len(cevaplar[soru_indexi]):
                harf_alayım = False
                alinmayan_harf_sayisi = 0

        for i in alınan_harf_indexi:
            yazı = pg.font.Font(None, 100)
            yazı_yüzeyi = yazı.render(cevaplar[soru_indexi][i], True,(0,0,0))
            yazı_yüzeyleri.append(yazı_yüzeyi)
            harf_dörtgeni = yazı_yüzeyi.get_rect(center = (i*110+345,395))
            harf_dörtgenleri.append(harf_dörtgeni)   
        harf_alayım = False 

    for j in range(len(harf_dörtgenleri)):
        ekran.blit(yazı_yüzeyleri[j],harf_dörtgenleri[j])   

    renk = (0,0,0)
    sayac_fontu = pg.font.Font(None,65)

    if sureyi_durdur == True :
        durdurulan_sure_soruluk = gercek_zaman - surenin_durduruldugu_an
        renk = (255,0,0)

    sayactan_eksilen = gercek_zaman - durdurulan_sure_soruluk - toplam_durdurulan_sure
    
    if sayactan_eksilen >= 0 and sayactan_eksilen < 60000:
        dakika = f'4:{59-int((sayactan_eksilen/1000))}'
        sayac_yuzeyi = sayac_fontu.render(str(dakika),True,renk)
    if sayactan_eksilen >= 60000 and sayactan_eksilen < 120000:
        dakika = f'3:{119-int((sayactan_eksilen/1000))}'
        sayac_yuzeyi = sayac_fontu.render(str(dakika),True,renk)
    if sayactan_eksilen >= 120000 and sayactan_eksilen < 180000:
        dakika = f'2:{179-int((sayactan_eksilen/1000))}'
        sayac_yuzeyi = sayac_fontu.render(str(dakika),True,renk)
    if sayactan_eksilen >= 180000 and sayactan_eksilen < 240000:
        dakika = f'1:{239-int((sayactan_eksilen/1000))}'
        sayac_yuzeyi = sayac_fontu.render(str(dakika),True,renk)
    if sayactan_eksilen >= 240000 and sayactan_eksilen < 300000:
        dakika = f'0:{299-int((sayactan_eksilen/1000))}'
        sayac_yuzeyi = sayac_fontu.render(str(dakika),True,renk)
    

    if kelimeyi_goster == True:
        for i in range(len(cevaplar[soru_indexi])):
            yazı = pg.font.Font(None,100)
            yazı_yüzeyi = yazı.render(cevaplar[soru_indexi][i],True,(0,0,0))
            yazı_yüzeyleri2.append(yazı_yüzeyi)
            harf_dörtgeni = yazı_yüzeyi.get_rect(center = (i*110+345,395))
            harf_dörtgenleri2.append(harf_dörtgeni)
        
        for j in range(len(cevaplar[soru_indexi])):
            ekran.blit(yazı_yüzeyleri2[j],harf_dörtgenleri2[j])

    ekran.blit(sayac_yuzeyi, (250, 255))

    skor_fontu = pg.font.Font(None,75)
    skor_yuzeyi = skor_fontu.render(str(skor),True,(0,0,0))
    ekran.blit(skor_yuzeyi,(250,205))

    pg.display.update()
    zaman.tick(60)