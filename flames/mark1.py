name1=raw_input("name1:")
name2=raw_input("name2:")
name1=list(name1)
name2=list(name2)
for i in name1:
	if i in name2:
		name1.remove(i)
		name2.remove(i)
for i in name1:
	if i in name2:
		name1.remove(i)
		name2.remove(i)
for i in name1:
	if i in name2:
		name1.remove(i)
		name2.remove(i)
flames=list("flames")
num=len(name2)+len(name1)
count=0
while(len(flames)!=1):
	key=(num+count)%len(flames)
	flames.remove(flames[key-1])
	count=key-1
	if(count<0):
		count=0
if flames[0]=='a':
	print 'affection'
elif flames[0]=='l':
	print 'love'
elif flames[0]=='f':
	print 'friends'
elif flames[0]=='m':
	print 'marriage'
elif flames[0]=='s':
	print 'sister'
elif flames[0]=='e':
	print 'enemies'
