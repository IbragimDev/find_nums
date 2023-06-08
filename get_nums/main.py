import random

rand_num = random.randint(0, 100)
res = 0
while True:
    num_input = input("Sonni kiriting: ")
    if num_input == "":
        continue
    num = int(num_input)
    res += 1
    if rand_num == num:
        print(f"Siz yutdingiz va {res} martada topdingiz ")
        break
    elif rand_num < num:
        print("Xato. Siz kiritgan son katta")
    else:
        print("Xato, Siz kiritgan son kichik")
