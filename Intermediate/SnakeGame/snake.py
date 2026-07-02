from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        s = Turtle()
        s.color("white")
        s.shape("square")
        s.penup()
        s.goto(position)
        self.segments.append(s)
    

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def contact_with_tail(self):
        for segs in self.segments[1:]:
            if self.head.distance(segs) < 15:
                return True
        return False
    
    
    def up(self):
        if int(self.head.heading()) == DOWN:
            pass
        else:
            self.head.setheading(UP)
    
    def down(self):
        # if the current head is facing north, we don't change the heading direction to down
        if int(self.head.heading()) == UP:
            pass
        else:
            self.head.setheading(DOWN)
    
    def left(self):
        if int(self.head.heading()) == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)
    
    def right(self):
        if int(self.head.heading()) == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)
    
