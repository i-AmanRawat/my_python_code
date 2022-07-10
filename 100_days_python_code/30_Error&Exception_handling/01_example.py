#keywords for error handling and catching exception

try:
    file= open("daata.txt")     #by default mode = read
    dict= {'key':'value'}
    print(dict['gfgf'])
except FileNotFoundError:
    file= open("daata.txt", 'w')
    file.write("hello there!")
except KeyError as errormessage :
    print(f"The key {errormessage} doesn't exist.")
else:
    content= file.read()
    print(content)
finally:
    file.close()
    print("file has been closed.")
    raise TypeError("This erroe is raised by me ! ")   #😝😅 apni marji se error bhi bna sakte ho tum


'''
    try run kro try m koi glti hai toh except run krega 
    agr try sahe hai toh else run krega (bcz except run nhi kra)
    and lastly finally toh run hoga he 
'''
