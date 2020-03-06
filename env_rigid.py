import numpy as np
import matplotlib.pyplot as plt
import cv2
from collections import deque
import math


class Nodes:
    def __init__(self,state,parent,cost):
        self.state = state
        self.cost = 19999
        self.parent = None

def coll_circle(position):
	p_x = position[1]
	p_y = position[0]
	location = np.sqrt((p_x -225)**2+(p_y -50)**2) - (25+radius+clearance)
	if location < 0:
		return True
	else:
		return False

def coll_ellipse(position):
	p_x = position[1]
	p_y = position[0]
	center = [150,100]
	location = ((float(p_x)-150)**2/(40+radius+clearance)**2) + ((float(p_y)-100)**2/(20+radius+clearance)**2) -1.0
	if location < 0:
		return True
	else:
		return False

def area(x1, y1, x2, y2, x3, y3):
	return abs((x1 * (y2 - y3) + x2 * (y3 - y1)+ x3 * (y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):
	A = area (x1, y1, x2, y2, x3, y3)
	A1 = area (x, y, x2, y2, x3, y3)
	A2 = area (x1, y1, x, y, x3, y3)
	A3 = area (x1, y1, x2, y2, x, y)

	if(A == (A1 + A2 + A3)):
		return True
	else:
		return False



def coll_rho1(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(200,175,250,175,225,(160-(radius+clearance)),p_x,p_y):
		return True
	else:
		return False

def coll_rho2(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(200,175,250,175,225,(190+(radius+clearance)),p_x,p_y):
		return True
	else:
		return False
def coll_rec1(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(95,170+(radius+clearance),95+int(10*math.cos(math.pi/3)),170-int(10*math.sin(math.pi/3))\
		,95-int(75*math.cos(math.pi/6)),170-int(75*math.sin(math.pi/6)),p_x,p_y):
		return True
	else:
		return False

def coll_rec2(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(95-int(75*math.cos(math.pi/6))+int(10*math.cos(math.pi/3)),170-int(75*math.sin(math.pi/6))-int(10*math.sin(math.pi/3))-(radius+clearance),95+int(10*math.cos(math.pi/3)),170-int(10*math.sin(math.pi/3))\
		,95-int(75*math.cos(math.pi/6)),170-int(75*math.sin(math.pi/6)),p_x,p_y):
		return True
	else:
		return False

def coll_poly1(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(20-(radius+clearance),80,50+(radius+clearance),50+(radius+clearance),25-(radius+clearance),15,p_x,p_y):
		return True
	else:
		return False
#
def coll_poly2(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(25-(radius+clearance),15,50+(radius+clearance),50+(radius+clearance),75,15-(radius+clearance),p_x,p_y):
		return True
	else:
		return False

def coll_poly3(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(75,15-(radius+clearance),50,50+(radius+clearance),75,80+(radius+clearance),p_x,p_y):
		return True
	else:
		return False

def coll_poly4(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(75,15-(radius+clearance),100+(radius+clearance),50,75,80+(radius+clearance),p_x,p_y):
		return True
	else:
		return False

def coll_check(position):
	if coll_rho1(position):
		return True
	elif coll_rho2(position):
		return True
	elif coll_poly1(position):
		return True
	elif coll_poly2(position):
		return True
	elif coll_poly3(position):
		return True
	elif coll_poly4(position):
		return True
	elif coll_circle(position):
		return True
	elif coll_ellipse(position):
		return True
	elif coll_rec1(position):
		return True
	elif coll_rec2(position):
		return True
	else:
		return False

def moveRight(position):
	p_x = position[0]
	p_y = position[1]
	if p_x<300 and not (coll_check(position)):
		updated_pos = [p_x+1,p_y]
		cost = 1
		return updated_pos,cost
	else:
		return None,None

def moveLeft(position):
	p_x = position[0]
	p_y = position[1]
	if p_x>0 and not (coll_check(position)):
		updated_pos = [p_x-1,p_y]
		cost = 1
		return updated_pos,cost
	else:
		return None,None

def moveUp(position):
	p_x = position[0]
	p_y = position[1]
	if p_y<200 and not (coll_check(position)):
		updated_pos = [p_x,p_y+1]
		cost = 1
		return updated_pos,cost
	else:
		return None,None

def moveDown(position):
	p_x = position[0]
	p_y = position[1]
	if p_y>0 and not (coll_check(position)):
		updated_pos = [p_x,p_y-1]
		cost = 1
		return updated_pos,cost
	else:
		return None,None

def moveUpRight(position):
	p_x = position[0]
	p_y = position[1]
	if p_y<200 and p_x<300 and not (coll_check(position)):
		updated_pos = [p_x+1,p_y+1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def moveDownRight(position):
	p_x = position[0]
	p_y = position[1]
	if p_y>0 and p_x<300 and not (coll_check(position)):
		updated_pos = [p_x+1,p_y-1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def moveUpLeft(position):
	p_x = position[0]
	p_y = position[1]
	if p_y<200 and p_x>0 and not (coll_check(position)):
		updated_pos = [p_x-1,p_y+1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def moveDownLeft(position):
	p_x = position[0]
	p_y = position[1]
	if p_y>0 and p_x>0 and not (coll_check(position)):
		updated_pos = [p_x-1,p_y-1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def mover(position,action):
    if action == 'right':
        [updated_pos,cost] = moveRight(postition)
    elif action == 'left':
        [updated_pos,cost] = moveLeft(position)
    elif action == 'up':
        [updated_pos,cost] = moveUp(postition)
    elif action == 'down':
        [updated_pos,cost] = moveDown(position)
    elif action == 'upRight':
        [updated_pos,cost] = moveUpRight(position)
    elif action == 'upLeft':
        [updated_pos,cost] = moveUpLeft(postition)
    elif action == 'downRight':
        [updated_pos,cost] = moveDownRight(position)
    elif action == 'downLeft':
        [updated_pos,cost] = moveDownLeft(position)
    return updated_pos,cost

def mappingofneighbors(current_position):
    neighbors=['right','left','up','down','upRight','upLeft','downRight','downLeft']

    active_points=[]
    for action in neighbors:
        new_pos,cost = mover(current_position,action)
        active_points.append((new_pos,cost))
    return active_points
#
'''
def dijkstra(map,start,goal):
    visited = {} #set of all points visited
    visited.add(start_point)
    nodes=[]
    nodes.append(start_point)
    Q=deque()
    Q.append(0)
    actual_costs=math.inf
    cost2come=0
    while Q:
        parent = Q.popleft()
        new_pos= nodes[parent]
        neighbor_list= mappingofneighbors(new_pos)
        for new in neighbors_list:
            point = new[0]
            cost  = new[1]
            if point not in visited:
                visited.add(point)
                nodes.append(point)
                Q.append(len(nodes)-1)
            if cost2come + cost < actual_costs:
                actual_costs= cost2come+cost
            if point == goal:
                break
'''
def priority_pop(queue):  # Priority Queue, outputs the node with least cost attached to it
    min_a = 0
    for elemt in range(len(queue)):
        if queue[elemt].cost < queue[min_a].cost:
            min_a = elemt
    return queue.pop(min_a)

def find_node(point, queue):
    for elem in queue:
        if elem.state == point:
            return queue.index(elem)
        else:
            return None

def track_back(node):
    print("Tracking Back")
    p = []
    p.append(node.parent)
    parent = node.parent
    if parent is None:
        return p
    while parent is not None:
        p.append(parent)
        parent = parent.parent
    return p

def color_pixel(image_color, point):
    #print(point)
    image_color[point[1], point[0]] = [255,0,255]
    return image_color

def plan_algo(start,goal,imap):
	visited = []
	s_node = Nodes(start)
	s_node.cost = 0
	Q = [s_node]
	imap[start[1], start[0]] = [255, 0, 0]
	imap[goal[1], goal[0]] = [0, 0, 255]
	while Q:
		current = priority_pop(Q)
		visited.append(current.state)
		neighbors = mappingofneighbors(current.state)

		for n in neighbors:
			if n[0] is not None:

				new_node = Nodes(n[0])
				#print(n[0])
				new_node.parent = current

				if n[0][0]==goal[0] and n[0][1]==goal[1]:
					print("Goal Reached")
					return new_node,imap
				#print(current.state)
				#imap = color_pixel(imap, current.state)
				#imap[start[1], start[0]] = [255, 0, 0]
				#imap[goal[1], goal[0]] = [0, 0, 255]

				#resized_new_1 = cv2.resize(imap, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
				#cv2.imshow("Figure", resized_new_1)
				#cv2.waitKey(1)

				if n[0] not in visited:
					#print("Here's Johnny")
					new_node.cost = n[1]+new_node.parent.cost
					visited.append(new_node.state)
					Q.append(new_node)
				else:
					node_id = find_node(new_node,Q)

					if node_id:
						t_node = queue[node_id]
						if t_node.cost> n[1]+new_node.parent.cost:
							t_node.cost= n[1]+new_node.parent.cost
							t_node.parent = current
			else:
				continue

	return None,None





def main():
	img = np.zeros((201,301,3), np.uint8)

	BLACK = (0,0,0)
	WHITE = (255,255,255)

	for i in range(201):
		for j in range(301):
			if coll_check([i,j]):
				img[i][j] = BLACK
			else:
				img[i][j] = WHITE


	# start = [start_x,start_y]
	# goal =  [goal_x,goal_y]
    start = [5,295]
	goal =  [295,5]
	result,image = plan_algo(start,goal,img)
	n_list = track_back(result)
	for elem in n_list:
		x = elem.state[1]
		y = elem.state[0]
		image[x, y] = [0, 255, 0]
		resized_new = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
		cv2.imshow("Figure", resized_new)
		cv2.waitKey(100)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	#cv2.imshow('Environment',img)
	#cv2.waitKey(0)
if __name__ == '__main__':
    print("Please Enter all the values as requested:")
    # start_x=int(input("Enter the starting x postition:"))
    # start_y=int(input("Enter the starting y position:"))
    # goal_x=int(input("Enter the goal x position:"))
    # goal_y=int(input("Enter the goal y position:"))
    # if start_x > 300 or goal_x > 300 or start_x < 0 or goal_x < 0:
    #     print("The X coordiantes should be within the limit [0-300]")
    #     exit()
    # if start_y > 300 or goal_y > 300 or start_y < 0 or goal_y < 0:
    #     print("The Y coordiantes should be within the limit [0-300]")
    #     exit()
    # start = [start_x,start_y]
	# goal =  [goal_x,goal_y]
    radius= int(input("Enter the radius of the robot:"))
    clearance=int(input("Enter the clearance: "))
    main()
