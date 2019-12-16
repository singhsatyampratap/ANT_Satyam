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
    if startdate<10:
        d='0'+str(startdate)
       
    else:
        d=str(startdate)
      
    if enddate<10:
        e='0'+str(enddate)
    else:
        e=str(enddate)
    
    
    
    
    
    
    if month<10:
        c='0'+str(month)
    else:
        c=str(month)
    stn = obspy.read('/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/'+station+'/BHZ/XB.'+station+'.02.BHZ__2006'+c+d+'T000000Z__2006'+c+e+'T000000Z.mseed')
#stn+=obspy.read('/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/CM09/BHN/XB.CM09.02.BHN__20060204T000000Z__20060205T000000Z.mseed')
   # tr=stn[0]
   # for i in range(startdate,enddate):
   #     if i<10:
   #         a='0'+str(i)
   #     else:
   #         a=str(i)
   #     if (i+1)<10:
   #         b='0'+str(i+1)
   #     else:
   #         b=str(i+1)
   #     loc='/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/'+station+'/BHN/XB.'+station+'.02.BHN__2006'+c+a+'T000000Z__2006'+c+b+'T000000Z.mseed'
    #print(loc)
    #    stn=obspy.read(loc)
    #    tr=tr+stn[0]
    #stn= Stream([tr])
    return stn
 
