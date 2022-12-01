# CFP Calendar

[![CFP_calendar_nightly](https://github.com/leo8a/cfp_events/actions/workflows/nightly.yml/badge.svg)](https://github.com/leo8a/cfp_events/actions/workflows/nightly.yml)

This is a _very_ simple and fragile scraper that creates an iCalendar file to watch CFP of some conferences.

## Subscribe to calendar

To subscribe to this calendar you could follow the "Use a link to add a public calendar" option from this [Google support article](https://support.google.com/calendar/answer/37100?hl=en&co=GENIE.Platform%3DDesktop).

Basically, it boils down to the following steps:
1. On your computer, open [Google Calendar](https://calendar.google.com/).
2. On the left, next to `Other calendars` click `Add +` other calendars and then `From URL`.
3. Enter this [calendar's address](https://raw.githubusercontent.com/leo8a/cfp_events/main/assets/cfp_calendar.ics).
4. Click `Add calendar`. The calendar appears on the left, under `Other calendars`.
5. (Optional) You may customize the name of the new calendar as well as other params.

> **Important Notes:**
>   - The first time the calendar is loaded, the events appear almost instantaneously in your personal calendar. 
>   - After that first loading, Google Calendar might take up to 12 hours to show new changes (or events) in your calendar again.

## Add events manually

If you feel conformable with [RFC-5546](https://www.rfc-editor.org/rfc/rfc5546) and want to write your own events, you may use the `extra` folder to drop custom `*.ics` files manually. These files will be merged to the [generated iCalendar](assets/cfp_calendar.ics) nightly.