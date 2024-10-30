import random

# 1. Parolada kullanılabilecek karakter kümesini oluştur
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# 2. Kullanıcıdan parola uzunluğunu al
uzunluk = int(input("Parolanın uzunluğunu girin: "))

# 3. Parola oluşturma süreci
parola = ""
for _ in range(uzunluk):
    parola += random.choice(karakterler)

# 4. Parolayı ekrana yazdır
print("Oluşturulan Parola:", parola)