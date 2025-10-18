SecretScanner.py
================

Purpose and Explanation
-----------------------
This application demonstrates a scanner that can pick up potential usernames and tokens based on regex patterns. The program uses common regex patterns and searches any input text file for a match. All lines in the file are searched and if there is a match, the program will output the matching pattern in the console as well as the pattern's matching token type; if none is detected, the console will display "Nothing found". There are three files located in the project folder that each hold at least one detectable regex pattern. The user may input the name and extension of each of these files to run the demonstration.

How to use the program
----------------------
There are two ways to run the program:
1. Simply run the program by double-clicking it from the project directory.
2. Open the command line and change the directory to the folder containing the program, then run the program directly in the command line.

Once the input prompt is on screen, input one of these three filenames to run a check: secrets.txt, apikeys.txt, or lorem.txt.

Limitations
-----------
The program is limited to only being able to detect X (Twitter) usernames, Facebook access tokens, Instagram usernames, Google API keys, and Slack user access tokens. However, other patterns would easily be able to be added to the program if needed. Also, the program only scans one file at a time, but can scan an unlimited number of files while it is active.
