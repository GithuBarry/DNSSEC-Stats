import csv
import os

path = "./results_probe"
files = os.listdir(path)
succeed_list = []
count = 0

if not os.path.exists('./results_probe'):
    print('no ./results_probe. Either cleaned or not initialized')
    exit()

if not os.path.exists('./results_grok_info'):
    os.makedirs('./results_grok_info')

for filename in files:
    file_addr = path + '/' + filename

    if filename[-4:] == '.txt':
        os.replace(file_addr, './' + filename)
        continue

    if '-chk.json' in filename:
        os.replace(file_addr, './results_grok_info/' + filename)
        continue

    if os.stat(file_addr).st_size < 1:
        os.remove(file_addr)
        continue

    list.append(succeed_list, filename[:-5])
