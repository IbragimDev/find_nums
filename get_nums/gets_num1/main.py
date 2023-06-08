"""import random

begin = 1
end = 100
for i in range(1_000_000):
    num = random.randint(begin, end)
    answer = input(
        f"Men o`ylagan son {num}. \n \t"
        f"Agar siz o`ylagan son {num} ga teng bo`lsa (t) harfini kiriting. \n \t"
        f"Agar siz o`ylagan son {num} dan katta bo`lsa (k) harfini kiriting. \n \t"
        f"Agar siz o`ylagan son {num} dan kichik bo`lsa (w) harfini kiriting.: "
    )
    if answer == "t":
        print("Topdim")
        break
    elif answer == "k":
        end = num - 1
    elif answer == "w":
        begin = num + 1
"""

import random

bosh = 1
oxir = 100
for i in range(1_000_000):
    taxmin = random.randint(bosh, oxir)
    javob = input(
        f"Men {taxmin} sonini o'yladim. \n"
        f"To'g'ri (t), katta (+), yoki kichik (-) ? "
    )
    if javob == "t":
        print("Yutdim!")
        break
    elif javob == "+":
        bosh = taxmin + 1
    elif javob == "-":
        oxir = taxmin - 1
