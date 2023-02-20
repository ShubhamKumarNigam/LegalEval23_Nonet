import os
import re
import csv
#import spacy 
# Function to remove the HTML tags
# from the given tags
def RemoveHTMLTags(strr):
     
    # Print string after removing tags
    return re.compile(r'<[^>]+>').sub('', strr)
def Reverse(lst):
    return [ele for ele in reversed(lst)]
count1=0
count2=0
fi=os.listdir("Music/")

fields = ['uid', 'decision', 'explanation'] 
filename = "predictions15.csv"
    

row=[]


#print(len(fi))
#f=open("win_loss.txt","a+")
all_docs=os.listdir("Music/")
v=[]
for i in range(0,len(fi)):
	file_pointer=open("Music/"+fi[i],"r+")
	ff=str(file_pointer.read())
	fff=ff.split()
	lll=fff[len(fff)-300:len(fff)]
	text=""
	for j in range(0,len(lll)):
		text=text+lll[j]+" "	
	print(text)
	#fff=str(RemoveHTMLTags(ff))
	ffff=ff.split(".")
	#ffff=Reverse(ffff)
	#print(fffff)
	#ffff=ffff[-30:]
	for j in range(0,len(ffff)):
		if (("dispose" in ffff[j]) or ("disposed" in ffff[j]) or ("accept" in ffff[j]) or ("allow" in ffff[j]) or ("allowed" in ffff[j]) or ("accepted" in ffff[j]) or ("upheld" in ffff[j])):
			print(fi[i]+" "+"1")
			v.append(fi[i])
			count1=count1+1
			row.append([fi[i].split(".")[0],"Accepted",text])
			#f.write(fi[i]+"------"+"Appealant Won\n")
			break
			#print("accept")

		elif ( ("dismiss" in ffff[j]) or ("dismissed" in ffff[j]) or ("reject" in ffff[j]) or ("rejected" in ffff[j]) or ("discarded" in ffff[j]) or ("discard" in ffff[j])):
			#print("reject")
			print(fi[i]+" "+"0")
			v.append(fi[i])
			count2=count2+1
			row.append([fi[i].split(".")[0],"Denied",text])
			#f.write(fi[i]+"------"+"Defendant Won\n")
			break
	#print()
		#else:
			#v.append(fi[i])
			#count2=count2+1
		#	f.write(fi[i]+"------"+"No Judgement\n")
		#	break
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(row)    
# data rows of csv file 
#print(count1,count2)
#print("------------")
#print(len(v),len(all_docs))
#v1=set(all_docs)-set(v)
#v1=list(v1)
#for i in range(0,len(v1)):
#		f.write(v1[i]+"------"+"No Judgement\n")
#print(list(v1)[1])
#print(list(v1))


