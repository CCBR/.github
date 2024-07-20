#!/bin/bash

set -exo pipefail

MDPATH="assets/make_readme"
python ${MDPATH}/get_recent_releases_table.py 