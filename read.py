inter = open("text-write.txt", "w")

data=inter.write("username")
inter.close()
with open("test.txt","r") as inter:
    data = inter.read()
    print(data)