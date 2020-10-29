'''
PROBLEM 

Given a string of words, reverse all the words.
'''

# SOLUTION

def rev_sentence(s):
	rev = s.split()
	rev.reverse()
	rev = " ".join(rev)
	return rev

reversed_sentence = rev_sentence("Software engineer gradudate programme")
print(reversed_sentence)