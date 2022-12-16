#!/usr/bin/env bash

git diff assets/cfp_calendar.ics > /tmp/diffs

if [ -s /tmp/diffs ]; then
  echo "assets_changed=true" >> "$GITHUB_OUTPUT"
else
  echo "assets_changed=false" >> "$GITHUB_OUTPUT"
fi
