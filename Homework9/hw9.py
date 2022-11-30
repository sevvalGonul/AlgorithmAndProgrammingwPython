import string
"""
remove methodu argüman olarak verdiğin elemanı listeden ilk bulduğu yerde temizler! Her yerde temizlemez! O eleman listede
yoksa da exception verir! 

"""




def stop_words_listesi_olustur(stop_words):
    try:
        file = open("stop_words_turkish.txt", "r", encoding="utf8")
        line = file.readline()
        while line != "":
            line = line.rstrip("\n")
            stop_words.append(line)
            line = file.readline()
        file.close()
    except IOError:
        print("Dosya açılamadı ya da okunamadı!")

def noktalama_isaretlerini_temizle(metin):
    noktalama_isaretleri = string.punctuation
    for n in noktalama_isaretleri:
        metin = metin.replace(n, "") # boşluk ile değiştirmelisin, split zaten algılıyor!
    return metin

def stop_words_temizle(metin, stop_words):
    kelime_listesi = metin.split()  # Metni kelimelerine bölüp kelimeleri bir listeye atadım.
    for eleman in kelime_listesi:  # Target variable olan eleman, metindeki kelimeleri tek tek dolaşırken:
        if eleman in stop_words:  # O kelime gereksiz sözcükler(stop words) listesinde var ise:
            kelime_listesi.remove(eleman)  # Kelime listesinden o elemanı çıkardım.

    # Join methoduyla gereksiz kelimelerden arınmış kelime listesini aralarına bir boşluk bırakarak stringe dönüştürdüm.
    yeni_metin = " ".join(kelime_listesi)
    return yeni_metin

def temizlenmis_metni_yazdir(yeni_metin):
    print("Noktalama işaretleri ve gereksiz kelimeler çıkarıldıktan sonra küçük harflerle kalan metin:")
    print(yeni_metin)
    print()

def kelime_tekrar_say_bul_ve_yazdir(kelime_listesi, kelime_tekrar_say):
    for kelime in kelime_listesi:
        kelime_tekrar_say[kelime] = kelime_tekrar_say.get(kelime, 0) + 1

    print("Kalan metindeki kelimeler ve tekrar sayıları:")
    print(format("Kelime", "70"), end=" ")
    print("Tekrar Say")
    print("-" * 70, end=" ")  # Kelimeler in altını çizmek için
    print("-" * 10)  # Tekrar Say ın altını çizmek için

    for kelime in kelime_tekrar_say:  # for key in dictionary:
        print(format(kelime, "70"), end=" ")
        print(format(kelime_tekrar_say[kelime], "7"))
    print()

def uzunluga_gore_tekrar_say_bul_ve_yazdir(kelime_listesi, kelime_uzunluk_tekrar_say):
    for kelime in kelime_listesi:
        if len(kelime) in kelime_uzunluk_tekrar_say:  # if key in dictionary:
            kelime_uzunluk_tekrar_say[len(kelime)] += 1
        else:
            kelime_uzunluk_tekrar_say[len(kelime)] = 1

    print("Kalan metindeki her uzunluktaki kelime sayıları:")
    print("Uzunluk Kelime Say")
    print("------- ----------")
    for uzunluk in sorted(kelime_uzunluk_tekrar_say):
        print(uzunluk, end="\t\t\t")
        print(kelime_uzunluk_tekrar_say[uzunluk])


def main():
    stop_words = []
    stop_words_listesi_olustur(stop_words)
    metin = input("Türkçe bir metin giriniz:\n")
    # "I" lower methodu ile küçük harfe dönüştürülürken "i" olduğu için metindeki "I" ları "ı" larla, "İ" küçük harfe
    # dönüştürülürken iki karakter uzunluğunda i olduğu için onu da "i" ile değiştiriyorum:
    metin = metin.replace("I", "ı").replace("İ", "i")
    metin = metin.lower()  # Metni küçük harflerle yazılmış haline dönüştürdüm.
    noktasiz_metin = noktalama_isaretlerini_temizle(metin)  # Metindeki noktalama işaretlerini temizledim.
    yeni_metin = stop_words_temizle(noktasiz_metin, stop_words)  # Metindeki gereksiz sözcükleri temizledim.
    temizlenmis_metni_yazdir(yeni_metin)

    kelime_listesi = yeni_metin.split()  # split methoduyla metnin son halindeki kelimeleri içeren bir liste oluşturdum.
    kelime_tekrar_say = {}  # Anahtarları metindeki kelimeler, değerleri o kelimelerin tekrar sayıları olan sözlük
    kelime_tekrar_say_bul_ve_yazdir(kelime_listesi, kelime_tekrar_say)

    kelime_uzunluk_tekrar_say = {}  # Anahtarları metindeki kelimelerin uzunlukları, değerleri tekrar sayıları olan sözlük
    uzunluga_gore_tekrar_say_bul_ve_yazdir(kelime_listesi, kelime_uzunluk_tekrar_say)

main()