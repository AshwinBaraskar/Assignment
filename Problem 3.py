'''Write a function to parse a log file & extract details of Errors & Warnings recorded into a separate file.'''

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print("Logging Module Demo")
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

import re

log_file_path = "log.txt"
regex = '[:a-zA-z]+'

match_list = []
with open(log_file_path, "r") as file:
    w = file.read()
    print(w)
    for line in file:
        for match in re.finditer(regex, line):
            match_text = match.group()
            match_list.append(match_text)
            print(match_text)
    with open('newfile.txt', 'w+') as f:
        f.write(w)
