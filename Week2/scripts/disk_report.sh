#!/bin/bash

set -euo pipefail

df -h | awk '
BEGIN {OFS=","}
{print $1, $2, $3, $4, $5, $6}
'
> disk_usage.csv
