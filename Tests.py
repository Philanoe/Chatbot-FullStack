# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
Tests for the Multi-context question answering chatbot

Ask a question Q
    Question = UserInput()
Find the label
    Label = Classifier(Question)
Get the context data related to this label
    Context = GetContext(Label)
Get the answer from the context data
    Answer = QuestionAnswering(Question, Context)
Answer the user
    AnswerUser(Answer)
"""

import Chatbot as chat
import StreamlitPage as app

def MainTestFunction():
    app.InitStreamLitPage()
    Question = app.UserInput()
    
def TestStreamLit():
    app.InitStreamLitPage()
    Question = app.UserInput()
    app.AnswerUser(Question)

def test():
    print("test")

def TestInput():
    return input("please enter a question : ")

#def TestStreamLit():
    

if __name__ == '__main__':
    #print("start of the test program")
    #test()
    #MyInput = TestInput()
    #print(f'\nYour question was :  {MyInput}\n')
    TestStreamLit()
    #print("end of the test program")
