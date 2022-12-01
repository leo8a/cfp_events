#!/usr/bin/env bash

git diff assets/cfp_calendar.ics > /tmp/diffs ; [ -s /tmp/diffs ]

if [ $? == '0' ]; then
  echo "::set-output name=assets_changed::true"
else
  echo "::set-output name=assets_changed::false"
fi
