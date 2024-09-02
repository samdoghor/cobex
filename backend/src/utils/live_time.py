"""live_time.py

Keyword arguments:
argument -- description
Return: network_time
"""

from datetime import datetime, timezone

import ntplib


class NetworkTime:
    @staticmethod
    def network_time() -> datetime:
        try:
            client = ntplib.NTPClient()
            response = client.request('time.windows.com', version=3)
            network_time = datetime.fromtimestamp(
                response.tx_time, timezone.utc)
            return network_time
        except Exception:
            network_time = datetime.now(timezone.utc)
            return network_time
