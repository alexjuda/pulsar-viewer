from ._msg import Message


class PulsarPoller:
    def __init__(self, pulsar_url: str, topic_fq: str):
        self._pulsar_url = pulsar_url
        self._topic_fq = topic_fq

    def read_new_batch(self) -> list[Message] | None:
        ...
        return None
