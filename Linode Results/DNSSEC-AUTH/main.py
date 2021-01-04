import csv
import os
import subprocess

data = None
with open('./results/failed2.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

os.chdir('./results')

count = 0
err_count = 0
child_processes = []
with open("failed3.txt", "a") as f:
    for i in range(0, len(data)):
        item = data[i]
        count += 1

        this_str = "dnsviz probe -A -o " + item[-1] + ".json " + item[-1]
        process = subprocess.Popen(this_str.split(), close_fds=True, start_new_session=True,
                                   stderr=open(os.devnull, 'wb'),
                                   stdout=open(os.devnull, 'wb'))
        child_processes.append(process)
        if count % 1 ==0:
            for cp in child_processes:
                try:
                    cp.wait(35)
                except Exception as e:
                    print(e)
                    f.write(cp.args[-1])
                    f.write("\n")
                    f.flush()
                    err_count += 1
                    pass
            child_processes = []
            print("-----", count / len(data) * 100, "%", count, 'finished but failed', err_count)

print(err_count, "failed among all", count, 'trials')
# if count % 100 == 0:
#     process.communicate()
# _, _ = process.communicate()

# this_str = "dnsviz grok -l warning " + " -r " + item[0] + ".json" + " -o " + item[0] + "-chk.json"
# print(this_str)
# process = subprocess.Popen(this_str.split())
# _, _ = process.communicate()
#
# os.remove(item[0] + ".json")
