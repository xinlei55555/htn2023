import math

KERNAL_SIZE = 3

def get_data(file):
    positions = []
    for coordinates in open(file, 'r').read().split('\n')[0:-1]:
        temp = coordinates.split(',')
        positions.append((float(temp[0]), float(temp[1])))
    return positions

def get_changes(KERNAL_SIZE):
    positions = get_data('C:\Krish\Coding\HTN 23\htn2023\street1.csv')
    velocity = []
    for pos in range(0, len(positions) - KERNAL_SIZE, KERNAL_SIZE):
        su = 0
        for num in range(pos, pos + KERNAL_SIZE):
            su += math.sqrt((positions[num + 1][0] - positions[num][0]) ** 2 + (positions[num + 1][1] - positions[num][1]) ** 2) / 0.5
        velocity.append(su / KERNAL_SIZE)

    acceleration = []
    for pos in range(len(velocity) - 1):
        acceleration.append((velocity[pos + 1] - velocity[pos]) / 0.5)
    
    curb = lambda x: (-math.tanh(abs(x) / 30)) + 1

    real_acceleration = []
    for ele in acceleration:
        real_acceleration.append(curb((((ele * 111000) / (KERNAL_SIZE * 0.5)) / 2)) * (((ele * 111000) / (KERNAL_SIZE * 0.5)) / 2))
    
    return real_acceleration

def calculate_change(info):
    acceleration = get_changes(KERNAL_SIZE)
    for t in range(0, len(acceleration)):
        print(acceleration[t])