import csv
import os

path = "./results"
files = os.listdir(path)
succeed_list = []
count = 0

if not os.path.exists('./results'):
    print('no ./results. seems cleaned or not initialized')
    exit()

if not os.path.exists('./results_grok'):
    os.makedirs('./results_grok')

for filename in files:
    file_addr = path + '/' + filename

    if filename[-4:] == '.txt':
        os.replace(file_addr, './' + filename)
        continue

    if filename[-9:] == '-chk.json':
        os.replace(file_addr, './results_grok/' + filename)
        continue

    if os.stat(file_addr).st_size < 1:
        os.remove(file_addr)
        continue

    list.append(succeed_list, filename[:-5])

with open('./top10000.csv') as f:
    with open("probe_failures.txt", "a") as ff:
        reader = csv.reader(f)
        data = list(reader)
        for datum in data:
            if datum[-1] not in succeed_list:
                ff.write(datum[-1])
                ff.write("\n")
                ff.flush()
                count += 1

print("Probe failed",count)
os.replace('./results/', './results_probe/')
