#RegEx /pomocu regEx (regularne expresije) mozemo da trazimo sablone unutar nekog texta ili brojeva

import  re
from sys import prefix

# proveraa da li samo brojevi unutar stringa preko regex-a

ourNumbers = "12345"
# malo slovo r predstavlja da mi trazimo i tretiramo ceo string kao obican tekst - sta god ovde pise mi cemo raditi proveru.
# \ escape karakter
# ^ znaci da pocinjemo da trazimo od poetka stringa
#\d - trazi samo brojeve (0-9)
# + trazi sve sledece brojeve
# $ - kraj stringa

pattern = r"^\d+$"

#proveri da li postoji taj pattern ili sablon unutar stringa ourNumbers
if re.match(pattern, ourNumbers):
    print("Samo brojevi.")
else:
    print("Nisu samo brojevi.")

# regEx koji proverava da li imamo samo slova unutar stringa

sentence = "Ilovepython"

#Character class: [a-z] - trazi slova od a do z
letterPattern = r"^[a-zA-Z ]+$" #razmak - space posle Z

if re.match(letterPattern, sentence):
    print("Only letters")
else:
    print("Not letters")

# da li recenica pocinje velikim slovom

importantSentence = "Today will rain"

capitalPattern = r"^[A-Z]" #trazi na pocetku stringa od a do z veliko

if re.match(capitalPattern, importantSentence):
    print("Has capital letter")


# da li pocinje sa vise karaktera

# phoneNum = "381605463546"
#
# phonePattern = r"^381" #
#
# if re.match(phonePattern, phoneNum):
#     print("Start with 381")

# imamo vise 38 brojeva... 381, 382, 385, 389

phoneNum = "385605463546"

phonePattern = r"^38(1|2|5|9)" #pretrazi taj string da pocinje sa 38( 1 ili 2 ili 5 ili 9)

phoneMatch = re.match(phonePattern,phoneNum)
print(phoneMatch)

phone_map = {
    "381": "Serbia",
    "382": "Montenegro",
    "385": "Bosnia and Hezegovina",
    "389": "Croatia"
}

print(phone_map)

if phoneMatch:
    prefix = "38"+phoneMatch.group(1) #prvo pogadjanje
    country = phone_map[prefix]
    print(f"Prefix number is {prefix} and matching country is {country}")


