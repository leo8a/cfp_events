#!/usr/bin/env bash

set -xe

sed -i '1p;/BEGIN:VCALENDAR/d' assets/cfp_calendar.ics
sed -i '2p;/VERSION:2.0/d' assets/cfp_calendar.ics
sed -i '3p;/PRODID:<CFP Calendar>/d' assets/cfp_calendar.ics

sed -i '$p;/END:VCALENDAR/d' assets/cfp_calendar.ics
