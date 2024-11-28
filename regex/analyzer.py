import re

with open('logs/http.log', 'r') as file:
    lines = file.readlines()

error_pattern = r"Error \d{3]" #-> nadji rec error pracenu za 3 broja
success_pattern = r"Status \d{3]"

#izvlacite podatke iz http/log
#ako je u pitanju error linija upisite u logs/error.log
#Ako je u pitanju status linija upisiste u logs/sucess.log

for line in lines:
    if re.search(error_pattern, line):
        with open('logs/errors.log', 'a') as error_file:
            error_file.write(line)
    elif re.search(success_pattern, line):
        with open('logs/success.log', 'a') as success_file:
            success_file.write(line)


