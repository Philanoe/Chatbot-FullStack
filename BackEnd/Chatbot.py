# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
Functions for the Multi-context question answering chatbot
"""

def Init():
    import os
    #import transformers
    #model = 'sfs'

def Classifier(Question):
    return "Ubuntu"

def LoadContext(Label):
    if(Label == "sldkfjsfd"):
        Context = "sdfsdf"
    elif(Label == "sldkfjsfd"):
        Context == "sdfsdfx"
    return Context

def ContextBasedQuestionAnswering(Question, Context):
    Answer = "sdfsdf"
    return Answer

def QuestionAnswering(Question):
    Label = Classifier(Question)
    Context = LoadContext(Label)
    Answer = ContextBasedQuestionAnswering(Question, Context)
    
    return Answer

