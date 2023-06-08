import random

rand_num = random.randint(0, 100)
res = 0
for i in range(1_000_000):
    num = input("Sonni kiriting: ")
    if num == "":
        print("Xato. Raqam kiritilmadi.")
        continue
    num = int(num)
    res += 1
    if rand_num == num:
        print(f"Siz yutdingiz va {res} martada topdingiz ")
        break
    elif rand_num < num:
        print("Xato. Siz kiritgan son katta")
    else:
        print("Xato, Siz kiritgan son kichik")
