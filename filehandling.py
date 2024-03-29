'''#to read a file
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\example.txt","r")
print(f.read())

#To write in a file and delete the old data
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\example.txt","w")
f.write("Python file handling example.")

#To write and add a data
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\example.txt","a")
f.write("written successfully.")


#To append and read a file
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\example.txt","a+")
f.write("byebye")
f.close()
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\example.txt","r")
print(f.read())


f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\example.txt","r+")
print(f.read())
f.write("hi")

#To remove a file
import os
os.remove("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\sample.txt")

#To rename a file
import os
os.rename("sample.txt","example.txt")

#To check file exists or not
import os
file_path = "C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\oops.py"
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
    with open(file_path,'r') as file:
        print(file.read())
else:
    print(f"The file '{file_path}' does not exist.")

#To find the word less than 4
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\notes.txt","r")
data=f.read()
words=data.split()
for i in words:
    if len(i)<4:
            print(i,end=" ")
f.close()

#To find the vowels in lines
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\notes.txt","r")
data=f.read()
vowels='aeiou'
words=data.split()
for i in words:
    if i in vowels:
     print(i,end=' ')
f.close()

#To remove the file using  if else
import os
file_path = "C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\demo.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file '{file_path}' is deleted.")
else:
    print(f"The file '{file_path}' does not exist.")

#To find the words using function
def find_length(f):
    f=open(f,"r")
    data=f.read()
    words=data.split()
    for i in words:
        if len(i)<=4:
            print(i)
find_length("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\notes.txt")

#To count the upper case words
f=open("C:\\Users\\racha\\OneDrive\\Desktop\\sumago\\notes.txt","r")
data=f.read()
count=0
for i in data:
    if i.isupper() :
        count+=1
print(count)
f.close()'''

# Open multiple files for writing using 'with' statement
with open('example.txt', 'a') as file1, open('notes.txt', 'a') as file2: 
    file1.write("hi")
    file2.write("hello")







            












