from time import sleep
from os import sys
import os
import random

words_list = open('words.txt','r')
words_list = words_list.read()
words_list = words_list.split('\n')
#print words_list
# words_list = words_list.sort()
used_word = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
rand_number = int((random.random()*100)%26)

next_word_start = alphabet[rand_number]
# print words_list
print "Start a word which starts with "+ next_word_start

# print "Enter a word"
# first_word=raw_input('word>')
# next_word_start = first_word

while True:
	word=raw_input('word>')
	if word[0] != next_word_start:
		print "wrong input"
	elif word not in used_word:
		start_letter = word[0]
		end_letter	 = word[-1]
		for words in words_list:
			if words[0] == end_letter:
				print words
				next_word_start = words[-1]
				words_list.remove(words)
				used_word.append(word)
				print "Next word start letter is "+ next_word_start
				break
	else:
		print "word already used"
