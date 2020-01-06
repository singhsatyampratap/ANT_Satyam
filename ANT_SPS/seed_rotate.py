#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:50:16 2020

@author: singhsatyampratap
"""

from obspy.geodetics.base import gps2dist_azimuth
class rotate_seed:
    """ This..
    ...
    ...
    ....
    .....
    ......
    .......
    """
    
    
    def __init__(self,lat1,lon1,lat2,lon2):
        self.lat1=lat1
        self.lon1=lon1
        self.lat2=lat2
        self.lon2=lon2
        self.result=0
    #def _str_(self):
    #    return '{}'.format
    def back_azimuth(self):
        
        self.result = gps2dist_azimuth(self.lat1, self.lon1, self.lat2, self.lon2)[2]
        return(self.result)
    
    
    def rotate_NEtoRT(self):
        
        pathname="/home/singhsatyampratap/internship/Code/ANT_Python/seismic-noise-tomography-master/Data Folder/station/"
        for i in range(0,32):
            stn='CM{:02}'.format(i+1)
            staname='XB.{}.xml'.format(stn)
            #print(staname)
            loc=os.path.join(pathname,staname)
            inv=read_inventory(loc)
            #m[i,0]=stn
            self.m[i,0]=inv[0][0][0].latitude
            self.m[i,1]=inv[0][0][0].longitude
            
        st.rotate(method="NE->RT",back_azimuth=self.result, inventory=inv)  
                  
     'NE->RT'
        
        
import os
import numpy as np
from obspy import read_inventory
 
class latlon_mat:
    """
    ...
    ....
    .....
    ......
    .......
    """
    def __init__(self):
        self.m=np.zeros([32,2])
        
        
    def open_xml(self):
        pathname="/home/singhsatyampratap/internship/Code/ANT_Python/seismic-noise-tomography-master/Data Folder/station/"
        for i in range(0,32):
            stn='CM{:02}'.format(i+1)
            staname='XB.{}.xml'.format(stn)
            #print(staname)
            loc=os.path.join(pathname,staname)
            inv=read_inventory(loc)
            #m[i,0]=stn
            self.m[i,0]=inv[0][0][0].latitude
            self.m[i,1]=inv[0][0][0].longitude
        return m
    
    
        








import obspy
from obspy import read, read_inventory, Stream

st = read("/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/BHE/2006-02/XB.CM01.BHE.mseed")
st += read("/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/BHN/2006-02/XB.CM01.BHN.mseed")
#inv = read_inventory("/home/singhsatyampratap/internship/Code/ANT_Python/seismic-noise-tomography-master/Data Folder/station/XB.CM01.xml")
st.rotate(method="NE->RT", back_azimuth=185.44)
Stream(st[0]).write('XB.CM01.BHT.mseed',format='MSEED')
Stream(st[1]).write('XB.CM01.BHR.mseed',format='MSEED')




def rotates(s1,trN,trE):
    




        
        