import re
from collections import Counter

def log_analiz(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as f:
        loglar = f.readlines()

    hatalar = [satir for satir in loglar if "ERROR" in satir]
    ip_adresleri = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ''.join(loglar))
    en_cok_ip = Counter(ip_adresleri).most_common(3)
    
    print(f"Toplam Satır: {len(loglar)}")
    print(f"Toplam Hata: {len(hatalar)}")
    print(f"En Çok Görülen 3 IP: {en_cok_ip}")

if __name__ == "__main__":
    dosya = input("Log dosyasının yolu: ")
    log_analiz(dosya)
