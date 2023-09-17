import math
# from distance import *

KERNAL_SIZE = 3

def get_data(file):
    positions = []
    for coordinates in open(file, 'r').read().split('\n')[0:-1]:
        temp = coordinates.split(',')
        positions.append((float(temp[0]), float(temp[1])))
    return positions

def get_changes(KERNAL_SIZE):
    positions = get_data('street1.csv')
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

def calculate_rating(ml_info):
    acceleration = get_changes(KERNAL_SIZE)
    rating = 0
    for t in range(0, len(acceleration)):
        if ml_info[1] == 0:
            rating -= ((acceleration[t]) ** 2) - 1
        if ml_info[1] == 1:
            rating -= -(10/(acceleration[t]+1)) - 2
        if ml_info[0] != 0 and ml_info[0] is not None:
            rating -= ((acceleration[t]/4) ** 2) * max((get_distance(ml_info[0])/5) - (3/5), 0)
    return rating
    
# import math
def get_distance(height):
    """
    #licence plate centered about the origin
    n_top_left = ((top_left[0]-top_right[0]) / 2, (bottom_left[1]-top_left[1]) / 2) 
    n_top_right = ((top_right[0]-top_left[0]) / 2, (bottom_right[1]-top_right[1]) / 2)
    n_bottom_left = ((bottom_left[0]-bottom_right[0]) / 2, (top_left[1]-bottom_left[1]) / 2)
    n_bottom_right = ((bottom_right[0]-bottom_left[0]) / 2, (top_right[1]-bottom_right[1]) / 2)

    #correct orientation
    if (n_top_left[1]-n_bottom_left[1]) > (n_top_right[0]-n_top_left[0]):
        o_top_left = (-n_top_right[1], n_top_right[0])
        o_bottom_left = (-n_top_left[1], n_top_left[0])
        o_bottom_right = (-n_bottom_left[1], -n_bottom_left[0])
        o_top_right = (-n_bottom_right[1], -n_bottom_right[0])
    else:
        o_top_left = n_top_left
        o_top_right = n_top_right
        o_bottom_left = n_bottom_left
        o_bottom_right = n_bottom_right
    
    #Finding the height of the license plate
    left_height = math.sqrt((o_top_left[0]-o_bottom_left[0])**2 + (o_top_left[1]-o_bottom_left[1])**2)
    right_height = math.sqrt((o_top_right[0]-o_bottom_right[0])**2 + (o_top_right[1]-o_bottom_right[1])**2)
    height = (left_height + right_height) / 2
    """

    #Using regressed values to find distance
    a1 = 2.02885
    b1 = 14036.5
    a2 = 0.739826
    b2 = -10.6141
    distance = ((a1*height * (3465 / 1080))+b1)/((a2*height * (3465 / 1080))+b2)
    return distance