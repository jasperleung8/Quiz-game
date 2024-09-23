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
