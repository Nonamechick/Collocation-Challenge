from tkinter import *

# define question dictionary
question = {
	"A temporary, low level job": ['Doing an internship', 'Black work', 'Do Low-level job as driver of garbage truck ', 'Who know?'],
	"A job that does not require much skill or experience": ['Work for dummies', 'Entry-level job', 'Dream job'],
	"The mininum salary required by law": ['The minimum salary', 'Coins', 'The minimum wage', 'Entry-level job salary'],
	"A good team player": ['You cooperate well with your co-workers', 'You play in group very well', 'You feel cosy in group ', 'I do not know'],
	"Get a promotion":['Get an increase in responsibility', 'Became more famous', 'Get extry money'],
	"Get a raise": ['Raise a hand', 'Show off','Get an increase in responsibility',' Get an increase in salary'],
	" Be fired/dismissed ": ['Lose your job', 'Lose a hope', 'To be a broke'],
	"A heavy workload" : ['A lot of work','Complex work','A boring work','God,please help me'],
	"Work overtime": ['Typicall Japanase workers','Work extra hours','Work till you die','Work more than 5 hours'],
	"Demanding job ": ['Dream job','an intense job with lots of responsibilities','Just a job which you must do ','I do not know'],
	"Quit your job": ['Lose a job', 'To be a broken totally','leave your job voluntarily','look for another job'],
	"Competitive salary": ['salary that is higher than average','Average salary','Low income'],
	"Generous benefits": ['extra benefits like health insurance, discounts, a company car, etc','bonus from company','Extra money'],
	"Job seekers": ['people looking for a job', 'people hunt for a job','people fight for a job '],
	"Earn a living": ['Earn to survive', 'Earn for food','get enough money to survive'],
	" A dream job": ['a job that would be perfect for you','A job which you can see in dreams','Unreal job','A job where salary higher than average']
	}
# define answer list
ans = ['Doing an internship', 'Entry-level job', 'The minimum wage', 'You cooperate well with your co-workers', 'Get an increase in responsibility',' Get an increase in salary','Lose your job','A lot of work','Work extra hours','an intense job with lots of responsibilities','leave your job voluntarily','salary that is higher than average','extra benefits like health insurance, discounts, a company car, etc','people looking for a job','get enough money to survive','a job that would be perfect for you']

current_question = 0


def start_quiz():
	start_button.forget()
	next_button.pack()
	next_question()


def next_question():
	global current_question
	if current_question < len(question):
		# get key or question that need to be printed
		check_ans()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		# clear frame to update its content
		clear_frame()
		# printing question
		Label(f1, text=f"Question : {c_question}", padx=30,
			font="calibre 30 normal").pack(anchor=NW)
		# printing options
		for option in question[c_question]:
			Radiobutton(f1, text=option, variable=user_ans,
						value=option, padx=600, indicatoron=0). pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"Your Score is {user_score.get()} out of {len(question)}"
		Label(f1, text=output, font="calibre 50 bold").pack()
		Label(f1, text="Thanks for Participating",
			font="calibre 40 bold").pack()


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


if __name__ == "__main__":
	root = Tk()
	# setup basic window
	root.title("GFG QUIZ APP")
	root.geometry("850x850")
	root.minsize(800, 800)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="Quiz App about collocations", 
		font="calibre 50 bold",
		relief=SUNKEN, background="green", 
		padx=20, pady=20).pack()
	Label(root, text="", font="calibre 20 bold").pack()
	start_button = Button(root, 
						text="Start Quiz,Good Luck!",
						command=start_quiz, 
						font="calibre 30 bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Question",
						command=next_question, 
						font="calibre 30 bold")

	root.mainloop()
#Quiz APP about collocations Pre-Alpha.0.01 version