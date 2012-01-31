#!/usr/bin/env python

import sys
from Ska.DBI import DBI
from Chandra.Time import DateTime

dbh = DBI(dbi='sybase', server='sybase', user='aca_read')

t = DateTime()
if len(sys.argv) > 1:
    t = DateTime(sys.argv[1])
timeline = dbh.fetchone("""select * from timelines \
                           where datestart <= '%s'
                           and datestop > '%s'"""
                           % (t.date, t.date))
mp = '/data/mpcrit1/mplogs'
print "file://%s%s%s" % (mp, timeline['dir'], 'starcheck.html')
