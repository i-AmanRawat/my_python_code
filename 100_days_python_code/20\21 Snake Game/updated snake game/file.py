#file handling
file = open("my_file.text")     #bydefault mode is read , mode='r'
content = file.read()
print(content)
file.close()
# content= file.read()      will not work bcz now the file has been closed manually if you want to automate the closing of file then you have to use with keyword

#using with keyword
with open("my_file.text") as file :
    content= file.read()
    print(content)

with open("my_file.text") :
    print(open("my_file.text").read())

with open("my_file.text", mode='w') as file:    #write will overwrite on the existing content of the file, but if you want to add on the content then use append mode 'a'
    file.write("1234")

with open("my_file.text", mode='a') as file:
    file.write("hello")