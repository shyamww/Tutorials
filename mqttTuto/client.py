# import socket

# c = socket.socket()

# c.connect(('localhost',9876))

# # name = "shyam"

# for i in range(5):
#     name = input("Topic 1 or 2")
#     c.send(bytes(name,'utf-8'))
#     print(c.recv(1024).decode())


from random import randrange, uniform

# randrange gives you an integral value
for i in range(5):
    irand = randrange(3,3)
    print(irand)


# uniform gives you a floating-point value
# frand = uniform(0, 10)



# print(irand)
# print(frand)