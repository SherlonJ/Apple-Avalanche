import turtle as trtl
import leaderboard as lb
import random 

#-----setup-----
fruit_image = "apple.gif" # Store the file name of your shape
background_image = "tree.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(fruit_image) # Make the screen aware of the new file

apples_turtles = []
letter_turtle= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#scores and name
leaderboard_file_name = 'bruh.txt'
score= 0
name = trtl.textinput("Player Name", "What is your name?")
#----Timer count_down----
timer_writer = trtl.Turtle()
timer_writer.penup()
timer_writer.goto(-150, 150)
timer_writer.hideturtle()
time_remaining = 15
counter_interval = 1000
#---score counter---
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(250, 100)
text_style = ("Arial", 24, "italic")
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_fruit(active_fruit):
  active_fruit.shape(fruit_image)
  wn.update()

count = 0
while count < 10:
  appleturtle = trtl.Turtle()
  apples_turtles.append(appleturtle)
  draw_fruit(appleturtle)
  x = random.randint(-100, 200)
  y = random.randint(-50, 100)
  appleturtle.penup() 
  appleturtle.goto(x, y)
  appleturtle.left(90)
  appleturtle.write(letter_turtle[count])
  print(appleturtle)
  count = count + 1


def something_a():
  print("apple a was dropped")
  apples_turtles[0].backward(200)
  update_score()
def something_b():
  print("apple b was dropped")
  apples_turtles[1].backward(200)
  update_score()
def something_c():
  print("apple c was dropped")
  apples_turtles[2].backward(200)
  update_score()
def something_d():
  print("apple d was dropped")
  apples_turtles[3].backward(200)
  update_score()
def something_e():
  print("apple e was dropped")
  apples_turtles[4].backward(200)
  update_score()
def something_f():
  print("apple f was dropped")
  apples_turtles[5].backward(200)
  update_score()

def something_g():
  print("apple g was dropped")
  apples_turtles[6].backward(200)
  update_score()
def something_h():
  print("apple h was dropped")
  apples_turtles[7].backward(200)

def something_i():
  print("apple i was dropped")
  apples_turtles[8].backward(200)
  update_score()
def something_j():
  print("apple b was dropped")
  apples_turtles[9].backward(200)
  update_score()
def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=text_style)
def manage_highscores():
    global score, name
    print("Game has ended.")
    lb.load_leaderboard(leaderboard_file_name)
    lb.update_leaderboard(score, name)
    lb.draw_leaderboard(appleturtle, text_style)

def countdown():
    global time_remaining
    time_remaining = time_remaining - 1
    if time_remaining > 0:
        timer_writer.clear()
        timer_writer.write("Timer: " + str(time_remaining), font=text_style)
        wn = trtl.Screen()
        wn.ontimer(countdown, counter_interval)
    else:
        timer_writer.clear()
        timer_writer.write("Time is up!!!.", font=text_style)
        manage_highscores()

def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=text_style)
#-----function calls-----
print("We did it yay")
wn.bgpic(background_image)
wn.onkeypress(something_a, "a")
wn.onkeypress(something_b, "b")
wn.onkeypress(something_c, "c")
wn.onkeypress(something_d, "d")
wn.onkeypress(something_e, "e")
wn.onkeypress(something_f, "f")
wn.onkeypress(something_g, "g")
wn.onkeypress(something_h, "h")
wn.onkeypress(something_i, "i")
wn.onkeypress(something_j, "j")
wn.listen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()

bruh = []

count = 0

while count < 2:
   new = trtl.Turtle
   bruh.append(new)
   
