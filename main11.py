import json
from platform import system
from datetime import datetime

# 1. Budzet
# 2. Dodavanje troskova
# 3. Brisanje troskova
# 4. Logovanje troskova


user = None
max_budget = 100000
with open("data11/user.json", 'r') as file:
    user = json.load(file)

user_budget = user['budget'] + user['credit']
print(user_budget)
# Definisati koliki je maksimalni budzet,
# ako korisnik ima veci od maksimalno budzeta ili manji od 0 ispisati gresku.

if user_budget >= max_budget or user_budget <= 0:
    print("Desila se greska. Vas budzet je veci od dozvoljenog ili je premali!")
    exit() #kod se stopira, ne ide dalje

print(f"Dobar dan! Dobrodosli nazad Vas budzet iznosi: {user_budget}")

# Dodavanje troskova
expense = 0

while expense <= 0 or expense > user_budget:
    expense = int(input("Molim vas unesite iznos troskova: "))

#Logovanje troskova
# Napraviti text file koji se zove "expense_log.txt"
# Upisati svaki trosak u sledecem formatu
# "Amount : cifra_expense, user: id (1), DateTime: 21.08.2024. 5:55:05, Budget: trenutni_budzet, Preostali budzet: PREOSTALI_BUDZET


with open("logs/expense_log.txt", 'a') as file: #a je da dodaje podatke u txt, jer w brise prethodno i postavlja novo
    remaining_budget = user_budget-expense
    message = f"\nAmount: {expense}, User: {user["id"]}, Budget: {user_budget}, Preostali budzet: {remaining_budget}, DateTime: {datetime.now()}"
    file.write(message)




