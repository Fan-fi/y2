import random
number = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
kv = int(input("Какой длины пароль(число):"))
wpass = ""
for i in range(int(kv)):
    wpass += random.choice(number)
print(wpass)
