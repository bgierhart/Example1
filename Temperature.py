#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:16:18 2024

@author: bengierhart
"""
import streamlit as st

st.title("Temperature Converter")
def convert_fahrenheit(temperature):
    F2C = (float(temperature)-32)/1/8
    F2K = (5/9)*(float(temperature)-32)+273.15
    return F2C, F2K

def convert_celsius(temperature):
    C2F = (1.8*temperature)+32
    C2K = float(temperature)+273.15
    return C2F, C2K

def convert_kelvin(temperature):
    K2F = (9/5)*(float(temperature)-273)+32
    K2C = float(temperature)-273.15
    return K2F, K2C