'''
This code is used to pre-process the tweets that we received because that file
has a lot of special and alphanumeric characters.
'''

import os
os.chdir('F:/') #My file (Tweets.txt) is in F drive.
import re
string = open('Tweets.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open('Processed.txt', 'w').write(new_str)

'''
This code will strip all the special characters and
replace them with white spaces.
'''
