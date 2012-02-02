#!/usr/bin/env python

import sys
from Ska.DBI import DBI
from Chandra.Time import DateTime
import numpy as np

dbh = DBI(dbi='sybase', server='sybase', user='aca_read')
mp = '/data/mpcrit1/mplogs'

t = DateTime()
if len(sys.argv) > 1:
    t = DateTime(sys.argv[1])
timelines = dbh.fetchall(
"""select * from timelines
   where datestart <= '%(date)s' and datestop > '%(date)s'"""
% {'date': t.date})

if not len(timelines):
    timelines = dbh.fetchall(
"""select * from timelines
   where ( datestart = (
       select max(datestart) from timelines where datestart < '%(date)s'))
    or ( datestart = (
       select min(datestart) from timelines where datestart > '%(date)s'))"""
% {'date': t.date})

for tdir in np.unique(timelines['dir']):
    print "file://%s%s%s" % (mp, tdir, 'starcheck.html')
