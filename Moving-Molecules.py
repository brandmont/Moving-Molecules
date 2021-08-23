import turtle
import random

wn = turtle.Screen()
wn.setup(1400, 900)
wn.bgcolor("black")
wn.title("Moving Molecules")
wn.tracer(0)
wn.register_shape("Molecule1.gif")
wn.register_shape("Molecule2.gif")
wn.register_shape("Molecule3.gif")
wn.register_shape("Molecule4.gif")
wn.register_shape("Molecule5.gif")
wn.register_shape("Molecule6.gif")
wn.register_shape("Molecule7.gif")
wn.register_shape("Molecule8.gif")
wn.register_shape("Molecule9.gif")
wn.register_shape("Molecule10.gif")
wn.register_shape("Molecule11.gif")
wn.register_shape("Molecule12.gif")
wn.register_shape("Molecule12.gif")
wn.register_shape("Molecule13.gif")
wn.register_shape("Molecule14.gif")
wn.register_shape("Molecule15.gif")
wn.register_shape("Molecule16.gif")
wn.register_shape("Molecule17.gif")
wn.register_shape("Molecule18.gif")
wn.register_shape("Molecule19.gif")
wn.register_shape("Molecule20.gif")
wn.register_shape("Molecule21.gif")
wn.register_shape("Molecule22.gif")
wn.register_shape("Molecule23.gif")
wn.register_shape("Molecule24.gif")
wn.register_shape("Molecule25.gif")

balls = []

for _ in range(14):
    balls.append(turtle.Turtle())
    
    #colors = ["red", "seashell", "blue", "green yellow", "hot pink", "gray", "yellow", "orange", "green", "white", "purple", "cyan"]
    objects = ["Molecule1.gif","Molecule2.gif","Molecule3.gif","Molecule4.gif","Molecule5.gif","Molecule6.gif","Molecule7.gif","Molecule8.gif","Molecule9.gif","Molecule10.gif","Molecule11.gif","Molecule12.gif","Molecule13.gif","Molecule14.gif","Molecule15.gif","Molecule16.gif","Molecule17.gif","Molecule18.gif","Molecule19.gif","Molecule20.gif","Molecule21.gif","Molecule22.gif","Molecule23.gif","Molecule24.gif","Molecule25.gif"]
    #objects = ["Molecule1.gif","Molecule2.gif","Molecule3.gif","Molecule4.gif","Molecule5.gif","Molecule6.gif","Molecule7.gif","Molecule8.gif","Molecule9.gif","Molecule10.gif","Molecule11.gif","Molecule12.gif","Molecule13.gif","Molecule14.gif"]

for ball in balls:
    #ball.shape(random.choice(["circle", "square", "triangle"]))
    #ball.color(random.choice(colors))
    B = random.choice(objects)
    ball.shape(B)
    objects.remove(B)
    ball.penup()
    ball.speed(1)
        #ball.turtlesize(2)
        #ball.write("1")
    x = random.randint(-680, 680)
    y = random.randint(-380, 380)
    ball.goto(x, y)
    ball.dy = random.choice([-.6, -.5, -.4, -.3, -.2, .6, .5, .4, .3, .2,])
    ball.dx = random.choice([-.6, -.5, -.4, -.3, -.2, .6, .5, .4, .3, .2,])


#gravity = 0.1

while True:
    wn.update()
    #ball.dy -= gravity
    
    for ball in balls:
        ball.sety(ball.ycor() + ball.dy)
    
        ball.setx(ball.xcor() + ball.dx)
    
    #Check Wall
        if ball.xcor() > 675:
            ball.dx *= -1
        
        if ball.xcor() < -675:
            ball.dx *= -1
    
    #Check Bounce
        if ball.ycor() < -425:
            ball.dy *= -1

        if ball.ycor() > 425:
            ball.dy *= -1

    #check for collisions
        for i in range(0, len(balls)):
            for j in range(i+1, len(balls)):
                #check for collision
                if balls[i].distance(balls[j]) <50:
                    temp_dx = balls[i].dx
                    temp_dy = balls[i].dy
                    
                    balls[i].dx = balls[j].dx
                    balls[i].dy = balls[j].dy
                    
                    balls[j].dx = temp_dx
                    balls[j].dy = temp_dy
                    
                    





wn.mainloop()