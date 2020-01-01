#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 23:56:13 2019

@author: singhsatyampratap
"""

from obspy import read
from obspy import Stream
def load_stream(startdate,enddate,month,station):
   
#importing the cameron downloaded data
#february month data
 
    d='{}'.format(startdate)
       
    e='{}'.format(enddate)
  
    c='{}'.format(month)
    stn = obspy.read('/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/'+station+'/BHZ/XB.'+station+'.02.BHZ__2006'+c+d+'T000000Z__2006'+c+e+'T000000Z.mseed')

    return stn
 
