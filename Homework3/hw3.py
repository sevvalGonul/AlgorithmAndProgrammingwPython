hasta_maske_takmis_mi = input("COVID-19 hastasında tıbbi maske takılmış olup olmadığını giriniz (e/h): ")
N95_endikasyonu = input("N95 endikasyonu olup olmadığını giriniz (e/h): ") #Sağlık çalışanının N95 kullanma gerekliliği var mı?
saglik_calisani_maske = input("Sağlık çalışanının maske kullanım durumunu giriniz (t: tıbbi, n: N95, h: hiçbiri): ")
goz_koruyucu_kullanimi = input("Sağlık çalışanının göz koruyucu kullanıp kullanmadığını giriniz (e/h): ")
eldiven_onluk_kullanimi = input("Sağlık çalışanının eldiven&önlük kullanıp kullanmadığını giriniz (e/h): ")

yuksek_riskli = False
orta_riskli = False
dusuk_riskli = False

#Sağlık çalışanının risk kategorisini belirleme:

if hasta_maske_takmis_mi == "e": #Hasta maskeliyken:
    #Sağlık çalışanı maske takmamışsa veya N95 takması gerekirken tıbbi maske takmışsa orta riskli.
    if saglik_calisani_maske == "h" or (N95_endikasyonu == "e" and saglik_calisani_maske == "t"):
        print("Sağlık çalışanı Orta Riskli kategoridedir.")
        orta_riskli = True
    #Sağlık çalışanı göz koruyucu veya eldiven önlük kullanmamışsa düşük riskli
    elif goz_koruyucu_kullanimi == "h" or eldiven_onluk_kullanimi == "h":
        print("Sağlık çalışanı Düşük Riskli kategoridedir.")
        dusuk_riskli = True
    #Tüm kişisel koruyucu ekipmanları uygun kullanmışsa risksiz
    else:
        print("Sağlık çalışanı Risksiz kategoridedir.")
else: #Hasta maskesizken:
    #Sağlık çalışanı maske takmamışsa yüksek riskli.
    if saglik_calisani_maske == "h":
        print("Sağlık çalışanı Yüksek Riskli kategoridedir.")
        yuksek_riskli = True
    #Göz koruyucu kullanmamışsa veya N95 kullanması gerekirken tıbbi maske kullanmışsa orta riskli.
    elif goz_koruyucu_kullanimi == "h" or (N95_endikasyonu == "e" and saglik_calisani_maske == "t"):
        print("Sağlık çalışanı Orta Riskli kategoridedir.")
        orta_riskli = True
    #Eldiven önlük kullanmamışsa düşük riskli
    elif eldiven_onluk_kullanimi == "h":
        print("Sağlık çalışanı Düşük Riskli kategoridedir.")
        dusuk_riskli = True
    #Tüm kişisel koruyucu ekipmanları uygun kullanmışsa risksiz.
    else:
        print("Sağlık çalışanı Risksiz kategoridedir.")

#Semptom gelişmezse 7. günde PCR testi yapılmasının gerekli olup olmadığı:
if yuksek_riskli or orta_riskli: #Sağlık çalışanı yüksek riskli veya orta riskli kategorisinde ise yapılması gerekli.
    print("Semptom gelişmezse 7. günde PCR testi yapılması gereklidir.")
elif dusuk_riskli: # Sağlık çalışanı düşük riskli kategorisinde ise yapılması gerekli değil.
    print("Semptom gelişmezse 7. günde PCR testi yapılması gerekli değildir.")


#Sağlık çalışanının o güne kadar çalışıp çalışamama durumu:
if yuksek_riskli: # Yüksek riskli kategorisinde ise çalışamaz.
    print("O güne kadar çalışamaz.")
elif orta_riskli or dusuk_riskli: #Orta veya düşük riskliyse çalışabilir.
    print("O güne kadar çalışabilir.")