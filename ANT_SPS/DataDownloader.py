#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:02:14 2019

@author: singhsatyampratap
"""
"""
this part of the code can be used to download the data from IRIS network"""

import obspy
from obspy.clients.fdsn.mass_downloader import RectangularDomain, \
    Restrictions, MassDownloader

# Rectangular domain containing parts of Cameron.
domain = RectangularDomain(minlatitude=2.3355, maxlatitude=7.0136,
                           minlongitude=9.0251, maxlongitude=12.1289)

restrictions = Restrictions(
    # Get data for a whole year.
    starttime=obspy.UTCDateTime(2006, 2, 1),
    endtime=obspy.UTCDateTime(2007, 2, 1),
    # Chunk it to have one file per day.
    chunklength_in_sec=86400,
    network="XB", station="CM", location="02",
    # The typical use case for such a data set are noise correlations where
    # gaps are dealt with at a later stage.
    reject_channels_with_gaps=False,
    # Same is true with the minimum length. All data might be useful.
    minimum_length=0.0,
    # Guard against the same station having different names.
    minimum_interstation_distance_in_m=100.0)

# Restrict the number of providers if you know which serve the desired
# data. If in doubt just don't specify - then all providers will be
# queried.
mdl = MassDownloader()
mdl.download(domain, restrictions, mseed_storage="waveforms",
             stationxml_storage="stations")

 