# Lab — Bash pipeline
## Write `scripts/disk_report.sh`: uses `df`, filters root volume, prints CSV line to stdout; `chmod +x`; run from repo root; document usage in `scripts/README.md`.

This directory contains internal automation and monitoring utilities for the project.

### 1. Disk Utilization Reporter (`disk_report.sh`)

This script is built using strict shell execution standards (`set -euo pipefail`), ensuring that if any system command fails, the pipeline will terminate instantly rather than reporting false health metrics.

#### Output Format
The script prints a single line to `stdout` containing comma-separated values in the following schema:

#### Usage

Always execute this script from the **root of the repository**:

Check permissions of the file. Make sure to have execute permissions to the user

chmod +x scripts/disk_report.sh
```bash
./scripts/disk_report.sh