#!/bin/sh
#
# MCL Clinical Data
# =================
#
#
# Database maintenance. This assumes that PostgreSQL commands are on the PATH.



dropdb --if-exists clinical_data
dropuser --if-exists mcl

createuser \
    --createdb \
    --inherit \
    --login \
    --no-createrole \
    --no-superuser \
    mcl


createdb --encoding=UTF8 --owner=mcl clinical_data
