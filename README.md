# Turkiye Ilce Mahalle Verisi

Turkiye'nin 81 iline ait ilce ve mahalle verilerini [TurkiyeAPI](https://turkiyeapi.dev/) uzerinden cekerek JSON formatinda kaydeden Python scripti.

## Veri Icerigi

Uretilen JSON dosyasi her il icin su bilgileri icerir:

- Plaka kodu
- Koordinatlar (enlem/boylam)
- Ilceler ve bagli mahalleler

## Kurulum

```bash
python -m venv venv
source venv/bin/activate
pip install requests
```

## Kullanim

```bash
python fetch_turkey_data.py
```

Script calistiktan sonra `turkiye_ilce_mahalle.json` dosyasi olusturulur.

## Ornek Cikti

```json
{
  "ANKARA": {
    "plaka": 6,
    "koordinatlar": {
      "latitude": 39.925533,
      "longitude": 32.866287
    },
    "ilceler": {
      "AKYURT": ["BALCI MAH", "CUBUKKOY MAH", "..."],
      "ALTINDAG": ["AKARBAŞI MAH", "..."]
    }
  }
}
```
