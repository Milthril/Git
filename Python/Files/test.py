# -*- coding: utf-8 -*-


def text_create(name, msg):
    desktop_path = ""
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


text_create('text', 'Hello world!')

f = open("text.txt", "r")
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        print(line.strip())

f = open("text.txt", "w")
f.write("hhhhhhlllll")
f.close()

f = open("text.txt", "a")
f.writelines(["oooooo", "kkkkk"])
f.close()

f = open("text.txt")
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        print(line.strip('k'))
