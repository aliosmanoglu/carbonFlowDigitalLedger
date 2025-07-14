import random
import datetime
import json



LOCATIONS = [
    "Düzce Merkez - Şehir Parkı",
    "Düzce - Avni Akyol Parkı",
    "Düzce - Bisiklet Yolu 1",
    "Düzce - Kent Ormanı",
    "Düzce - Melen Botanik Parkı",
    "Düzce - Yeşil Vadi Yürüyüş Alanı",
    "İstanbul - Yogurtcu Parkı",
    "İstanbul - Ortaköy",
    "İstanbul - Gülhane Parkı",
]


DATA = []

def generate_random_timestamp(days_back=30):
    #DAYS BACK KAC GUN ICINDE RASTGELE URETILECEGINI BELIRLER
    
    now = datetime.datetime.now()
    random_days = random.randint(0, days_back)
    random_seconds = random.randint(0, 86400)  # Gün içi rastgele saat
    random_time = now - datetime.timedelta(days=random_days, seconds=random_seconds)
    return random_time.isoformat()


def generate_fake_data():

    #SENTETIK DATA OLUSTURUR
    return {
        "timestamp": generate_random_timestamp(),
        "location": random.choice(LOCATIONS),
        "temperature": round(random.uniform(18, 32), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "light": round(random.uniform(100, 1000), 2),
        "co2_ppm": random.randint(350, 800)
    }


for _ in range(50):
    DATA.append(generate_fake_data)



with open("sensor_data.json", "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=4, ensure_ascii=False)