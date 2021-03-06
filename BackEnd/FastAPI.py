# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- BACK --
Functions for the Multi-context question answering chatbot
"""
from fastapi import FastAPI
import Chatbot

app = FastAPI()

@app.get("/")
# use async when you do not need to wait for any answer to run the code
async def root():
    return {"message": "Hello World"}

@app.get("/question/")
def EmptyQuestion():
    answer = "Empty Question !"
    return {"question" : "", "answer" : answer}

@app.get("/question/{question_from_frontend}")
def GET_Model_Question_Answering2(question_from_frontend):
    answer = f'Your question {question_from_frontend} was quite interesting !'
    question = question_from_frontend
    return {"question" : question, "answer" : answer}