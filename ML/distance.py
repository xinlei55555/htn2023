import math
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