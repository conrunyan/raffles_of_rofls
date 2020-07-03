#!/bin/bash
set -x

if [ -d "$1" ]; then
    python manage.py test $1
else
    python manage.py test ./raffle_backend/tests/
fi