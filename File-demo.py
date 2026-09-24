# f = open('test.txt', 'r')

# print(f.name)
# print(f.read())
# print(f.mode)
# f.close()

with open('test.txt', 'r') as f:
    f_contents = f.read(10)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(10)
    # for line in f:
    #     print(line, end='')
    # f_contents = f.readline()
    # print(f_contents,end='')
    # f_contents = f.readline()
    # print(f_contents) 
