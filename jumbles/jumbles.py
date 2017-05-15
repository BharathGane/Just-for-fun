from PyDictionary import PyDictionary
dictionary=PyDictionary()
import warnings
def permute1(start, rest):
	res = []
	if len(rest) <= 1:
		res += [start + rest, rest + start]
	else:
		for i, c in enumerate(rest):
			s = rest[:i] + rest[i+1:]
			for perm in permute1(c, s):
				res += [start + perm]
	return res
text_word = raw_input("Input A Jumbled Word To Find The Meaning : ")
x = permute1('',text_word)
z=[]
for i in x:
	if i not in z:
		z.append(i)
# print dictionary.meaning("apple")
# for i in z:
# 	try:
# 		(dictionary.meaning(i))
# 	except Error:
# 		pass

import enchant
d = enchant.Dict("en_US")

for i in z:
	warnings.filterwarnings("UserWarning")
	if d.check(i) == True:
		print i,dictionary.meaning(i)
	else:
		pass