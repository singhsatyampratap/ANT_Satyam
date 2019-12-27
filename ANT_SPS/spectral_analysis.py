#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 00:08:56 2019

@author: singhsatyampratap
"""
import obspy
import numpy as np
import matplotlib.pyplot as plt  
#amplitude spectrum plot
def spectrum_show(st,fig_name):
    st.taper(0.01)
    st.resample(1.0)
    dat=st[0].data
    samp = len(dat)                                # number of sample point
    delta = st[0].stats.delta                             
   

  
    # FFT data into frequency-domain
    Fdat = np.fft.rfft(dat, n=samp)
    
    # x-axis in f-domain for plotting
    xf = np.linspace(0.0, 1.0/(2.0*delta), (samp/2)+1)
    
    # plot
    
    plt.title('Frequency Domain')
    plt.plot(xf, 2.0/samp * np.abs(Fdat), color='b',label="no Taper",linewidth=1.5)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    plt.ylim([0,20])
    plt.figure(figsize=(20,5))
    plt.savefig('.png')
    plt.show()
    return xf, Fdat   
