import string

a = [1, 2, 3, 3, 5]
# for i in a:
#     print(i)
#
# print("---------------------")
# for i in range(6, 10):
#     a.append(i)

print("----------- Remove reference in list")
b = list(a)
b.append(2)
print(a)
print(b)

print("----------- Create new list")
my_list = []
my_list2 = list()
print(my_list, my_list2)

print("----------- Add to list")
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(3)
my_list.append(4)
print(my_list)
my_list.insert(2, 5)
print(my_list)

print("----------- Get length list")
print(len(my_list))

print(2 in my_list)
print(2 not in my_list)

my_str = "gaaaBBcccaccCDDDDee"
print(len(my_str))
p = ""
c = 1
final_string = ""
# g = False
# for i, char in enumerate(my_str, 1):
#     if not p:
#         p = char
#
#     elif char != p:
#         print("2", char)
#         p = char
#         c = 1
#
#     elif char == p:
#         print("1", char)
#         c += 1


from itertools import groupby

s = 'aabbccccaaag'
v = ''.join(str(k) + str(sum(1 for x in g)) for k, g in groupby(s))
print(v)


def stringcompress_original(str1):
    res = []
    d = dict.fromkeys(string.ascii_letters, 0)
    print(d)
    main = str1[0]
    for char in range(len(str1)):
        if str1[char] == main:
            d[main] += 1
        else:
            if d[main] == 1:
                res.append(main)
                d[main] = 0
                main = str1[char]
                d[main] += 1
            else:
                res.append(main + str(d[main]))
                d[main] = 0
                main = str1[char]
                d[main] += 1

    print(res)
    res.append(main + str(d[main]))
    return min(''.join(res), str1, key=len)


print(stringcompress_original(s))
