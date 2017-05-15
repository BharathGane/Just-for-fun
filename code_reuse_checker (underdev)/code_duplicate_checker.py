import glob

file_name = raw_input("enter file name : ")
f = open(str(file_name),"r")
input_file = f.read().split("\n")
original_code = list()
duplicate_code = list()
empty_character = 0
blank_character = 0
for i in input_file:
	if i is "":
		empty_character+=1
	elif i is " ":
		blank_character+=1
	elif i not in original_code:
		original_code.append(i)
	else:
		duplicate_code.append(i)
import pprint
print "number of lines of original_code without blank lines : " + str(len(original_code))
print "number of lines of  duplicate_code without blank lines : " + str(len(duplicate_code))
print "number of blank_character : " + str(blank_character)
print "number of empty_character : " + str(empty_character)

if len(input_file)>100 and len(duplicate_code) < 100:
	print "probablity of same code used very less"
elif len(duplicate_code) >= len(original_code):
	print "probablity of same code used very high"
elif len(duplicate_code) - len(original_code) > len(input_file) /2:
	print "probablity of same code used very high" 
else:
	print "need to be checked manually"
# pprint.pprint(original_code)
# pprint.pprint(duplicate_code)