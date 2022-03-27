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

@app.get("/{question_from_frontend}")
def GET_Model_Question_Answering(question_from_frontend: str):
    answer = "hello the world"
    question = question_from_frontend
    
    return {"answer" : answer, "question" : question}

#@app.post("/question")
#def POST_Model_Question_Answering(data: question_from_frontend):
#    answer = "hello the world"
#    question = question_from_frontend
#    
#    return {"answer" : answer, "question" : question}