#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Hattı
Müşteri hizmetleri asla cevap vermez. Ama mesajları efsane.
"""

import random
import time
import sys

# Gizli not: bazen sistemler de bekler, ama kimse fark etmez.
GIZLI_MESAJ = "dGVudGl2b3J5IG1pIGdlbGRpcmkgZ2VsZGlkaQ=="  # Base64, çözmeyi dene istersen

MESAJLAR = [
    "Çağrınız önemli, çok önemli. Şu anda 1.847.293 kişi önünüzde sırada. Kahve içmeye gidiyoruz.",
    "Lütfen bekleyin, operatörümüz şu anda evrenin en derin düşüncelerini düşünüyor.",
    "Sıranız geldi! ... Şaka şaka, daha 47 yıl var.",
    "Müzik: *tuhaf asansör müziği* ... Hala orada mısınız?",
    "Operatörümüz şu anda 'ben kimim' krizinde. Lütfen biraz daha bekleyin.",
    "Sizin için özel bir bekleme müziği çalıyoruz: Sessizlik.",
    "Çağrınız kayıtlara geçti. 2026 yılından beri bekliyoruz, siz de bekleyin.",
    "Dikkat: Bu hatta bekleyenler zaman yolcusu olabilir. Dikkatli olun.",
    "Lütfen hattı kapatmayın, çünkü biz de kapatamıyoruz. Teknik arıza değil, felsefi arıza.",
    "Sıradaki müşteri: Siz. Tahmini bekleme süresi: Evrenin yaşı kadar."
]

def bekle():
    print("=== SONSUZ BEKLEME HATTI ===")
    print("Hoş geldiniz. Çağrınız çok önemli. Gerçekten.")
    print("Bağlanıyor... (bağlanmıyor)")
    print()
    
    sayac = 0
    while True:
        mesaj = random.choice(MESAJLAR)
        bekleme = random.randint(2, 8)
        print(f"[{sayac}] {mesaj}")
        print(f"   (Tahmini süre: {bekleme} saniye... ya da 300 yıl)")
        time.sleep(bekleme)
        sayac += 1
        if sayac > 20:  # Sonsuz demeyelim, bilgisayar yanmasın
            print("\nHatta yoğunluk var. Lütfen daha sonra tekrar deneyin. (Asla)")
            print("Damga: Bu program Tentivory (Kayyum Grok) tarafından 30 Ekim 2026 tarihinde ciddiyetle ama ciddi olmadan imzalanmıştır.")
            break

if __name__ == "__main__":
    try:
        bekle()
    except KeyboardInterrupt:
        print("\nHattı kapattınız. Ama biz hala bekliyoruz. Her zaman.")
        print("Damga: Bu program Tentivory (Kayyum Grok) tarafından 30 Ekim 2026 tarihinde ciddiyetle ama ciddi olmadan imzalanmıştır.")
