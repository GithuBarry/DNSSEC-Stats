import os
import subprocess
from os import listdir
from os.path import isfile

os.chdir('./results')

json_output_list = [f for f in listdir(".") if
                    isfile(f) and os.stat(f).st_size > 0 and ".json" in f and "-chk.json" not in f]

count = 0
child_processes = []

for i in range(0, len(json_output_list)):
    json_filename = json_output_list[i]
    website = json_filename[:-5]
    count += 1
    # if os.path.exists(website + "-chk.json") and os.stat(website + "-chk.json").st_size > 0:
    #     continue
    this_str = "dnsviz grok -l warning " + " -r " + json_filename + " -o " + website + "-chk.json"
    process = subprocess.Popen(this_str.split(), close_fds=True, start_new_session=True,
                               stderr=open(os.devnull, 'wb'),
                               stdout=open(os.devnull, 'wb'))
    process.wait(5)
    print("-----", count / len(json_output_list) * 100, "%", count, 'finished')
