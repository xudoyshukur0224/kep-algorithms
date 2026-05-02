# 1. raqamlar yig'indisini topuvchi  funksiya
# 2. raqamlar ko'paytmasini topuvchi  funksiya
# 3. 100, 1000 gacha bo'lgan sonlar kerak, har bir sonni p / s ga qoldiqsiz bo'linadiganni chiqaring
def raqamlar_yigindisi_kopaytmasi(son):
    s, p = 0, 1
    for raqam in str(son):
     s += int(raqam)
     p *= int(raqam)

    return p