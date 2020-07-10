W = 800
H = 600

#flappy bird constants
JUMPPOWER = 15
GRAVITY = 1

#pipe constants
GAP_H = H/2
GAP_W = W/16
SPEED = 3.5

class FlappyBird(object):
    def __init__(self):
        self.x = width/10
        self.y = height/2
        self.xvelocity = 0
        self.yvelocity = 0
        self.img = loadImage("bird.jpg")
        self.jump = False
        
    def update(self):
        if self.jump == True:
            self.yvelocity -= GRAVITY
            self.y -= self.yvelocity
        if self.y > height-20:
            self.y = height-20
            self.jump = False
        
    def draw(self):
        image(self.img, self.x, self.y, 50,50)


class Pipe(object):
    def __init__(self, x, y):
        #these x and y coords are the top left corner of the gap
        self.x = x
        self.y = y
        
    def update(self):
        self.x -= SPEED
    
    def draw(self):
        fill(0,255,0)
        
        #draw top pipe (X, Y, width, height)
        rect(self.x, 0, GAP_W, self.y)
        
        #draw bottom pipe (X, Y, width, height)
        rect(self.x, self.y + GAP_H, GAP_W, height - self.y - GAP_H)
    
def check_collision(bird, pipe):
    global gameover
    #check if bird is within x boundaries of pipe
    if pipe.x < bird.x and bird.x < pipe.x+GAP_W:
        #check if bird not within the y boundaries of gap
        if pipe.y > bird.y or pipe.y+GAP_H < bird.y:
            gameover = True

def setup():
    size(W,H)
    global flappybird, pipes, gameover, score
    flappybird = FlappyBird()
    pipes = []
    gameover = False
    score = 0
    
def draw():
    global flappybird, pipes, gameover, score
    background(0)
    if gameover == False:
        fill("#ffffff")
        textSize(36)
        text("Score:"+str(score), 50,50)
        flappybird.update()
        flappybird.draw()
        if random(100) > 99:
            pipes.append(Pipe(width, random(100,300)))
        for pipe in pipes:
            pipe.draw()
            pipe.update()
            check_collision(flappybird, pipe)
            if pipe.x + GAP_W < 0:
                score += 1
                pipes.remove(pipe)
    else:
        textSize(48)
        text("Game Over", 50,100)
        text("Press DOWN to play again", 50, 250)
    
def keyPressed():
    global pipes, gameover
    if key == CODED:
        if keyCode == UP:
            flappybird.jump = True
            flappybird.yvelocity = JUMPPOWER
        if keyCode == DOWN:
            pipes = []
            gameover = False
