
from tkinter import *
import tkinter.messagebox as tkMessageBox

root = Tk()
root.geometry("320x550")
root.title("Tic Tac Toe")

root.resizable(0,0)

fram1= Frame(root) 
fram1.pack()
titleLabel1=Label(fram1,text="Tic Tac Toe" , font=("Arial",26), bg="blue",width=16)
titleLabel1.grid(row=0,column=0 )

optionalFrame= Frame(root,bg="grey")
optionalFrame.pack()



frame2=Frame(root,bg="lightblue")
frame2.pack()

board = { 1:" ",2:" ",3:" ",
          4:" ",5:" ",6:" ",
          7:" ",8:" ",9:" " }


turn = "X"
game_end=False
mode="singlePlayer"

def changemodeToSinglePlayer():
    global mode
    mode= "singlePlayer"
    SinglePlayer["bg"]="lightgreen"
    multiPlayer['bg']="lightgrey"
    restartgame()
    tkMessageBox.showinfo(message="Switched To Single Player")

def changemodeToMultiplayer():
    global mode
    mode= "multiPlayer"
    multiPlayer['bg']="lightgreen"
    SinglePlayer["bg"]="lightgrey"
    restartgame()
    tkMessageBox.showinfo(message="Switched To Multi Player")


def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"]=board[key]

    
def checkforwin(player):
    # all rows
    if board[1]==board[2] and board[1]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    # all Columns 
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    # diagonals
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True
    else:
        return False

def checkfordraw():
    for i in board.keys():
        if board[i]==" ":
            return False 
    return True
            
def restartgame(): 
    global game_end
    game_end=False
    for button in buttons:
        button['text']=" "

    for i in board.keys():
        board[i]=" "

    titleLabel1=Label(fram1,text="Tic Tac Toe" , font=("Arial",26), bg="blue", width=15)
    titleLabel1.grid(row=0,column=0)

def minimax(board,ismaximize):
    if checkforwin("O"):
        return 1
    
    if checkforwin("X"):
        return -1
    
    if checkfordraw():
        return 0

    if ismaximize:
        bestScore = -100   
        for keys in board.keys():
            if(board[keys]== " "):
                board[keys]="O"
                score=minimax(board,False)  
                board[keys]=" "
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
     
        for keys in board.keys():
            if(board[keys]== " "):
                board[keys]="X"
                score=minimax(board,True)  
                board[keys]=" "
                if score < bestScore:
                    bestScore = score

        return bestScore 

def playComputer():
    bestScore = -100
    bestMove =0
     
    for keys in board.keys():
        if(board[keys]== " "):
            board[keys]="O"
            score=minimax(board,False)  
            board[keys]=" "
            if score > bestScore:
                bestScore = score
                bestMove= keys

    board[bestMove]= "O"

def play(event):
    global turn,game_end
    if game_end :
        return
   
    button=event.widget

    buttontext =str(button)
    clicked= buttontext[-1]
    # print(clicked)

    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    # print(clicked)

    if button['text']==" ":
        if turn == "X":
            board[clicked]=turn
            if checkforwin(turn):
                winningLabel=Label(fram1,text=f"{turn} wins the game ",bg="blue",font=("Arial",26),width=16)
                winningLabel.grid(row=0,column=0,columnspan=3)
                game_end=True
                tkMessageBox.showinfo(message=f"{turn} wins the game ")
            turn = "O"
            updateBoard() 
            if mode=="singlePlayer":
                playComputer()
                if checkforwin(turn):
                    winningLabel=Label(fram1,text="Computer wins the game",bg="blue",font=("Arial",26),width=16)
                    winningLabel.grid(row=0,column=0,columnspan=3)
                    game_end=True
                    tkMessageBox.showinfo(message="Computer wins the game")

                turn="X"
                updateBoard()
        else:
            board[clicked]=turn
            updateBoard()
            if checkforwin(turn):
                winningLabel=Label(fram1,text=f"{turn} wins the game ", bg="blue",font=("Arial",26),width=16)
                winningLabel.grid(row=0,column=0,columnspan=3)
                game_end=True
                tkMessageBox.showinfo(message=f"{turn} wins the game ")
            turn = "X"
        
        if checkfordraw():
            drawLabel=Label(fram1,text="Game draw", bg="blue",font=("Arial",26),width=16)
            drawLabel.grid(row=0,column=0,columnspan=3)
            tkMessageBox.showinfo(message="Game draw")

# UI Design 
# change mode options
SinglePlayer = Button(optionalFrame,text="SinglePlayer",width=13,height=1,font=("Arial",15),bg="lightgreen",relief=RAISED,borderwidth=5,command=changemodeToSinglePlayer)
SinglePlayer.grid(row=0,column=0,columnspan=1,sticky=NW)

multiPlayer = Button(optionalFrame,text="Multiplayer",width=13,height=1,font=("Arial",15),bg="lightgrey",relief=RAISED,borderwidth=5,command=changemodeToMultiplayer)
multiPlayer.grid(row=0,column=1,columnspan=1,sticky=NW)

# Tic Tac Toe Board

# 1st row
button1=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button1.grid(row= 0,column=0)
button1.bind("<Button-1>",play )

button2=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button2.grid(row= 0,column=1)
button2.bind("<Button-1>",play )

button3=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button3.grid(row= 0,column=2)
button3.bind("<Button-1>",play )

# 2nd row
button4=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button4.grid(row= 1,column=0)
button4.bind("<Button-1>",play )

button5=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button5.grid(row= 1,column=1)
button5.bind("<Button-1>",play )

button6=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button6.grid(row= 1,column=2)
button6.bind("<Button-1>",play )

# 3rd row 
button7=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button7.grid(row= 2,column=0)
button7.bind("<Button-1>",play )

button8=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button8.grid(row= 2,column=1)
button8.bind("<Button-1>",play )

button9=Button(frame2,text=" ",width=4,height=2 ,font=("Arial",30),bg="lightblue",relief=RAISED,borderwidth=5)
button9.grid(row= 2,column=2)
button9.bind("<Button-1>",play )

# Restart-Button
restartbutton = Button(frame2,text="Restart-Game",width=19,height=1,font=("Arial",20),bg="lightgreen",relief=RAISED,borderwidth=5,command=restartgame)
restartbutton.grid(row=4,column=0,columnspan=3)

buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()