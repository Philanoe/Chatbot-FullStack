# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:47:14 2022

@author: Philanoe
-- FRONT --
Module aiming at communicating with the FastAPI app
"""

import requests

def QuestionAnswering(Question):
    
    API_url = 'http://127.0.0.1:8080/'
    parameters = {'question': Question}
    BackToFrond_Data = requests.get(API_url, params=parameters)
    #Answer = f'url : {BackToFrond_Data.url}, answer : {BackToFrond_Data.text}'
    Answer = BackToFrond_Data.json()['message']
     
        
    return Answer

