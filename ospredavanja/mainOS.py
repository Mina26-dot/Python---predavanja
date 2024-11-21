import platform

#operativni sistem koji koristimo
print(platform.system())

#detaljne informacije o nasem operativnom sistemu
print(platform.platform())

#verzija python-a na mom racunaru
py_version = platform.python_version()
print(f"Verzija python-a na mom racunaru je: {py_version}")

#ZADATAK
# Ako je verzija py-a koju koristimo > ili < od 3 onda ispisati poruku :
# "Ne koristite dobru verziju pajtona

version = int(py_version[0])

if version != 3:
    print("Ne koristite dobru verziju pajtona")
else:
    print("Imate dobru verziju pajtona.")