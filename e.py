def getFullPosible(x,y):
    posibles = []
    for j in range(8):
        for i in range(8):
            if abs(i-x) == abs(j-y):
                posibles.append((i,j))
    return posibles

fem = "3k4/8/8/2P1P3/3B4/2R1R3/8/4K3 w - - 0 1"#input()
values = fem.strip().split()
rowsString = values[0]
turn = values[1]
rows = rowsString.split("/")
chess = [
    ['1','2','3','4','5','6','7','8'],
    ['1', '2', '3', '4', '5', '6', '7', '8'],
['1','2','3','4','5','6','7','8'],
['1','2','3','4','5','6','7','8'],
['1','2','3','4','5','6','7','8'],
['1','2','3','4','5','6','7','8'],
['1','2','3','4','5','6','7','8'],
['1','2','3','4','5','6','7','8']
]

whites = "PRNBQK"
blacks = "prnbqk"
whiteBishop = "B"
blackBishop = "b"

if turn == "w":
    myBishop = whiteBishop
    myEnemies = blacks
    myPieces = whites
else:
    myBishop = blackBishop
    myEnemies = whites
    myPieces = blacks

for i in range(len(rows)):
    newStringRow = ""
    for c in rows[i]:
        if c in "12345678":
            newStringRow += int(c)*"-"
        else:
            newStringRow += c
    rows[i] = newStringRow


for i in range(8):
    for j in range(8):
        c = rows[i][j]
        if c == "-":
            chess[i][j] = "-" #empty
        elif c == myBishop:
            chess[i][j] = "B" #bichop
        elif c in myEnemies:
            chess[i][j] = "E" #enemy
        else:
            chess[i][j] = "M" #mine
results =[]

def removeIfWalled(posibles,posible,i,j):
    for jj in range(8):
        for ii in range(8):
            c2 = chess[ii][jj]
            isEmpty = c2=="-"
            if not isEmpty:
                distBishopWallX =  abs(i-ii)
                distBishopWallY = abs(j-jj)
                distBishopPosibleX = abs(i-posible[0])
                distBishopPosibleY = abs(j-posible[1])
                distWallPosibleX = abs(posible[0] - ii)
                distWallPosibleY = abs(posible[1] - jj)
                if distWallPosibleX == distWallPosibleY and distBishopWallX < distBishopPosibleX and distBishopWallY < distBishopPosibleY:
                    posibles.remove(posible)
                    return


def isMine(posible):
    return chess[posible[0]][posible[1]] in "MB"

def isEnemy(posible):
    return chess[posible[0]][posible[1]] == "E"

for j in range(8):
    print(chess[j])

for j in range(8):
    for i in range(8):
        c = chess[i][j]
        if c == "B":
            posibles = getFullPosible(i,j)
            print(posibles)
            for posible in posibles:
                if isMine(posible):
                    posibles.remove(posible)
                elif isEnemy(posible):
                    continue
                else: #sera posible solo si no hay nada tapandolo
                   removeIfWalled(posibles,posible,i,j)
            print(posibles)