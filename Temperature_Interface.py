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
    
#st.write(scale)
prompt = f'Enter the temperature in {scale}.'
freezing = False

if scale=="***F***":
    tempF = st.number_input(prompt, step=1.0, value=32.0)
    C, K = t.convert_fahrenheit(tempF)
    st.metric('Temperature C\u00b0', f'{C:.2f}')
    st.metric('Kelvins', f'{K:.2f}')
    if tempF<32.0:
        freezing=True
elif scale=="***C***":
    tempC = st.number_input(prompt, step=1.0, value=0.0)
    F, K = t.convert_celsius(tempC)
    st.metric('Temperature F\u00b0', f'{F:.2f}')
    st.metric('Kelvins', f'{K:.2f}')
    if tempC<0.0:
        freezing=True
else:
    tempK = st.number_input(prompt, step=1.0, value=273.15)
    C, F = t.convert_kelvin(tempK)
    st.metric('Temperature C\u00b0', f'{C:.2f}')
    st.metric('Temperature F\u00b0', f'{F:.2f}')
    if tempK<273.15:
        freezing=True
    
if freezing:
    st.snow()
    freezing=False
#st.write(t.convert_fahrenheit(32.0))
#st.write(t.convert_celsius(0.0))
#st.write(t.convert_kelvin(271.0))

