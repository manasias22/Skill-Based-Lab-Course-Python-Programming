#==========file handling=======
#CODE:

print("Enter some text::\n")
while str != "@":
    file1=open("text.txt","a")
    str=input()
    if str != "@":
        file1.write(str+"\n")
        file1.close
        
print("\nContent in the file is::\n")
file1=open("text.txt","r")
file1.seek(0,1)
filetxt=file1.read()
print(filetxt)
file1.close


"""
OUTPUT::

Enter some text::

future is mystry.
tomorrow is history.
today is god gift.
this is random text.

Content in the file is::

future is mystry.
tomorrow is history.
today is god gift.
this is random text.

"""
