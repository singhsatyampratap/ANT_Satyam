#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:15:52 2019

@author: singhsatyampratap
"""

#main program
#flow of the code 

import obspy
import numpy as np
import matplotlib.pyplot as plt
#st=obspy.read('/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/CM09/BHZ/XB.CM09.02.BHZ__20060201T000000Z__20060202T000000Z.mseed')
#st+=obspy.read('/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/CM08/XB.CM08.02.BHN__20060201T000000Z__20060202T000000Z.mseed')
stack=np.zeros(7201)
for i in range(14,27):
    st=load_stream(i,i+1,2,'CM09')
    st+=load_stream(i,i+1,2,'CM25')
    print(st)
    st=process_one(st)
    print(st)
    #onebit normalisation and spectral whitening
    stp = st.copy()                            # copy stream
    for tr in stp:
        tr = normalize(tr)
        tr = whiten(tr, 0.1, 0.2)
#    freq, amp=spectral_analysis(tr)
#    
#st.plot()
#plt.plot(freq,abs(amp))
#plt.show()

    stack+=correlateNoise(stp, ['CM09','CM25'], 7200)
stack = stack / float((np.abs(stack).max()))   
plotStack(st,stack,500)

