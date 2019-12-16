#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:17:41 2019

@author: singhsatyampratap
"""

#processing 1
#run this code nto do the initial processing.
"""
this code is basically created to work on the segement data data for faster processing
The processing flow is as follow: 
       Rotation to the great circle
     1.The horizontal and he vertical component are rotate to Radial and transverse component.
     2. Trend and mean correction
     3. 5-point,zero phase band pass Butterworth filter 
            Input the period here (1-7s)
     4. Downsample to N Hertz
""" 
import obspy
def process_one(st):
    st.detrend('linear')                                            # remove trends using detrend
    st.taper(max_percentage=0.05, type='cosine')                    # taper the edges
    st.filter('bandpass', freqmin=0.1, freqmax=0.2, zerophase=True) # filter data of all traces in the streams
    st.resample(1.0)
    return st
    

