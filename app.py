from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # create db object
        self.dbo=Database()
        self.apio=API()


        self.root=Tk()
        self.root.title('NLPApp')
        self.root.geometry('350x600')
        self.root.configure(bg='#7DCEA0')

        self.login_gui()

        self.root.mainloop()


    def login_gui(self):

        self.clear()

        heading=Label(self.root,text='NlpApp',bg='#7DCEA0',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=25,show='*')
        self.password_input.pack(pady=(5, 10),ipady=4)

        login_btn=Button(self.root,text='Login',width=20,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(10, 10))

        redirect_btn=Button(self.root,text='Register Now',height=2,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            print(i.destroy())

    def perform_registration(self):
        # fetch data from gui
        name=self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration successful.You can login now ')
        else:
            messagebox.showerror('Error','Email already exists')
    def perform_login(self):

        email=self.email_input.get()
        password=self.password_input.get()

        response=self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','login suceessful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')

    def home_gui(self):

        self.clear()
        heading = Label(self.root, text='NlpApp', bg='#7DCEA0', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))


        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Name entity recognisations', width=30, height=4,
                               command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion predictions', width=30, height=4,
                               command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', height=2, command=self.login_gui)
        logout_btn.pack(pady=(10, 10))


    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='NlpApp', bg='#7DCEA0', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#7DCEA0', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20, 'bold'))

        label1 = Label(self.root, text='Enter the text ')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyse sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#7DCEA0',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        print(text)
        result=self.apio.sentiment_analysis(text)

        txt=''

        for i in result['sentiment']:
            txt=txt+i+' -> '+ str(result['sentiment'][i]) + '\n'


        self.sentiment_result['text']=txt


    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='NlpApp', bg='#7DCEA0', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Name entity  Analysis', bg='#7DCEA0', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20, 'bold'))

        label1 = Label(self.root, text='Enter the text ')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Analyse NER', command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='',bg='#7DCEA0',fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)
        print(result)


        self.ner_result['text']=result

    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NlpApp', bg='#7DCEA0', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Prediction', bg='#7DCEA0', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20, 'bold'))

        label1 = Label(self.root, text='Enter the text ')
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn= Button(self.root, text='Predictions', command=self.emotion_predictions)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='',bg='#7DCEA0',fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def emotion_predictions(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_prediction(text)
        print(result)


        self.emotion_result['text']=result




nlp=NLPApp()