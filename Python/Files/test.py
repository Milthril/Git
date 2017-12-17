# -*- coding: utf-8 -*-


def text_create(name, msg):
    desktop_path = "Python/Files/"
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


text_create('text', 'Hello world!')

f = open("Python/Files/text.txt", "r")
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        print(line.strip())

f = open("Python/Files/text.txt", "w")
f.write("hhhhhhlllll")
f.close()

f = open("Python/Files/text.txt", "a")
f.writelines(["oooooo", "kkkkk"])
f.close()

f = open("Python/Files/text.txt")
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        print(line.strip('k'))
