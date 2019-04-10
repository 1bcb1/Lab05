# Brooks Brickley & Hector Hernandez CC: 2019
import matplotlib.pyplot as plt

name = input('What is the name of the angles file you want to open? :') + '.csv'
angles = open(name, 'r')

name = input('What is the name of the momentum file that you want to open? :') + '.csv'

momentuum = open(name, 'r')

data = []
nextline = angles.readline()
while nextline != '':
    data.append(nextline.split(','))
    nextline = angles.readline()

theta = []
for i in range(len(data)):
    theta.append(float(data[i][1]))

data = []
nextline = momentuum.readline()
while nextline != '':
    data.append(nextline.split(','))
    nextline = momentuum.readline()

deviation = []
for i in range(len(data)):
    deviation.append(float(data[i][1]))
coord = []
for i in range(len(theta)):
    coord.append([theta[i], deviation[i]])
coords = sorted(coord)
theta = []
deviation = []
for i in range(len(coords)):
    theta.append(coords[i][0])
    deviation.append(coords[i][1])

plt.plot(theta, deviation, '*r-')
plt.title('Deviation of Momentum vs. Angle Measurement')
plt.xlabel('Degrees\u00b0')
plt.ylabel('Momentum (Kgm/s)')
plt.show()
