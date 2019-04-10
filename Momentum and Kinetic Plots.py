# Brooks Brickley & Hector Hernandez CC: 2019
import math
import matplotlib.pyplot as plt
import statistics as stat

print('What is the name of the file that has the data before?')
name = input() + '.csv'

before = []
filebefore = open(name, 'r')

print('What is the name of the file that has the data after?')
name1 = input() +'.csv'

after = []
fileafter = open(name1, 'r')

firstline = filebefore.readline()
nextline = filebefore.readline()

while nextline != '':
    before.append(nextline.split(','))
    nextline = filebefore.readline()

firstline = fileafter.readline()
nextline = fileafter.readline()

while nextline != '':
    after.append(nextline.split(','))
    nextline = fileafter.readline()

p1vxb = []
p1vyb = []
p2vxb = []
p2vyb = []
tb = []
for i in range(len(before)):
    p1vxb.append(float(before[i][0])/100)
    p1vyb.append(float(before[i][1])/100)
    p2vxb.append(float(before[i][2])/100)
    p2vyb.append(float(before[i][3])/100)
    tb.append(float(before[i][4])/1000)

p1vxa = []
p1vya = []
p2vxa = []
p2vya = []
ta = []
for i in range(len(after)):
    p1vxa.append(float(after[i][0])/100)
    p1vya.append(float(after[i][1])/100)
    p2vxa.append(float(after[i][2])/100)
    p2vya.append(float(after[i][3])/100)
    ta.append(float(after[i][4])/1000)
averagep1vxb = stat.mean(p1vxb)
averagep1vyb = stat.mean(p1vyb)
averagep2vxb = stat.mean(p2vxb)
averagep2vyb = stat.mean(p2vyb)
averagep1vxa = stat.mean(p1vxa)
averagep1vya = stat.mean(p1vya)
averagep2vxa = stat.mean(p2vxa)
averagep2vya = stat.mean(p2vya)

p1vb = math.sqrt((averagep1vxb)**2 + (averagep1vyb)**2)
p2vb = math.sqrt((averagep2vxb)**2 + (averagep2vyb)**2)
p1va = math.sqrt((averagep1vxa)**2 + (averagep1vya)**2)
p2va = math.sqrt((averagep2vxa)**2 + (averagep2vya)**2)

momentum_b1 = []
momentum_a1 = []
kinetic_b1 = []
kinetic_a1 = []
momentum_b2 = []
momentum_a2 = []
kinetic_b2 = []
kinetic_a2 = []

for i in range(len(p1vxb)):
    velocity1 = math.sqrt((p1vxb[i])**2 + (p1vyb[i]) ** 2)
    velocity2 = math.sqrt((p2vxb[i])**2 + (p2vyb[i])**2)
    momentum_b1.append((velocity1)/100)
    kinetic_b1.append((.5 * velocity1 ** 2)/100)
    momentum_b2.append(velocity2/100)
    kinetic_b2.append((.5 * velocity2 ** 2)/100)

for i in range(len(p1vxa)):
    velocity1 = math.sqrt((p1vxa[i])**2 + (p1vya[i]) ** 2)
    velocity2 = math.sqrt((p2vxa[i])**2 + (p2vya[i])**2)
    momentum_a1.append((velocity1)/100)
    kinetic_a1.append((.5 * velocity1 ** 2)/100)
    momentum_a2.append((velocity2)/100)
    kinetic_a2.append((.5 * velocity2 ** 2)/100)

ax1 = plt.subplot(2, 2, 1)
ax1.plot(tb, momentum_b1, '-g', label='Puck 1')
ax1.plot(tb, momentum_b2, '-r', label='Puck 2')
ax1.legend()
ax1.set(ylabel='Momentum (Kgm/s)')
ax1.set(xlabel='Time (s)')
ax1.set_title('Momentum before Collision')

ax2 = plt.subplot(2, 2, 2)
ax2.plot(ta, momentum_a1, '-g', label='Puck 1')
ax2.plot(ta, momentum_a2, '-r', label='Puck 2')
ax2.legend()
ax2.set(ylabel='Momentum (Kgm/s)')
ax2.set(xlabel='Time (s)')
ax2.set_title('Momentum after Collision')

ax3 = plt.subplot(2, 2, 3)
ax3.plot(tb, kinetic_b1, '-g', label='Puck 1')
ax3.plot(tb, kinetic_b2, '-r', label='Puck 2')
ax3.legend()
ax3.set(ylabel='Kinetic Energy (J)')
ax3.set(xlabel='Time (s)')
ax3.set_title('Kinetic Energy before Collision')

ax4 = plt.subplot(2, 2, 4)
ax4.plot(ta, kinetic_a1, '-g', label='Puck 1')
ax4.plot(ta, kinetic_a2, '-r', label='Puck 2')
ax4.legend()
ax4.set(ylabel='Kinetic Energy (J)')
ax4.set(xlabel='Time (s)')
ax4.set_title('Kinetic Energy after Collision')
title = input('What do you want to name the plots? :') + '\u00b0'
plt.suptitle(title)
plt.show()
