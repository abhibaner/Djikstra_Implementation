import numpy as np 
import matplotlib.pyplot as plt
import cv2


class Nodes:    
    def __init__(self,state,parent,cost):
        self.state = state
        self.cost = cost
        self.parent = parent

def coll_circle(position):
	p_x = position[1]
	p_y = position[0]
	location = np.sqrt((p_x -225)**2+(p_y -50)**2) - 25
	if location < 0:
		return True
	else:
		return False 

def coll_ellipse(position):
	p_x = position[1]
	p_y = position[0]
	center = [150,100]
	location = ((float(p_x)-150)**2/40**2) + ((float(p_y)-100)**2/20**2) -1.0
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
	if isInside(200,175,250,175,225,160,p_x,p_y):
		return True
	else:
		return False

def coll_rho2(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(200,175,250,175,225,190,p_x,p_y):
		return True
	else:
		return False

def coll_poly1(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(20,80,50,50,25,15,p_x,p_y):
		return True
	else:
		return False

def coll_poly2(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(25,15,50,50,75,15,p_x,p_y):
		return True
	else:
		return False

def coll_poly3(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(75,15,50,50,75,80,p_x,p_y):
		return True
	else:
		return False

def coll_poly4(position):
	p_x = position[1]
	p_y = position[0]
	if isInside(75,15,100,50,75,80,p_x,p_y):
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
		updated_pos = [p_x,p_y-1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def moveUpLeft(position):
	p_x = position[0]
	p_y = position[1]
	if p_y<200 and p_x>0 and not (coll_check(position)):
		updated_pos = [p_x,p_y-1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def moveDownLeft(position):
	p_x = position[0]
	p_y = position[1]
	if p_y>0 and p_x>0 and not (coll_check(position)):
		updated_pos = [p_x,p_y-1]
		cost = math.sqrt(2)
		return updated_pos,cost
	else:
		return None,None

def main():
	img = np.zeros((200,300,3), np.uint8)

	BLUE = (255,0,0)
	GREEN = (0,255,0)
	
	for i in range(200):
		for j in range(300):
			if coll_check([i,j]):
				img[i][j] = BLUE
			else:
				img[i][j] = GREEN
			

	plt.imshow(img)
	plt.show()
	#cv2.imshow('Environment',img)
	#cv2.waitKey(0)


if __name__ == '__main__':
    main() 


