from tkinter import *

HEME_COLOR = "#375362"

class QuizUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("True/False Quiz")
        self.window.minsize(width=700, height=700)
        self.window.config(bg="#06327E")

        #self.score_text = Label(text = "Score: 0", fg = "white", bg = "#06327E")
        #self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(self.window, width=600, height=600, bg = "white")
        self.qtext = self.canvas.create_text(300, 300, text = "some question text", fill = "black")
        #self.canvas.grid(row = 1, column = 0, columnspan = 2)


        #self.question_bg = PhotoImage(file="images/Question.png")
        #self.card_image = self.canvas.create_image(300, 300, image = self.question_bg)
        self.window.mainloop()
