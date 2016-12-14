from operator import itemgetter
file1path = input()
file2path = input()
file1 = open(file1path)
file2 = open(file2path)
data1 = []
data2 = []
for line in file1:
    data1.append(line.strip().split(','))
for line in file2:
    data2.append(line.strip().split(','))
join = []
for row1 in data1:
    for row2 in data2:
        if row1[2] == row2[0]:
            userId = row2[0]
            userName = row2[1]
            problemId = row1[1]
            problemName = row1[5]
            submitionId = row1[3]
            lenguage = row1[4]
            status = row1[6]
            join_row =[userId,userName,problemId,problemName,submitionId,lenguage,status]
            join.append(join_row)
sorted_join = sorted(join, key=itemgetter(0,6))
for listRow in sorted_join:
    print(",".join(listRow))

