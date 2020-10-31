import csv
import os
# csv: comma separated value
file = "users.csv"


def read_csv(file=None):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8-sig") as f:
            lines = csv.DictReader(f)
            for line in lines:
                print(line)


def write_csv(file=None):
    with open(file, "w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"name": "shoes 222", "price": 2222})
        writer.writerow({"name": "shoes 223", "price": 233})
        writer.writerow({"name": "shoes 224", "price": 233333})
        writer.writerow({"name": "shoes 225", "price": 55555})


write_csv("products.csv")


