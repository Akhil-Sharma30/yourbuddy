from polygon import RESTClient
import requests
from typing import cast
from urllib3 import HTTPResponse
import json
import typing
from typing import List

client = RESTClient(api_key="kpifpRjhP433rt_sqL5G6HYC3ho7JMmZ")

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        'APPL',
        1,
        'day',
        '2022-09-01',
        '2023-09-19',
        raw=True
    ),
)

aggs1 = client.get_aggs(
    ticker='APPL',
    multiplier=1,
    timespan='day',
    from_='2022-09-01',
    to='2023-09-19',
    # raw=True
)
print(aggs1.data)
# data = json.loads(aggs.data)
# print(data)
