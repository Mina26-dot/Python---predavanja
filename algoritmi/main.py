# Sort, BubbleSort, Factorial Calculation

# Linear search
# Nadji najveci broj u listi -> linearna pretraga

numbers =[3,5,6,13,7,8,12]

max_number = numbers[0] #-> neka nam max broj po difoltu bude prvi broj

#Predji preko svih brojeva, ako je trenutni max manji od broja iz petlje onda je taj iz petlje maximalni.

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

# pronadji br 8

for number in numbers:
    if(number == 8):
        print("Nasli smo broj 8")
        break

# Nadji koliko puta se ponavlja 8
# Nadji koliko puta se ponavlja nesto iz array
# Proveri duplikate


