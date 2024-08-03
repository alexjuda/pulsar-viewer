from datetime import datetime, timezone
from pulsar_viewer.pulsar import PulsarPoller


def _current_timestamp() -> int:
    return int(datetime.now(tz=timezone.utc).timestamp())


class TestReadNewBatch:
    @staticmethod
    def test_with_empty_topic():
        timestamp = _current_timestamp()
        topic = f"persistent://tests/integration/test1-{timestamp}"

        poller = PulsarPoller(
            pulsar_url="pulsar://localhost:8080",
            topic_fq=topic,
        )
        batch = poller.read_new_batch()
        assert batch is None
