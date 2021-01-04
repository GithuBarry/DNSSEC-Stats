import json
import os
import re

path = "./results_grok_info"
files = os.listdir(path)

count = 0

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
                matched = re.findall(r'"status": "(INSECURE|BOGUS|LAME|SECURE|INCOMPLETE)*"', data)
                if len(matched)<1:
                    print(filename)
                else:
                    status = matched[-1]
                    add_to_record(status, website)

with open('results_delegation.json', 'w') as fp:
    json.dump(err_record, fp)

keys = err_record.keys()
for key in keys:
    err_record[key] = len(err_record[key])
err_record = {k: v for k, v in sorted(err_record.items(), key=lambda item: item[1], reverse=True)}
print(err_record)
print(count)

with open('results_delegation_stats.json', 'w') as fp:
    json.dump(err_record, fp)
