# Quantifiers
import re

# *: Matches 0 or more occurrences -> da li ima 0 ili vise ponavljanja odredjenog slova npr a* "","a","aa"
# +: Matches 1 or more occurrences
# ?: Matches 0 or 1 occurrence -> ima 0 ili 1
# {n}: Matches exactly -> a{3} -> "aaa"
# {n,}: Matches n or more occurrences a{2,} -> "aa","aaa"...
# {n,m}: Matches between n and m occurrences a{2,4}, "aa","aaa","aaaa"...

bonus_codes = "ABC123, bonus455, bonus22"

# [A-Za-z]{3} -> pronadji svuda gde imamo 3 slova zaredom
# \d trazimo brojeve
#\d{3} -> pronadji sablon gde imamo 3 broja zaredom

pattern = r"[A-Za-z]{3}\d{3}"
product_codes = re.findall(pattern, bonus_codes)
print(product_codes)

# rec do 5 slova, pracena sa minimum 2 broja

username = "mina123"
username_pattern = r"[a-zA-Z]{1,5}\d{2,}"
match = re.match(username_pattern, username)

if match:
    print(match.group())

