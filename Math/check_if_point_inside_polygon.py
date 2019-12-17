'''
Check if Point is Inside Polygon

Given a polygon (created by counterclockwise ordered points, more than 2 points) and a point "p", find if "p" lies inside the polygon or not. 
The points lying on the border are considered inside.

Input: [(0, 0), (3, 0), (3, 2), (0, 2)], (1, 1)
Output: True
Output explanation: In this example the polygon is a rectangle parallel with the X axis.

=========================================
To check if a point is inside a polygon you'll need to draw a straight line (in any of the 4 directions: up, right, down, left),
and count the number of times the line intersects with polygon edges. If the number of intersections is odd then the point
is inside or lies on an edge of the polygon, otherwise the point is outside.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def check_if_point_inside_polygon(polygon, p):
    n = len(polygon)
    # add the first point as last to avoid checking, using modulo (polygon[(i + 1) % n]) or duplicate code for the last point
    polygon.append(polygon[0])
    is_inside = False   # or you can use counter and return (counter % 2) == 1

    for i in range(n):
        if intersect(polygon[i], polygon[i + 1], p):
            is_inside = not is_inside

    return is_inside

def intersect(a, b, p):
    # Y coordinate of p should be between Y coordinates
    # this can be written like (a[1] > p[1]) != (b[1] > p[1])
    if p[1] < max(a[1], b[1]) and p[1] >= min(a[1], b[1]):
        ''' 
        Equation of line:   
        y = (x - x0) * ((y1 - y0) / (x1 - x0)) + y0
        This formula is computed using the gradients (slopes, changes in the coordinates)
        Modify this formula to find X instead Y (because you already have Y)
        '''
        x_intersect = (p[1] - a[1]) * ((b[0] - a[0]) / (b[1] - a[1])) + a[0]

        # check if the point is on the left of the intersection (because in this case you're drawing a line to the right)
        return x_intersect <= p[1]


###########
# Testing #
###########

# Test 1
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (1, 1)))

# Test 2
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (1, 0)))

# Test 3
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (3, 1)))

# Test 3
# Correct result => False
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (3, 3)))