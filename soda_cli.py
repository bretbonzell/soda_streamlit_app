from soda.scan import Scan
from datetime import timedelta
from functions import run_soda_scan
from datetime import datetime


default_args = {
    "owner": "soda_core",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

print(run_soda_scan("snowflake", "test_scan"))

