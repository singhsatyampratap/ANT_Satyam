#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:54:33 2020

@author: singhsatyampratap
"""


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:57:00 2020

@author: singhsatyampratap
"""


''' This script rotate can be used to rotate the stream(BHN and BHZ) present within
a folder to radial and tranverse component. 
'''




from obspy.geodetics.base import gps2dist_azimuth
import os
import numpy as np
from obspy import read_inventory
class rotate_seed:
    """ This..
    ...
    ...
    ....
    .....
    ......
    .......
    """
    
    
    def __init__(self):
        #self.lat1=lat1
        #self.lon1=lon1
        #self.lat2=lat2
        #self.lon2=lon2
        self.result=0
        self.m=np.zeros([32,2])
    #def _str_(self):
    #    return '{}'.format
    def back_azimuth(self,lat1,lon1,lat2,lon2):
        
        self.result = gps2dist_azimuth(lat1, lon1, lat2, lon2)[2]
        return(self.result)
         
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
        return (self.m)














from obspy import read, read_inventory, Stream
import os





#inputs
path="/home/singhsatyampratap/internship/Code/IRIS/waveforms/CM*/"
year=2006
month_start=02
month_end=12
base_station='CM01'
network_name="XB"
station_names=['CM{:02}'.format(i)  for i in range(1,33)]
#can be enter manually like
#['XB.CM01', 'XB.CM02'....... ]







month_years=['{}-{:02}'.format(year,i)  for i in range(month_start,month_end+1) ]

station_nameBHN=['{}.{}.BHN.mseed'.format(network_name,station_name)  for station_name in station_names]
station_nameBHE=['{}.{}.BHE.mseed'.format(network_name,station_name)  for station_name in station_names]

lat_lon=rotate_seed().open_xml()
dict_st_latlon={station_names[i]:lat_lon[i,:] for i in range(32) }
lat1=dict_st_latlon[base_station][0]
lon1=dict_st_latlon[base_station][1]




i=0
#j=6
#creating the path name
for j in range(len(station_nameBHN)):
    pathBHN=os.path.join(path,'BHN',month_years[i],station_nameBHN[j])
    pathBHE=os.path.join(path,'BHE',month_years[i],station_nameBHE[j])


    #reading the stream data
    st = read(pathBHN)
    st+=read(pathBHE)


    #calculating backazimuth for rotation
    lat2=lat_lon[j,0]
    lon2=lat_lon[j,1]
    ba=rotate_seed().back_azimuth(lat1, lon1, lat2, lon2)

    #rotating the stream in the stream to radial and transverse component
    st.rotate(method="NE->RT", back_azimuth=ba)


    #saving the files as mseed 

    Stream(st[0]).write('XB.{}{}.BHT.mseed'.format(base_station,station_nameBHN[j]),format='MSEED')
    Stream(st[1]).write('XB.{}{}.BHR.mseed'.format(base_station,station_nameBHN[j]),format='MSEED')



        