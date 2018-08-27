file1 = open('id.txt', 'r')
file2 = open('id1.txt', 'r')
FO = open('id01.txt', 'w')

for line1 in file1:
    for line2 in file2:
        if line1 == line2:
            FO.write("%s\n" %(line1))

FO.close()
file1.close()
file2.close()
