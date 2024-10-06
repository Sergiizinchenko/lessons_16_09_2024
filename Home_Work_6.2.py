t = ("день,", "днів,", "дні,",)
my_input = int(22493)
day, left_1 = divmod(my_input, 86400)
god, left_2 = divmod(left_1, 3600)
hv, left_3 = divmod(left_2, 60)
god_1 = str(god)
if god < 12:
    god_2 = god_1.zfill(2)
else:
    god_2 = god_1
# day = 55
l, s = divmod(day, 10)
if s == 1 and day != 11:
    print("{} {} {} : {} : {}".format(day, t[0], god_2, hv, left_3))
if s in range(2, 4):
    print("{} {} {} : {} : {}".format(day, t[2], god_2, hv, left_3))
if s in range(5, 20) or day == 0:
    print("{} {} {} : {} : {}".format(day, t[1], god_2, hv, left_3))
print(left_1)  # type: ignore

print(god_2)

print(hv)  # type: ignore

print(left_3)

# print(divmod(day,10))




