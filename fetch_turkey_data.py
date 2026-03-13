import requests
import json
import time

BASE_URL = "https://api.turkiyeapi.dev/api/v1"

# 81 il - plaka kodu ve isim
ILLER = {
    1: "ADANA", 2: "ADIYAMAN", 3: "AFYONKARAHİSAR", 4: "AĞRI", 5: "AMASYA",
    6: "ANKARA", 7: "ANTALYA", 8: "ARTVİN", 9: "AYDIN", 10: "BALIKESİR",
    11: "BİLECİK", 12: "BİNGÖL", 13: "BİTLİS", 14: "BOLU", 15: "BURDUR",
    16: "BURSA", 17: "ÇANAKKALE", 18: "ÇANKIRI", 19: "ÇORUM", 20: "DENİZLİ",
    21: "DİYARBAKIR", 22: "EDİRNE", 23: "ELAZIĞ", 24: "ERZİNCAN", 25: "ERZURUM",
    26: "ESKİŞEHİR", 27: "GAZİANTEP", 28: "GİRESUN", 29: "GÜMÜŞHANE", 30: "HAKKARİ",
    31: "HATAY", 32: "ISPARTA", 33: "MERSİN", 34: "İSTANBUL", 35: "İZMİR",
    36: "KARS", 37: "KASTAMONU", 38: "KAYSERİ", 39: "KIRKLARELİ", 40: "KIRŞEHİR",
    41: "KOCAELİ", 42: "KONYA", 43: "KÜTAHYA", 44: "MALATYA", 45: "MANİSA",
    46: "KAHRAMANMARAŞ", 47: "MARDİN", 48: "MUĞLA", 49: "MUŞ", 50: "NEVŞEHİR",
    51: "NİĞDE", 52: "ORDU", 53: "RİZE", 54: "SAKARYA", 55: "SAMSUN",
    56: "SİİRT", 57: "SİNOP", 58: "SİVAS", 59: "TEKİRDAĞ", 60: "TOKAT",
    61: "TRABZON", 62: "TUNCELİ", 63: "ŞANLIURFA", 64: "UŞAK", 65: "VAN",
    66: "YOZGAT", 67: "ZONGULDAK", 68: "AKSARAY", 69: "BAYBURT", 70: "KARAMAN",
    71: "KIRIKKALE", 72: "BATMAN", 73: "ŞIRNAK", 74: "BARTIN", 75: "ARDAHAN",
    76: "IĞDIR", 77: "YALOVA", 78: "KARABÜK", 79: "KİLİS", 80: "OSMANİYE",
    81: "DÜZCE",
}


def fetch_province(province_id):
    """Bir ilin genel bilgilerini (koordinat dahil) çeker."""
    url = f"{BASE_URL}/provinces/{province_id}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_districts(province_id):
    """Bir ilin ilçe ve mahalle verilerini çeker."""
    url = f"{BASE_URL}/districts?provinceId={province_id}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.json()


def main():
    result = {}

    for plaka, il_adi in ILLER.items():
        print(f"[{plaka}/81] {il_adi} verisi çekiliyor...")
        try:
            # İl koordinatlarını çek
            province_data = fetch_province(plaka)
            coords = province_data.get("data", {}).get("coordinates", {})

            # İlçe ve mahalle verilerini çek
            data = fetch_districts(plaka)
            districts = data.get("data", [])

            ilceler = {}
            for d in districts:
                mahalleler = [n["name"] for n in d.get("neighborhoods", [])]
                ilceler[d["name"]] = mahalleler

            result[il_adi] = {
                "plaka": plaka,
                "koordinatlar": {
                    "latitude": coords.get("latitude"),
                    "longitude": coords.get("longitude"),
                },
                "ilceler": ilceler,
            }
        except Exception as e:
            print(f"  HATA: {il_adi} - {e}")
            result[il_adi] = {"plaka": plaka, "koordinatlar": {}, "ilceler": {}, "hata": str(e)}

        time.sleep(0.5)  # API'ye nazik olmak için

    output_path = "turkiye_ilce_mahalle.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # Özet istatistik
    toplam_ilce = sum(len(v["ilceler"]) for v in result.values())
    toplam_mahalle = sum(
        len(m) for v in result.values() for m in v["ilceler"].values()
    )
    print(f"\nTamamlandı! {output_path} dosyasına kaydedildi.")
    print(f"Toplam: 81 il, {toplam_ilce} ilçe, {toplam_mahalle} mahalle")


if __name__ == "__main__":
    main()
