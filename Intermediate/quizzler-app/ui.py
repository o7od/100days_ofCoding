from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # this is the window
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Image variables
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
    
        # Creating a canvas
        self.canvas = None
        self.canvas_id = self.create_canvas()

        # Creating button
        self.left_button = None
        self.right_button = None
        self.create_buttons()

        # Display score
        self.score = Label(text="Score: 0", font=("Arial", 15, "bold"), bg=THEME_COLOR)
        self.score.grid(row=0, column=1, sticky="e")    

        self.get_next_question()

    # Check the true answer
    def check_answer(self, user_answer):
        # if the answer is correct
        if self.quiz.check_answer(user_answer):
            # we flash a green light
            self.canvas.config(bg="green")
        # otherwise a red light
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        self.update_score()


    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}")

    def create_canvas(self):
        self.canvas = Canvas(self.window, width=300, height=250, highlightthickness=0, bd=0, bg="white")
        canvas_id = self.canvas.create_text(150, 125, text="Hello World", font=("Arial", 15, "italic"), width=200, justify="center", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        return canvas_id
    
    def create_buttons(self):
        self.left_button = Button(
                                image=self.true_img,
                                bd=0,
                                command=lambda: self.check_answer("true"))
        self.left_button.grid(row=2, column=0, pady=20)
        self.right_button = Button(
                                image=self.false_img,
                                bd=0,
                                command=lambda: self.check_answer("false"))
        self.right_button.grid(row=2, column=1, pady=20)
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_id, text=next_q)
        else:
            self.canvas.itemconfig(self.canvas_id, text="You've reached the end of the quiz.")
            self.left_button.config(state="disabled")
            self.right_button.config(state="disabled")