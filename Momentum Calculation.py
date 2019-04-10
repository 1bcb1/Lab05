# Brooks Brickley & Hector Hernandez CC: 2019
import math
import statistics
name = input('What is the name of the before file that you want to open? : ') + '.csv'

before = open(name, 'r')

name = input('What is the name of the after file that you want to open? : ') + '.csv'

after = open(name, 'r')

firstline = before.readline()
nextline = before.readline()

data = []
while nextline != '':
    data.append(nextline.split(','))
    nextline = before.readline()

p1vxb = []
p1vyb = []
p2vxb = []
p2vyb = []

for i in range(len(data)):
    p1vxb.append((float(data[i][0]))/100)
    p1vyb.append((float(data[i][1])/100))
    p2vxb.append(float(data[i][2])/100)
    p2vyb.append(float(data[i][3])/100)

data = []

firstline = after.readline()
nextline = after.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = after.readline()

p1vxa = []
p1vya = []
p2vxa = []
p2vya = []

for i in range(len(data)):
    p1vxa.append((float(data[i][0]))/100)
    p1vya.append((float(data[i][1]))/100)
    p2vxa.append(float(data[i][2])/100)
    p2vya.append(float(data[i][3])/100)

p1vb = math.sqrt((statistics.mean(p1vxb))**2 + (statistics.mean(p1vyb))**2)
p1va = math.sqrt((statistics.mean(p1vxa))**2 + (statistics.mean(p1vya))**2)
p2vb = math.sqrt((statistics.mean(p2vxb))**2 + (statistics.mean(p2vyb))**2)
p2va = math.sqrt((statistics.mean(p2vxa))**2 + (statistics.mean(p2vya))**2)

momentuum_before = p1vb + p2vb
momentuum_after = p1va + p2va
net_momentum = abs(momentuum_after - momentuum_before)

print('Would you like to save the data to a file?')
answer = input()

if answer == 'yes':
    name = input('What is the name of the file you want to save the data? :') + '.csv'
    out = open(name, 'a')
    trial = input('What is the name of the trial? : ')
    line = trial + ',' + str(net_momentum) + ',' + '\n'
    out.write(line)
