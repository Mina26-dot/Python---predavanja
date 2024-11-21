#ova bibl sluzi kako bismo radili neke stvari sa operativnim sistemom i hardverom na nasem racunaru
import time

import psutil

# #koliko jezgra imamo
# print(psutil.cpu_count())
#
# #info o mom procesoru
# print(psutil.cpu_stats())
#
# #izlistaj sve procese na racunaru
# processes = psutil.process_iter(['name'])
# for proc in processes:
#     print(proc)
#
# #koliko memorije koristi neki program
# processes = psutil.process_iter(['name', 'memory_percent'])
# for proc in processes:
#     print(f"Process {proc.name()} koristi {proc.memory_percent()} memorije")

#koliko procesora koristi
processes = list(psutil.process_iter(['name', 'memory_percent', 'cpu_percent']))

for proc in processes:
    proc.cpu_percent(interval = None)

time.sleep(1)
#formatiramo ispis
print(f"{'Name' :<25}{'Memory(%)' :<10}{'CPU(%)' :<10}")

for proc in processes:
    print(f"{proc.name() :<25}{proc.memory_percent():<10.2f}{proc.cpu_percent():<10}.")




