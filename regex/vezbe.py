import re

# name = "Mina Vasiljevic"
#
# pattern = r"[A-Z][a-z]+ [A-Z][a-z]+$" #trazi prvo veliko slovo pa posle njega malo slovo nastavi za svaki sledeci karakter, nadji razmak posle njega da imamo veliko slovo pa malo slovo i da ide do kraja
#
# if re.match(pattern, name):
#     print("Ime i prezime")


#======================================

email = "mina@gmail.com"

# proveri neki tekst pre @ (slova . -)
# \w proveravamo da li postoje slova
# \.-
# Proveri da li sadrzi [\w\.-] (sliva ili . ili - )
# Posle toga da li sadrzi @
# text pa @ pa tekst / kad god hocemo da nastavimo dalje ide +
# Proveravamo da li postoji tacka
# \w
#Rezultat
# [\w\.-] -> Mina
# +@ -> @
# [\w\.-] -> gmail
# \. -> .
# \w -> com

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_pattern, email):
    print("It is email")
