from Joint import*

class Snake(Joint):


    def __init__(self):
        self.head = Joint(200,200)
        self.joint1 = Joint(300,290)
        self.joint2 = Joint(300,280)

        self.joint1.move_joint("s")
        self.joint2.move_joint("s")
        self.joint2.move_joint("s")


        self.skeleton = [self.head, self.joint1, self.joint2]


    def move_snake(self, dir):
        self.temp_joint(0,0) = self.skeleton[0]
        for i in range(len(self.skeleton)-1, 0, -1):
            self.skeleton[i] = self.skeleton[i-1]
        self.skeleton[0].move_joint(dir)



    def draw_snake(self, surface):
        for joint in self.skeleton:
            joint.draw_joint(surface)
