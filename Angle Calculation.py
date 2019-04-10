# Brooks Brickley & Hector Hernandez CC: 2019
import math
print("What is the name of the file you want to use?")
name = input() + '.csv'
fileID = open(name, 'r')
print("Is the angle acute or obtuse?")
answer = input()
firstline = fileID.readline()
data = []
nextline = fileID.readline()
while nextline != '':
    data.append(nextline.split(','))
    nextline = fileID.readline()

x = []
y = []
angle = 0
for i in range(len(data)):
    x.append(float(data[i][0])/100)
    y.append(float(data[i][1])/100)

if answer == 'acute':
    adjacent = abs(y[2]-y[0])
    opposite = abs(abs(x[0])-abs(x[2]))
    angle1 = math.degrees(math.atan(opposite/adjacent))
    adjacent = abs(y[2]-y[1])
    opposite = abs(x[2]-x[1])
    angle2 = math.degrees(math.atan(opposite/adjacent))
    angle = angle1 + angle2

if answer == 'obtuse':
    opposite = abs(y[1]-y[2])
    adjacent = abs(x[2]-x[1])
    angle = math.degrees(math.atan(opposite/adjacent)) + 90

print('Would you like to add this to a file to store angle values?')
answer = input()
if answer == 'yes':
    print("What is the name of the file you want to open?")
    name = input() + '.csv'
    print('What trial is this angle from?')
    trial = input()
    out = open(name, 'a')
    line = trial + ',' + str(angle) + ',' + '\n'
    out.write(line)
