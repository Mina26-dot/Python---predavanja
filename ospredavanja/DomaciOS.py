from multiprocessing.dummy import current_process

import psutil

cpu_usage = psutil.cpu_percent(interval = 1)
print(cpu_usage)


#fizicka jezgra/ logicka jezgra
cores = psutil.cpu_count(logical = False)

#logicka jezgra
logical_cores = psutil.cpu_count(logical = True)

current_process = psutil.Process()
num_threads = current_process.num_threads()

print(f"Total CPU usage : {cpu_usage}%")
print(f"Number of psyhical cores: {cores}")
print(f"Number od logical cores: {logical_cores}")
print(f"Number of threads in current process: {num_threads}")

#Ram memorija -> u cemu se iskazuje memorija (gb/mb)
#procesor -> izgradjen od jezgra
         #-> fizicka jezgra
         #-logicka jezgra
#storage -> ssd, nvme, hdd
         #-> za sta sluzi
         #-> koje su razlike? koji je najbolji


