import pgzrun

TITLE = "Quiz game"
WIDTH = 870
HEIGHT = 650

Title_box = Rect(0,0,880,80)
Question_box = Rect(0,0,650,150)
Timer_box = Rect(0,0,150,150)
Ans_box1 = Rect(0,0,300,150)
Ans_box2 = Rect(0,0,300,150)
Ans_box3 = Rect(0,0,300,150)
Ans_box4 = Rect(0,0,300,150)
Skip_box = Rect(0,0,350,330)

score = 0
time_left = 10
question_file_name = "question.txt"
title_message = ""
is_game_over = False

answer_boxes = [answer_box1answer_box2,answer_box3,answer_box4]
Questions = []
Question_count = 0
Question_index = 0

Title_box.move_ip(0,0)
Question_box.move_ip(20,100)
Timer_box.move_ip(700,100)
Ans_box1.move_ip(20,270)
Ans_box2.move_ip(370,270)
Ans_box3.move_ip(20,450)
Ans_box4.move_ip(370,450)
Skip_box.move_ip(700,270)

def draw():
    glodal title_message
    screen.clear()
    screen.fill(color="white")
    screen.draw.filled_rect(Title_box,"white")
    screen.draw.filled_rect(Question_box,"dark yellow")
    screen.draw.filled_rect(Timer_box,"orange")
    screen.draw.filled_rect(Skip_box,"yellow")

    for answer_box in answer_boxes :
        screen.draw.filled_rect(answer_box,"dark yellow")

    title_message = "Welcome to Quiz game !   "
    title_message = title_message + f"You're on question {Question_index} of {Question_count}"

    screen.draw.textbox(title_message,Title_box,color = "black")
    screen.draw.textbox(
        str(time_left),Timer_box,
        color = "black",shadow = (0.5,0.5),
        scolor = "gray"
    )
    screen.draw.textbox(
        "Skip",skip_box,
        color = "black",angle = 90
    )
    screen.draw.textbox(
        question[0].strip(),Question_box,
        color = "black",shadow = (0.5,0.5),
        scolor = "gray"
    )

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color = "black")
        index = index + 1

def update():
    move_title()

def move_title():
    Title_box.x = Title_box.x - 2
    if title_box.right < 0 :
        Title_box.left = WIDTH

def read_question_file():
    global Question_count,Questions
    q_file = open(question_file_name,"r")
    for question in q_file :
        Questions.append(question)
        Question_count = Question_count + 1
    q_file.close()

def read_next_question():
    global Question_index
    Question_index = Question_index + 1
    return questions.pop(0.split(","))
