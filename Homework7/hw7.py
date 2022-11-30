def il_mv_say_bul(mv_kont, parti_oy_listesi, il_mv_say_list):
    for sayac in range(mv_kont):
        max_oy = max(parti_oy_listesi)
        max_oy_index = parti_oy_listesi.index(max_oy)
        il_mv_say_list[max_oy_index] += 1
        parti_oy_listesi[max_oy_index] //= 2

def il_ciktilari_yaz(plaka_kodu, mv_kont, gecerli_oy_say, parti_oy_listesi, il_mv_say_list):
    print("Il Plaka Kodu:", plaka_kodu)
    print("Milletvekili Kontenjani:", mv_kont)
    print("Gecerli Oy Sayisi:", gecerli_oy_say)
    print("Pusula Sira   Oy Say   Oy Yuzde   MV Say")
    print("-----------   ------   --------   ------")
    for sayac in range(len(parti_oy_listesi)):  # for sayac in range(parti_say)
        print(format(sayac+1, "11d"), end="   ")
        print(format(parti_oy_listesi[sayac], "6d"), end="   ")
        print(format(parti_oy_listesi[sayac]*100/gecerli_oy_say, "8.2f"), end="   ")
        print(format(il_mv_say_list[sayac], "6d"))

def genel_ciktilari_yaz(top_mv_kontenjani, top_gecerli_oy, top_parti_oylari_listesi, sifir_mv_il_say_list, top_mv_say):
    print("Türkiye Geneli")
    print("Milletvekili Kontenjani:", top_mv_kontenjani)
    print("Gecerli Oy Sayisi:", top_gecerli_oy)
    print("Pusula Sira   Oy Say   Oy Yuzde   MV Say   MV Yuzde   0 MV Il Say")
    print("-----------   ------   --------   ------   --------   -----------")
    for sayac in range(len(top_parti_oylari_listesi)):
        print(format(sayac+1, "11d"), end="   ")
        print(format(top_parti_oylari_listesi[sayac], "6d"), end="   ")
        print(format(top_parti_oylari_listesi[sayac]*100/top_gecerli_oy, "8.2f"), end="   ")
        print(format(top_mv_say[sayac], "6d"), end="   ")
        print(format(top_mv_say[sayac]*100/top_mv_kontenjani, "8.2f"), end="   ")
        print(format(sifir_mv_il_say_list[sayac], "11d"))

def main():
    try:
        secim_dos = open("secim.txt", "r")
        parti_say = int(secim_dos.readline())
        mv_kontenjani_listesi = []  # Her ilin milletvekili kontenjanını bu listenin sonuna ekleyeceğim.
        parti_oy_listesi = [0] * parti_say  # Bir ilin partilere verdiği oyları tutacak olan liste

        sifir_mv_il_say_list = [0] * parti_say  # Partilerin hiç mv çıkaramadıkları il sayısını saydırma listesi
        top_mv_say = [0] * parti_say  # Partilerin çıkarmış oldukları toplam milletvekili sayılarını tutacak liste
        top_parti_oylari_listesi = [0] * parti_say  # Her partinin aldığı toplam oyları tutacak olan liste
        top_gecerli_oy = 0

        plaka_kodu = secim_dos.readline()
        while plaka_kodu != "":
            mv_kont = int(secim_dos.readline())
            mv_kontenjani_listesi.append(mv_kont)
            il_mv_say_list = [0] * parti_say  # Bir ilde çıkarılan milletvekili sayılarının partilere göre dağılımını tutan liste

            for i in range(parti_say):
                parti_oy_listesi[i] = int(secim_dos.readline())
                top_parti_oylari_listesi[i] += parti_oy_listesi[i]

            il_gecerli_oy = sum(parti_oy_listesi)
            top_gecerli_oy += il_gecerli_oy

            # il_mv_say_bul fonksiyonu parti_oy_listesini değiştireceği için onun bir kopyasını oluşturdum.
            parti_oy_listesi_copy = [] + parti_oy_listesi

            # Verisi işlenen ilin mv kontenjanını partilere dağıtıyorum.
            il_mv_say_bul(mv_kont, parti_oy_listesi, il_mv_say_list)
            # O il ile ilgili çıktıları yazdırıyorum.
            il_ciktilari_yaz(plaka_kodu, mv_kont, il_gecerli_oy, parti_oy_listesi_copy,il_mv_say_list)

            for ind in range(parti_say):
                top_mv_say[ind] += il_mv_say_list[ind]
                if il_mv_say_list[ind] == 0: # ise o ilde (ind+1). parti hiç mv çıkaramamıştır.
                    sifir_mv_il_say_list[ind] += 1

            plaka_kodu = secim_dos.readline()

        genel_top_mv_say = sum(mv_kontenjani_listesi)
        genel_ciktilari_yaz(genel_top_mv_say, top_gecerli_oy, top_parti_oylari_listesi, sifir_mv_il_say_list, top_mv_say)

    except IOError:
        print("Veri dosyası açılamadı ya da okunamadı!")

    except Exception as err:
        print(err)

main()