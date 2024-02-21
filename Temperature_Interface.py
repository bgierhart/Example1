#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:16:18 2024

@author: bengierhart
"""
import streamlit as st
import Temperature as t

st.title("Temperature Converter")
st.divider()

with st.sidebar:
    st.subheader("Temperature Scale")
    #radio buttons V
    scale = st.radio("What temperature scale?",
                     ["***F***", "***C***", "***K***"],
                     captions = ["The American Special", 
                                 "What the rest of the world uses",
                                 "Science, Baby!"])
    
st.write(scale)
    
    
#st.write(t.convert_fahrenheit(32.0))
#st.write(t.convert_celsius(0.0))
#st.write(t.convert_kelvin(271.0))

