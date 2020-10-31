from collections.abc import Iterable

# f = open("./my_file.txt")
# print(f, isinstance(f, Iterable))

#
# for line in f:
#     print(line)
#
# f.close()
import os


def read_file(file=None):
    if os.path.exists(file):
        with open(file) as f:
            print(f, isinstance(f, Iterable))

            for line in f:
                print(line, line.encode("utf-8"))
    else:
        print("file not found")


def write(file=None):
    with open(file, "a") as f:
        f.write("\nsadasdasd222")


def update_file(file=None):
    with open(file) as f:
        # f.read()
        data = f.readlines()

    for line, content in enumerate(data, 0):
        if line == 2:
            data[line] = "mohamd"

    # print(data)
    with open(file, "w") as f:
        f.writelines(data)


file = "./my_file.txt"

# read_file(file)
# write(file)
# update_file(file)

# with open(file) as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())


