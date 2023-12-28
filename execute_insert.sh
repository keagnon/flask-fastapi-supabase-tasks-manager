#!/bin/bash

psql -U . -d . -h . -W -a -f insert_data.sql
