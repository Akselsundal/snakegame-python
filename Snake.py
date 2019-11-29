from Joint import*

class Snake(Joint):


    def __init__(self): #Making 3 joints, setting bool var eatfruit
        self.head = Joint(BOARD_LENGTH/2,  BOARD_LENGTH/2)
        self.joint1 = Joint(BOARD_LENGTH/2,  BOARD_LENGTH/2-1)
        self.joint2 = Joint(BOARD_LENGTH/2,  BOARD_LENGTH/2-2)
        self.eat_fruit = False

        self.skeleton = [self.head, self.joint1, self.joint2]

    def set_speed(self, hardness, speed, points): #Calculating speed as a function of points
        if (points%5) == 0 and speed > 100:
            speed -= 10 #Framerate decreases with 10 every 5 points
        return(speed)


    def move_snake(self, dir):
            old_head = self.skeleton[0] #Old head, with ols position
            #Making new head by adding x- and y-pos and multiplying with dir(see Joint)
            new_head = Joint(old_head.x_pos + old_head.find_dir(dir)[0],
                                  old_head.y_pos + old_head.find_dir(dir)[1])

            self.skeleton.insert(0, new_head) #Inserting new head

            if self.eat_fruit == False: #If it didnt eat I want it to remove last element in list
                self.skeleton.pop()




#Draws the snake joint for joint
    def draw_snake(self, surface):
        for joint in self.skeleton:
            joint.draw_joint(surface)
