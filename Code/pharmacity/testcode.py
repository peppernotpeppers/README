def create_generator():
    mylist = range(4)
    for i in mylist:
        yield i * i


a = create_generator()
for i in a:
    print(i)
