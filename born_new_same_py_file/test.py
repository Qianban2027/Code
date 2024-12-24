i=1
s="i=%d\ns=%r\nwith open(\"test%d.py\",\'w\') as file:\n\tfile.writelines(s%%(i+1,s,i+1))\n\tfile.close()"
with open("test1.py",'w') as file:
    file.writelines(s%(i+1,s,i+1))
    file.close()
