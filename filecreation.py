testfile = open("testfile.txt", "w+")

for i in range(10):
    testfile.write("All work and No Play makes Jacob a Dull Boy \n")

testfile.close()