# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
Multi-context question answering chatbot

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

import ChatbotFunctions as chat
import StreamlitPage as app

app.InitStreamLitPage()
Question = app.UserInput()
Label = chat.Classifier(Question)
Answer = chat.QuestionAnswering(Question, Label)
app.AnswerUser(Answer)


