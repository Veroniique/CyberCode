
#Open in binary mode using 'b'
#Add image name here
f = open('snowie.png','rb')

#Read image binary data
contents = f.read()

#Change printing title to image name
print("Contents of Snowie.png: \n")
print(contents)

f.close()