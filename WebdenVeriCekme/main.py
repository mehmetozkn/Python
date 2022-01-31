import requests
from bs4 import BeautifulSoup
import operator


def sozlukOlustur(tumKelimeler):
    kelimeSayisi = {}

    for kelime in tumKelimeler:
        if kelime in kelimeSayisi:
            kelimeSayisi[kelime] += 1
        else:
            kelimeSayisi[kelime] = 1

    return kelimeSayisi

def sembolleriTemizle(tumKelimeler):
    sembolsuzKelimeler = []
    semboller = "!@$#^*()_+{}'\'<>_,-." + chr(775)
    for kelime in tumKelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")
        if(len(kelime) > 0):
            sembolsuzKelimeler.append(kelime)


    return sembolsuzKelimeler


url = "https://www.ntv.com.tr/galeri/saglik/9-yasindaki-veyselin-erken-yaslanma-hastaligi-ile-mucadelesi,SM0APDFywUmJBI3_GLNc9A"

tumKelimeler = []
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for kelimeGruplari in soup.find_all("p"):
    icerik = kelimeGruplari.text
    kelimeler = icerik.lower().split()


    for kelime in kelimeler:
        tumKelimeler.append(kelime)
        
tumKelimeler = sembolleriTemizle(tumKelimeler)

kelimeSayi = sozlukOlustur(tumKelimeler)

for anahtar,deger in sorted(kelimeSayi.items(), key = operator.itemgetter(0)):
    #0 alfabeye göre sıralar 1 sayıya göre
    print(anahtar,deger)
