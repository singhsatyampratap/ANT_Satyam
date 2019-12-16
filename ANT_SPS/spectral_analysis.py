#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:31:04 2019

@author: singhsatyampratap
"""

""" This portion of the code is useful to perform spectral analysis and spectrogram """

import obspy
import numpy as np
def spectral_analysis(tr):
    nsamp = tr.stats.sampling_rate                              # sampling rate
    fNy = nsamp / 2.0                          # Nyquist frequency
    y=tr.data
    y_f = np.fft.rfft(y)                    # transform all 3 signals into frequency domain 
    freq = np.linspace(0, fNy, len(y_f))    # frequency axis for plotting
    return freq, y_f


