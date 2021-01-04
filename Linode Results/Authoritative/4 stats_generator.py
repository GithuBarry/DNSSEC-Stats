import json
import os
import re

path = "./results_grok"
files = os.listdir(path)

count = 0


def find(target, dictData, notFound='not found'):
    queue = [dictData]
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == target:
                return value
            elif type(value) == dict:
                queue.append(value)
    return notFound


def findAll(target, dictData, notFound=[]):
    queue = [dictData]
    result = []
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == target:
                result.append(value)
            elif type(value) == dict:
                queue.append(value)
    if not result: result = notFound
    return result


err_record = dict()


def add_to_record(key, new_value):
    if key in err_record:
        # append the new number to the existing array at this slot
        err_record[key].append(new_value)
    else:
        # create a new array in this slot
        err_record[key] = [new_value]


# code = find('code', f)
# print(code)
for filename in files:
    website = filename[:-9]
    filename = path + '/' + filename
    if os.stat(filename).st_size < 2:
        print(filename[:-9])
    if os.stat(filename).st_size > 2:

        if filename.find('json') > 0 and filename.find('chk') > 0:
            count += 1
            with open(filename, 'rb') as f:
                data = f.read().decode("utf-8")
                matched = re.findall(r'"code": "[A-Z_]*"', data)
                for item in (set(matched)):
                    add_to_record(item[9:-1], website)

with open('results_warnings.json', 'w') as fp:
    json.dump(err_record, fp)

keys = err_record.keys()
for key in keys:
    err_record[key] = len(err_record[key])
err_record = {k: v for k, v in sorted(err_record.items(), key=lambda item: item[1], reverse=True)}
print(err_record)
print(count)

with open('results_warning_stats.json', 'w') as fp:
    json.dump(err_record, fp)
