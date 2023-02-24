import csv
with open("data.csv", 'w', newline = '') as f:
    wd = csv.DictWriter(f, ["key1",
                            "key2",
                            "key3"])
    wd.writeheader()
    wd.writerow({"key1":10,
                 "key2":20,
                 "key3":30})