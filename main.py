#!/usr/bin/env python

import os
import glob
import pytz

import requests
from bs4 import BeautifulSoup

from datetime import datetime
from dateutil.parser import parse

from icalendar import Calendar, Event, vCalAddress, vText

TIMEZONE = pytz.timezone("Europe/Madrid")
LF_UPCOMING_EVENTS = "https://events.linuxfoundation.org/about/calendar/"

DICT_EVENTS = []


def scrape_lf_upcoming_events(_soup):
    for event in _soup.find_all("article", {"class": "cell medium-6 large-4 callout large-margin-bottom"}):
        event_info = event.getText('\t', '\n').split('\t')

        if event_info[-1] in ['Closed',         # don't waste cpu cycles
                              'No Call for Proposals',
                              'Details Coming Soon']:
            continue

        DICT_EVENTS.append(
            {'name': event_info[0],
             'date': event_info[1],
             'location': event_info[2].strip(' and'),
             'cfp': event_info[-1],
             'url': event.find(href=True)['href'],
             'organizer': "Linux Foundation"}
        )


def create_icalendar():  # https://learnpython.com/blog/working-with-icalendar-with-python/
    cal = Calendar()

    # Some properties are required to be compliant
    cal.add('version', '2.0')
    cal.add('prodid', '<CFP Calendar>')

    for _event in DICT_EVENTS:
        deadline = parse(' '.join(_event['cfp'].rsplit()[-3:]))

        # Add subcomponents
        event = Event()
        event.add('summary', _event['name'])
        event.add('description', _event['url'])

        # Add date parameters
        event.add('dtstamp', datetime(deadline.year, deadline.month, deadline.day, 0, 0, 0, tzinfo=TIMEZONE))
        event.add('dtstart', datetime(deadline.year, deadline.month, deadline.day, 0, 0, 0, tzinfo=TIMEZONE))
        event.add('dtend', datetime(deadline.year, deadline.month, deadline.day, 23, 59, 59, tzinfo=TIMEZONE))

        # Add the organizer
        organizer = vCalAddress('MAILTO:events@linuxfoundation.org')
        organizer.params['name'] = vText('Linux Foundation')

        # Add parameters of the event
        event['organizer'] = organizer
        event['location'] = _event['location']

        # Add the event to the calendar
        cal.add_component(event)

    # Add events defined in extras
    for filename in glob.glob('extras/*.ics'):
        ecal = Calendar.from_ical(open(filename, 'rb').read())
        cal.add_component(ecal)

    # Write to disk
    f = open(os.path.join("./assets", 'cfp_calendar.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()


if __name__ == '__main__':
    r = requests.get(url=LF_UPCOMING_EVENTS)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.body.prettify())

    # scrape events
    scrape_lf_upcoming_events(soup)

    # create iCalendar
    create_icalendar()

    for lf_event in DICT_EVENTS:
        print(lf_event['date'], ':  ',
              lf_event['name'], '  -->  ',
              lf_event['cfp'], '   @',
              lf_event['location'])
