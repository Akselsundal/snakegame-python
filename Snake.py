from Joint import*

class Snake(Joint):


    def __init__(self):
        self.head = Joint(BOARD_LENGTH/2,  BOARD_LENGTH/2)
        self.joint1 = Joint(BOARD_LENGTH/2,  BOARD_LENGTH/2-1)
        self.joint2 = Joint(BOARD_LENGTH/2,  BOARD_LENGTH/2-2)
        self.dir = "s"
        self.eat_fruit = False

        self.skeleton = [self.head, self.joint1, self.joint2]

    def set_speed(self, hardness, speed, points): #Calculating speed as a function of points
        if (points%5) == 0 and speed > 100:
            speed -= 10 #Framerate decreases with 10 every 5 points
        return(speed)


    def move_snake(self, dir):
            self.dir = dir
            self.old_head = self.skeleton[0]
            self.new_head = Joint(self.old_head.x_pos + self.old_head.find_dir(dir)[0],
                                  self.old_head.y_pos + self.old_head.find_dir(dir)[1])
            self.skeleton.insert(0, self.new_head)

            if self.eat_fruit == True:
                self.eat_fruit = False

            else:
                self.skeleton.pop()




    def draw_snake(self, surface):
        for joint in self.skeleton:
            joint.draw_joint(surface)
