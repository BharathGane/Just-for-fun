import glob, os
file_dir=raw_input("Enter the file directory")
os.chdir(file_dir)
list_of_ = glob.glob("*.mkv")
print sorted(list_of_)
series_name = raw_input("Enter the tv series name")
series_number = input("enter series number")
i = 0
if(series_number < 10):
	series_number = "0" + str(series_number)
for temp in list_of_:
	i+=1
	if(i<10):
		episode_number = "0"+str(i)
	else:
		episode_number = str(i)
	os.system("mv -f " + file_dir + "/" + temp + " " + file_dir + "/" + series_name + "_s" + series_number + "_e" + episode_number + ".mkv" )
