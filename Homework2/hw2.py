SINIR_YAKLASMA_MESAFESI = 100
SINIR_BULUNMA_SURESI = 15
# Maskesiz biçimde yaklasılan mesafe 1 metreden az ve bulunulan süre 15dk veya daha fazla ise kişi yakın temaslı grubunda sayılacaktır.

ad_soyad = input("Adınızı-soyadınızı giriniz: ")
maske_takiyor_mu = input("COVID-19 (+) kişi ile temas ettiğiniz sırada maske takıp takmadığınızı giriniz (e/h): ")

if maske_takiyor_mu == "h":
    yaklasilan_mesafe = float(input("Bu kişiye ne kadar mesafe yaklaştığınızı giriniz (cm): "))
    bulunulan_sure = float(input("Bu mesafede bulunduğunuz süreyi giriniz (dk): "))

agir_kronik_var_mi = input("Ağır kronik bir hastalığınız olup olmadığını giriniz (e/h): ")

print("Sayın", ad_soyad + ",")
if maske_takiyor_mu == "h" and yaklasilan_mesafe < SINIR_YAKLASMA_MESAFESI and bulunulan_sure >= SINIR_BULUNMA_SURESI: #short-circuit evaluation
    print("Yakın temaslı grubundasınız.")
    yakin_temasli = True
else:
    print("Temaslı grubundasınız.")
    yakin_temasli = False

# Kişide ağır kronik hastalık varsa veya yakın temaslı grubundaysa ilaç tedavisi almalıdır.
if agir_kronik_var_mi == "e" or yakin_temasli:
    print("İlaç tedavisi almanıza gerek vardır.")
else:
    print("İlaç tedavisi almanıza gerek yoktur.")



