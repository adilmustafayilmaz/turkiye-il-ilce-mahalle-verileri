# Turkiye Il Ilce Mahalle Verileri / Turkey Provinces Districts Neighborhoods Data

Turkiye'nin 81 iline ait ilce, mahalle ve koordinat verilerini iceren acik veri seti.

Open dataset containing all provinces, districts, neighborhoods, and coordinates of Turkey.

> 81 il | 973 ilce | 32.186 mahalle
>
> 81 provinces | 973 districts | 32,186 neighborhoods

---

## TR - Turkce

### Veri Icerigi

JSON dosyasi her il icin su bilgileri icerir:

- Plaka kodu
- Koordinatlar (enlem / boylam)
- Ilceler ve bagli mahalleler

### Kullanim Alanlari

- Adres formu ve sehir/ilce/mahalle dropdown secicileri
- Harita uygulamalari ve konum bazli projeler
- Veri analizi ve istatistik calismalari
- Mobil ve web uygulamalarinda adres otomatik tamamlama

### Kurulum

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
pip install requests
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
pip install requests
```

### Calistirma

```bash
python fetch_turkey_data.py
```

Script calistiktan sonra `turkiye_ilce_mahalle.json` dosyasi olusturulur.

Hazir JSON dosyasini dogrudan indirip de kullanabilirsiniz.

---

## EN - English

### Data Content

The JSON file contains the following information for each province:

- License plate code
- Coordinates (latitude / longitude)
- Districts and their neighborhoods

### Use Cases

- Address forms and city/district/neighborhood dropdown selectors
- Map applications and location-based projects
- Data analysis and statistics
- Address autocomplete in mobile and web applications

### Setup

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
pip install requests
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
pip install requests
```

### Usage

```bash
python fetch_turkey_data.py
```

The script generates `turkiye_ilce_mahalle.json` after execution.

You can also download and use the ready-made JSON file directly.

---

## Ornek Cikti / Example Output

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

## Veri Kaynagi / Data Source

[TurkiyeAPI](https://turkiyeapi.dev/)
