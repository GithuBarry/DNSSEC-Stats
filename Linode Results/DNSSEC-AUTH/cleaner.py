import csv

import os

path = "./results"
files = os.listdir(path)
succeed_list = []
count = 0

for filename in files:
    file_addr = path + '/' + filename
    if os.stat(file_addr).st_size < 2:
        os.remove(file_addr)
    list.append(succeed_list, filename[:-5])


with open('./top10000.csv') as f:
    with open("failures.txt", "a") as ff:
        reader = csv.reader(f)
        data = list(reader)
        for datum in data:
            if datum[-1] not in succeed_list:
                ff.write(datum[-1])
                ff.write("\n")
                ff.flush()
                count+=1
print(count)


