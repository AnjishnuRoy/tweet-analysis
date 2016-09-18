#List of words on the analysis occurs.
Good = ['nice','great','good','awesome', 'growth', 'bought', 'buy', ]
Neutral = ['ok','nothing','tom','is','a','boy', 'is', 'the', 'RT']
Bad = ['jerk','hate', 'change', 'privacy', 'problem', 'apple']


#Opening text file containing twitters
file = open("Processed.txt", "r").read().split(' ')


print file

words = file

text = [word.strip(",.") for line in words for word in line.lower().split()]

postivity = 0
negativity = 0
no_significance = 0

for word in words:
	if(word in Good):
		print "found "+str(word)
		postivity = postivity + 1
		print "++"
	if(word in Bad):
		print "found "+str(word)
		negativity = negativity + -1
		print "--"
	if(word in Neutral):
		print "found "+str(word)
		no_significance = no_significance + 0
		print "Nothing counted"
	print "\n"

print "\nthe input text has a positivity rating of : "+str(postivity)
print "\nthe input text has a negativity rating of : "+str(negativity)
print "\nUseless words: "+str(no_significance)

total = postivity + negativity + no_significance

print "\nTotal Score: "+str(total)



