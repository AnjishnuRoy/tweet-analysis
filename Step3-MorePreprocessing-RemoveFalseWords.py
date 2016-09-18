import os
import sys
import fileinput

old_string = 'FALSE'

new_string = 'blablabla'

for line in fileinput.input('Processed.txt', inplace=1):
    sys.stdout.write(line.replace(old_string, new_string))
