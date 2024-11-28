# izvuci sva vremena iz logs/errors.log
import re

from pythonProject.regex.main2 import pattern

with open('logs/errors.log') as error_log:

    pattern = r"\d{2}:\d{2}:\d{2}"

    for error in error_log.readlines():
        match = re.search(pattern, error)
        print(match)