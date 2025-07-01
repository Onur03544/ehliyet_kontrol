isim = input("Adınız: ")
yas = int(input("Yaşınız: " ))

if yas < 18:
    kalan = 18 - yas
    print(f"Kanka {isim} ehliyet alman için daha {kalan} yıl beklemen gerekiyo üzgünüm")
else:
    print(f"Aferim sana ehliyet alabiliyosun hadi bekleme ehliyet al {isim}")