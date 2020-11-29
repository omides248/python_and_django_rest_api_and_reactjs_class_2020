def add_number():
    num = 0
    for i in range(3):
        # print("i", i)
        num += 1
        yield num


res = add_number()
# print(type(res))
# print(next(res))
# print(next(res))
# print(next(res))


price = [10000, 2, 3]
off = [3, 4, 0]
total = 0
for v_a, v_b in zip(price, off):
    print(v_a, v_b)

a = [1, 2, 1, 1]
print(list(set(a)))
