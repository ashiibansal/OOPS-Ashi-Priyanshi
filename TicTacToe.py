from tkinter import *
from tkinter import messagebox

def ButtonClick(button):
    global x_o, flag
    if button["text"] == "" and x_o:
        button["text"] = "X"
        x_o = False
        CheckForWin()
        flag += 1
    elif button["text"] == "" and not x_o:
        button["text"] = "O"
        x_o = True
        CheckForWin()
        flag += 1
    else:
        messagebox.showinfo("Tic Tac Toe", "Player has already Entered!")

def CheckForWin():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global player_x_score, player_o_score, flag
    
    # Check for Player X win
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        messagebox.showinfo("Tic Tac Toe", "Player X Won!")
        player_x_score += 1
        UpdateScore()
        ResetBoard()

    # Check for Player O win
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        messagebox.showinfo("Tic Tac Toe", "Player O Won!")
        player_o_score += 1
        UpdateScore()
        ResetBoard()

    # Check for a draw
    elif flag == 8:
        messagebox.showinfo("Tic Tac Toe", "Game Tied!")
        ResetBoard()

def UpdateScore():
    """Update the score display on the GUI."""
    score_label.config(text=f"Player X: {player_x_score} | Player O: {player_o_score}")

def ResetBoard():
    """Reset the game board for a new round."""
    global flag, x_o
    button1["text"] = ""
    button2["text"] = ""
    button3["text"] = ""
    button4["text"] = ""
    button5["text"] = ""
    button6["text"] = ""
    button7["text"] = ""
    button8["text"] = ""
    button9["text"] = ""
    flag = 0
    x_o = True

# Main application window
main = Tk()
main.title("Tic Tac Toe")

x_o = True
flag = 0
player_x_score = 0
player_o_score = 0

# Create buttons for the Tic Tac Toe grid
button1 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button1))
button1.grid(row=1, column=0)
button2 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button2))
button2.grid(row=1, column=1)
button3 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button3))
button3.grid(row=1, column=2)
button4 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button4))
button4.grid(row=2, column=0)
button5 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button5))
button5.grid(row=2, column=1)
button6 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button6))
button6.grid(row=2, column=2)
button7 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button7))
button7.grid(row=3, column=0)
button8 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button8))
button8.grid(row=3, column=1)
button9 = Button(main, text="", font=("arial", 30, "bold"), bg="white", fg="blue", width=5, height=2, command=lambda: ButtonClick(button9))
button9.grid(row=3, column=2)

# Score display
score_label = Label(main, text="Player X: 0 | Player O: 0", font=("arial", 20, "bold"), fg="green")
score_label.grid(row=0, column=0, columnspan=3)

main.mainloop()
