#Muhammed Beşir ASLAN - 030121038 

komşular = {
    'Afyonkarahisar': ['Isparta', 'Konya', 'Eskisehir', 'Kutahya', 'Usak', 'Denizli', 'Burdur'],
    'Aksaray': ['Nigde', 'Nevsehir', 'Kirikkale', 'Ankara', 'Konya'],
    'Ankara': ['Konya', 'Aksaray', 'Kirsehir', 'Kirikkale', 'Cankiri', 'Bolu', 'Eskisehir', 'Afyon'],
    'Antalya': ['Mersin', 'Karaman', 'Konya', 'Isparta', 'Burdur', 'Mugla'],
    'Aydin': ['Mugla', 'Denizli', 'Manisa', 'Izmir'],
    'Balikesir': ['Izmir', 'Manisa', 'Kutahya', 'Bursa', 'Canakkale'],
    'Bartın': ['Kastamonu', 'Zonguldak', 'Karabuk'],
    'Bilecik': ['Kutahya', 'Eskisehir', 'Bolu', 'Sakarya', 'Bursa'],
    'Bolu': ['Eskisehir', 'Ankara', 'Cankiri', 'Zonguldak', 'Duzce', 'Sakarya', 'Bilecik'],
    'Burdur': ['Mugla', 'Antalya', 'Isparta', 'Afyon', 'Denizli'],
    'Bursa': ['Balikesir', 'Kutahya', 'Bilecik', 'Sakarya', 'Kocaeli', 'Yalova'],
    'Canakkale': ['Balikesir', 'Tekirdag', 'Edirne'],
    'Cankiri': ['Ankara', 'Kirikkale', 'Corum', 'Kastamonu', 'Zonguldak', 'Bolu', 'Karabuk'],
    'Corum': ['Yozgat', 'Amasya', 'Samsun', 'Sinop', 'Kastamonu', 'Cankiri', 'Kirikkale'],
    'Denizli': ['Mugla', 'Burdur', 'Afyon', 'Usak', 'Manisa', 'Aydin'],
    'Düzce': ['Zonguldak', 'Bolu', 'Sakarya'],
    'Edirne': ['Canakkale', 'Tekirdag', 'Kirikkale'],
    'Eskisehir': ['Afyon', 'Konya', 'Ankara', 'Bolu', 'Bilecik', 'Kutahya'],
    'Isparta': ['Antalya', 'Konya', 'Afyon', 'Burdur'],
    'Istanbul': ['Kocaeli', 'Tekirdag', 'Kirklareli'],
    'Izmir': ['Aydin', 'Manisa', 'Balikesir'],
    'Karabuk': ['Zonguldak', 'Bartin', 'Cankiri'],
    'Karaman': ['Mersin', 'Konya', 'Antalya'],
    'Kars': ['Agri', 'Igdir', 'Ardahan', 'Erzurum'],
    'Kastamonu': ['Corum', 'Sinop', 'Cankiri', 'Bartin', 'Karabuk'],
    'Kırıkkale': ['Kirsehir', 'Yozgat', 'Corum', 'Cankiri', 'Ankara'],
    'Kırklareli': ['Edirne', 'Tekirdag', 'Istanbul'],
    'Kırşehir': ['Nevsehir', 'Aksaray', 'Kirikkale'],
    'Kocaeli': ['Yalova', 'Istanbul', 'Bursa', 'Bilecik', 'Sakarya'],
    'Konya': ['Antalya', 'Karaman', 'Mersin', 'Nigde', 'Aksaray', 'Ankara', 'Eskisehir', 'Afyon', 'Isparta'],
    'Kütahya': ['Manisa', 'Usak', 'Afyon', 'Eskisehir', 'Bilecik', 'Bursa', 'Balikesir'],
    'Manisa': ['Izmir', 'Aydin', 'Denizli', 'Usak', 'Kutahya', 'Balikesir'],
    'Mersin': ['Adana', 'Nigde', 'Konya', 'Karaman', 'Antalya'],
    'Muğla': ['Antalya', 'Burdur', 'Denizli', 'Aydin'],
    'Nevşehir': ['Nigde', 'Kayseri', 'Yozgat', 'Kirsehir', 'Aksaray'],
    'Niğde': ['Nevsehir', 'Kayseri', 'Adana', 'Mersin', 'Konya', 'Aksaray'],
    'Ordu': ['Samsun', 'Giresun', 'Sivas', 'Tokat'],
    'Sakarya': ['Duzce', 'Bolu', 'Bilecik', 'Bursa', 'Kocaeli'],
    'Sinop': ['Samsun', 'Corum', 'Kastamonu'],
    'Tekirdağ': ['Istanbul', 'Kirklareli', 'Edirne', 'Canakkale'],
    'Uşak': ['Manisa', 'Denizli', 'Afyon', 'Kutahya'],
    'Yalova': ['Kocaeli', 'Bursa'],
    'Zonguldak': ['Bartin', 'Cankiri', 'Bolu', 'Duzce', 'Karabuk']

}
    

    
    
def uygun_renkleme(node, renk, renklendirme):
    for komsu in komşular[node]:
        if komsu in renklendirme and renklendirme[komsu] == renk:
            return False
    return True

def harita_renkleme(nodlar, renkler, renklendirme):
    if not nodlar:
        return True

    node = nodlar[0]
    for renk in renkler:
        if uygun_renkleme(node, renk, renklendirme):
            renklendirme[node] = renk
            if harita_renkleme(nodlar[1:], renkler, renklendirme):
                return True
            renklendirme[node] = None

    return False

def turkiye_harita_renkleme():
    nodlar = list(komşular.keys())
    renkler_3 = ["Kırmızı", "Yeşil", "Mavi"]
    renkler_4 = ["Kırmızı", "Yeşil", "Mavi", "Sarı"]

    renklendirme = {node: None for node in nodlar}

    if harita_renkleme(nodlar, renkler_3, renklendirme):
        print("Harita 3 renkle boyanabilir:")
        print(renklendirme)
    else:
        print("Harita 3 renkle boyanamaz.")

    renklendirme = {node: None for node in nodlar}

    if harita_renkleme(nodlar, renkler_4, renklendirme):
        print("\nHarita 4 renkle boyanabilir:")
        print(renklendirme)
    else:
        print("\nHarita 4 renkle boyanamaz.")

if __name__ == "__main__":
    turkiye_harita_renkleme()


'''
Diğer iller eklenirse kod derlenmiyor çünkü çok fazla veri var. Aşağıdaki veriler 81 ilin tamamıdır 

 'Adana': ['Hatay', 'Osmaniye', 'Kahramanmaras', 'Kayseri', 'Nigde', 'Mersin'],
    'Adiyaman': ['Sanliurfa', 'Diyarbakir', 'Malatya', 'Kahramanmaras', 'Gaziantep'],
    'Afyon': ['Isparta', 'Konya', 'Eskisehir', 'Kutahya', 'Usak', 'Denizli', 'Burdur'],
    'Agri': ['Van', 'Igdir', 'Kars', 'Erzurum', 'Mus', 'Bitlis'],
    'Amasya': ['Yozgat', 'Tokat', 'Samsun', 'Corum'],
    'Ankara': ['Konya', 'Aksaray', 'Kirsehir', 'Kirikkale', 'Cankiri', 'Bolu', 'Eskisehir', 'Afyon'],
    'Antalya': ['Mersin', 'Karaman', 'Konya', 'Isparta', 'Burdur', 'Mugla'],
    'Artvin': ['Rize', 'Erzurum', 'Ardahan'],
    'Aydin': ['Mugla', 'Denizli', 'Manisa', 'Izmir'],
    'Balikesir': ['Izmir', 'Manisa', 'Kutahya', 'Bursa', 'Canakkale'],
    'Bilecik': ['Kutahya', 'Eskisehir', 'Bolu', 'Sakarya', 'Bursa'],
    'Bingol': ['Diyarbakir', 'Mus', 'Erzurum', 'Erzincan', 'Tunceli', 'Elazig'],
    'Bitlis': ['Siirt', 'Van', 'Agri', 'Mus', 'Batman'],
    'Bolu': ['Eskisehir', 'Ankara', 'Cankiri', 'Zonguldak', 'Duzce', 'Sakarya', 'Bilecik'],
    'Burdur': ['Mugla', 'Antalya', 'Isparta', 'Afyon', 'Denizli'],
    'Bursa': ['Balikesir', 'Kutahya', 'Bilecik', 'Sakarya', 'Kocaeli', 'Yalova'],
    'Canakkale': ['Balikesir', 'Tekirdag', 'Edirne'],
    'Cankiri': ['Ankara', 'Kirikkale', 'Corum', 'Kastamonu', 'Zonguldak', 'Bolu', 'Karabuk'],
    'Corum': ['Yozgat', 'Amasya', 'Samsun', 'Sinop', 'Kastamonu', 'Cankiri', 'Kirikkale'],
    'Denizli': ['Mugla', 'Burdur', 'Afyon', 'Usak', 'Manisa', 'Aydin'],
    'Diyarbakir': ['Sanliurfa', 'Mardin', 'Batman', 'Mus', 'Bingol', 'Elazig', 'Malatya', 'Adiyaman'],
    'Edirne': ['Canakkale', 'Tekirdag', 'Kirikkale'],
    'Elazig': ['Diyarbakir', 'Bingol', 'Tunceli', 'Erzincan', 'Malatya'],
    'Erzincan': ['Elazig', 'Tunceli', 'Bingol', 'Erzurum', 'Bayburt', 'Gumushane', 'Giresun', 'Sivas', 'Malatya'],
    'Erzurum': ['Bingol', 'Mus', 'Agri', 'Kars', 'Ardahan', 'Artvin', 'Rize', 'Trabzon', 'Bayburt', 'Erzincan'],
    'Eskisehir': ['Afyon', 'Konya', 'Ankara', 'Bolu', 'Bilecik', 'Kutahya'],
    'Gaziantep': ['Kilis', 'Sanliurfa', 'Adiyaman', 'Kahramanmaras', 'Osmaniye', 'Hatay'],
    'Giresun': ['Gumushane', 'Erzincan', 'Bayburt', 'Trabzon'],
    'Gumushane': ['Erzincan', 'Bayburt', 'Trabzon', 'Giresun'],
    'Hakkari': ['Van', 'Sirnak'],
    'Hatay': ['Kilis', 'Gaziantep', 'Osmaniye', 'Adana'],
    'Isparta': ['Antalya', 'Konya', 'Afyon', 'Burdur'],
    'Mersin': ['Adana', 'Nigde', 'Konya', 'Karaman', 'Antalya'],
    'Istanbul': ['Kocaeli', 'Tekirdag', 'Kirklareli'],
    'Izmir': ['Aydin', 'Manisa', 'Balikesir'],
    'Kars': ['Agri', 'Igdir', 'Ardahan', 'Erzurum'],
    'Kastamonu': ['Corum', 'Sinop', 'Cankiri', 'Bartin', 'Karabuk'],
    'Kayseri': ['Adana', 'Kahramanmaras', 'Sivas', 'Yozgat', 'Nevsehir', 'Nigde'],
    'Kirklareli': ['Edirne', 'Tekirdag', 'Istanbul'],
    'Kirsehir': ['Nevsehir', 'Yozgat', 'Kirikkale', 'Ankara', 'Aksaray'],
    'Kocaeli': ['Yalova', 'Istanbul', 'Bursa', 'Bilecik', 'Sakarya'],
    'Konya': ['Antalya', 'Karaman', 'Mersin', 'Nigde', 'Aksaray', 'Ankara', 'Eskisehir', 'Afyon', 'Isparta'],
    'Kutahya': ['Manisa', 'Usak', 'Afyon', 'Eskisehir', 'Bilecik', 'Bursa', 'Balikesir'],
    'Malatya': ['Kahramanmaras', 'Adiyaman', 'Diyarbakir', 'Elazig', 'Erzincan', 'Sivas'],
    'Manisa': ['Izmir', 'Aydin', 'Denizli', 'Usak', 'Kutahya', 'Balikesir'],
    'Kahramanmaras': ['Gaziantep', 'Adiyaman', 'Malatya', 'Sivas', 'Kayseri', 'Adana', 'Osmaniye'],
    'Mardin': ['Sanliurfa', 'Diyarbakir', 'Batman', 'Siirt', 'Sirnak'],
    'Mugla': ['Antalya', 'Burdur', 'Denizli', 'Aydin'],
    'Mus': ['Diyarbakir', 'Batman', 'Bitlis', 'Agri', 'Erzurum', 'Bingol'],
    'Nevsehir': ['Nigde', 'Kayseri', 'Yozgat', 'Kirsehir', 'Aksaray'],
    'Nigde': ['Nevsehir', 'Kayseri', 'Adana', 'Mersin', 'Konya', 'Aksaray'],
    'Rize': ['Artvin', 'Erzurum', 'Bayburt', 'Trabzon'],
    'Sakarya': ['Duzce', 'Bolu', 'Bilecik', 'Bursa', 'Kocaeli'],
    'Samsun': ['Ordu', 'Tokat', 'Amasya', 'Corum', 'Sinop'],
    'Siirt': ['Van', 'Bitlis', 'Batman', 'Mardin', 'Sirnak'],
    'Sinop': ['Samsun', 'Corum', 'Kastamonu'],
    'Sivas': ['Kayseri', 'Kahramanmaras', 'Malatya', 'Erzincan', 'Giresun', 'Ordu', 'Tokat', 'Yozgat'],
    'Tekirdag': ['Istanbul', 'Kirklareli', 'Edirne', 'Canakkale'],
    'Tokat': ['Sivas', 'Ordu', 'Samsun', 'Amasya', 'Yozgat'],
    'Trabzon': ['Rize', 'Bayburt', 'Gumushane', 'Giresun'],
    'Tunceli': ['Elazig', 'Bingol', 'Erzincan'],
    'Sanliurfa': ['Gaziantep', 'Adiyaman', 'Diyarbakir', 'Mardin'],
    'Usak': ['Manisa', 'Denizli', 'Afyon', 'Kutahya'],
    'Van': ['Hakkari', 'Sirnak', 'Siirt', 'Bitlis', 'Agri'],
    'Yozgat': ['Kayseri', 'Sivas', 'Tokat', 'Amasya', 'Corum', 'Kirikkale', 'Kirsehir', 'Nevsehir'],
    'Zonguldak': ['Bartin', 'Cankiri', 'Bolu', 'Duzce', 'Karabuk'],
    'Aksaray': ['Nigde', 'Nevsehir', 'Kirsehir', 'Ankara', 'Konya'],
    'Bayburt': ['Erzincan', 'Erzurum', 'Rize', 'Trabzon', 'Gumushane'],
    'Karaman': ['Mersin', 'Konya', 'Antalya'],
    'Kirikkale': ['Kirsehir', 'Yozgat', 'Corum', 'Cankiri', 'Ankara'],
    'Batman': ['Mardin', 'Siirt', 'Bitlis', 'Mus', 'Diyarbakir'],
    'Sirnak': ['Mardin', 'Siirt', 'Van', 'Hakkari'],
    'Bartin': ['Kastamonu', 'Zonguldak', 'Karabuk'],
    'Ardahan': ['Kars', 'Erzurum', 'Artvin'],
    'Igdir': ['Agri', 'Kars'],
    'Yalova': ['Kocaeli', 'Bursa']
    
}


   



'''

'''
Adana: Hatay,Osmaniye,Kahramanmaras,Kayseri,Nigde,Mersin
Adiyaman: Sanliurfa,Diyarbakir,Malatya,Kahramanmaras,Gaziantep
Afyon: Isparta,Konya,Eskisehir,Kutahya,Usak,Denizli,Burdur
Agri: Van,Igdir,Kars,Erzurum,Mus,Bitlis
Amasya: Yozgat,Tokat,Samsin,Corum
Ankara: Konya,Aksaray,Kirsehir,Kirikkale,Cankiri,Bolu,Eskisehir,Afyon
Antalya: Mersin,Karaman,Konya,Isparta,Burdur,Mugla
Artvin: Rize,Erzurum,Ardahan
Aydin: Mugla,Denizli,Manisa,Izmir
Balikesir: Izmir,Manisa,Kutahya,Bursa,Canakkale
Bilecik: Kutahya,Eskisehir,Bolu,Sakarya,Bursa
Bingol: Diyarbakir,Mus,Erzurum,Erzincan,Tunceli,Elazig
Bitlis: Siirt,Van,Agri,Mus,Batman
Bolu: Eskisehir,Ankara,Cankiri,Zonguldak,Duzce,Sakarya,Bilecik
Burdur: Mugla,Antalya,Isparta,Afyon,Denizli
Bursa: Balikesir,Kutahya,Bilecik,Sakarya,Kocaeli,Yalova
Canakkale: Balikesir,Tekirdag,Edirne
Cankiri: Ankara,Kirikkale,Corum,Kastamonu,Zonguldak,Bolu,Karabuk
Corum: Yozgat,Amasya,Samsun,Sinop,Kastamonu,Cankiri,Kirikkale
Denizli: Mugla,Burdur,Afyon,Usak,Manisa,Aydin
Diyarbakir: Sanliurfa,Mardin,Batman,Mus,Bingol,Elazig,Malatya,Adiyaman
Edirne: Canakkale,Tekirdag,Kirikkale
Elazig: Diyarbakir,Bingol,Tunceli,Erzincan,Malatya
Erzincan: Elazig,Tunceli,Bingol,Erzurum,Bayburt,Gumushane,Giresun,Sivas,Malatya
Erzurum: Bingol,Mus,Agri,Kars,Ardahan,Artvin,Rize,Trabzon,Bayburt,Erzincan
Eskisehir: Afyon,Konya,Ankara,Bolu,Bilecik,Kutahya
Gaziantep: Kilis,Sanliurfa,Adiyaman,Kahramanmaras,Osmaniye,Hatay
Giresun: Gumushane,Erzincan,Bayburt,Trabzon
Gumushane: Erzincan,Bayburt,Trabzon,Giresun
Hakkari: Van,Sirnak
Hatay: Kilis,Gaziantep,Osmaniye,Adana
Isparta: Antalya,Konya,Afyon,Burdur
Mersin: Adana,Nigde,Konya,Karaman,Antalya
Istanbul: Kocaeli,Tekirdag,Kirklareli
Izmir: Aydin,Manisa,Balikesir
Kars: Agri,Igdir,Ardahan,Erzurum
Kastamonu: Corum,Sinop,Cankiri,Bartin,Karabuk
Kayseri: Adana,Kahramanmaras,Sivas,Yozgat,Nevsehir,Nigde
Kirklareli: Edirne,Tekirdag,Istanbul
Kirsehir: Nevsehir,Yozgat,Kirikkale,Ankara,Aksaray
Kocaeli: Yalova,Istanbul,Bursa,Bilecik,Sakarya
Konya: Antalya,Karaman,Mersin,Nigde,Aksaray,Ankara,Eskisehir,Afyon,Isparta
Kutahya: Manisa,Usak,Afyon,Eskisehir,Bilecik,Bursa,Balikesir
Malatya: Kahramanmaras,Adiyaman,Diyarbakir,Elazig,Erzincan,Sivas
Manisa: Izmir,Aydin,Denizli,Usak,Kutahya,Balikesir
Kahramanmaras: Gaziantep,Adiyaman,Malatya,Sivas,Kayseri,Adana,Osmaniye
Mardin: Sanliurfa,Diyarbakir,Batman,Siirt,Sirnak
Mugla: Antalya,Burdur,Denizli,Aydin
Mus: Diyarbakir,Batman,Bitlis,Agri,Erzurum,Bingol
Nevsehir: Nigde,Kayseri,Yozgat,Kirsehir,Aksaray
Nigde: Nevsehir,Kayseri,Adana,Mersin,Konya,Aksaray
Rize: Artvin,Erzurum,Bayburt,Trabzon
Sakarya: Duzce,Bolu,Bilecik,Bursa,Kocaeli
Samsun: Ordu,Tokat,Amasya,Corum,Sinop
Siirt: Van,Bitlis,Batman,Mardin,Sirnak
Sinop: Samsun,Corum,Kastamonu
Sivas: Kayseri,Kahramanmaras,Malatya,Erzincan,Giresun,Ordu,Tokat,Yozgat
Tekirdag: Istanbul,Kirklareli,Edirne,Canakkale
Tokat: Sivas,Ordu,Samsun,Amasya,Yozgat
Trabzon: Rize,Bayburt,Gumushane,Giresun
Tunceli: Elazig,Bingol,Erzincan
Sanliurfa: Gaziantep,Adiyaman,Diyarbakir,Mardin
Usak: Manisa,Denizli,Afyon,Kutahya
Van: Hakkari,Siranak,Siirt,Bitlis,Agri
Yozgat: Kayseri,Sivas,Tokat,Amasya,Corum,Kirikkale,Kirsehir,Nevsehir
Zonguldak: Bartin,Cankiri,Bolu,Duzce,Karabuk
Aksaray: Nigde,Nevsehir,Kirsehir,Ankara,Konya
Bayburt: Erzincan,Erzurum,Rize,Trabzon, Gumushane
Karaman: Mersin,Konya,Antalya
Kirikkale: Kirsehir,Yozgat,Corum,Cankiri,Ankara
Batman: Mardin,Siirt,Bitlis,Mus,Diyarbakir
Sirnak: Mardin,Siirt,Van,Hakkari
Bartin: Kastamonu,Zonguldak,Karabuk
Ardahan: Kars,Erzurum,Artvin
Igdir: Agri,Kars
Yalova: Kocaeli,Bursa
Karabuk: Zonguldak,Bartin,Kastamonu,Cankiri
Kilis: Gaziantep,Hatay
Osmaniye: Gaziantep,Kahramanmaras,Adana,Hatay
Duzce: Zonguldak,Bolu,Sakarya
'''

