# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
Streamlit Functions for the Multi-context question answering chatbot
"""

import streamlit as st

def InitStreamLitPage():
    st.set_page_config(page_title="ChatBot", page_icon="🍂")
    #st.image("")
    st.title("Multi-context question answering chatbot")
    st.write("by JingPan and Philanoe")
    st.write("---")
    
def UserInput():
    return st.text_input()