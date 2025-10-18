import argparse
import fileinput
import re

# Use regex to detect common secret patterns
pattern1 = r"/(^|[^@\w])@(\w{1,15})\b/" # Twitter username
pattern2 = r"EAACEdEose0cBA[0-9A-Za-z]+" # Facebook access token
pattern3 = r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)" # Instagram username
pattern4 = r"AIza[0-9A-Za-z-_]{35}" # Google API key
pattern5 = r"xoxp-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}" # Slack user access token

# Accept a directory path or file as input
file = fileinput.input(input("Input file name : "))

# Output a report of findings (filename, line number, matched string)
lineNum = 1
for line in file:
    if re.search(pattern1, line):
        print("Line " + str(lineNum) + ": " + line + "......." + "Twitter username found")
    elif re.search(pattern2, line):
        print("Line " + str(lineNum) + ": " + line + "......." + "Facebook access token found")
    elif re.search(pattern3, line):
        print("Line " + str(lineNum) + ": " + line + "......." + "Instagram username found")
    elif re.search(pattern4, line):
        print("Line " + str(lineNum) + ": " + line + "......." + "Google API key found")
    elif re.search(pattern5, line):
        print("Line " + str(lineNum) + ": " + line + "......." + "Slack user access token found")
    else:
        print("Line " + str(lineNum) + ": " + line + "......." + "Nothing found")
    lineNum += 1




