import psutil

#nacin na koji dobijamo kolicinu memorije na nasem racunaru
memory_info = psutil.virtual_memory()
print(memory_info)

memory_bytes = memory_info.total
memory_gigabytes = memory_bytes/(1024**3)
print(f"{memory_gigabytes:.2f}")

#formula kako od cifre u bytes (bajtovima) doci do konkretne cifre
#total = 34268663808(bytes)
#        -> 1kb = 1024 bytes
#-> 34268663808 / 1024 = 33.465.492 (kb) => kilobytes
#-> 33.465.492 (kb) / 1024 = 32.682 (mb) => megabytes
#-> 32.681 (mb) / 1024 = 31.915 (gb) = > gigabytes




