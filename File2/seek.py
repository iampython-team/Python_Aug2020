file5 = open("File2/Seasons.txt",'r')
#file5.write("August is Autumn, May is summer ")


# a - EOF -32 
print(file5.seekable())
print(file5.seek(16))

print(file5.tell())