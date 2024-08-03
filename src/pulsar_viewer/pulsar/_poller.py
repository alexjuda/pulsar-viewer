import pulsar
from ._msg import Message
from functools import cached_property


class PulsarPoller:
    def __init__(self, pulsar_url: str, topic_fq: str):
        self._pulsar_url = pulsar_url
        self._topic_fq = topic_fq

    @cached_property
    def client(self):
        return pulsar.Client(service_url=self._pulsar_url)

    @cached_property
    def reader(self):
        return self.client.create_reader(
            topic=self._topic_fq,
            start_message_id=pulsar.MessageId.earliest,
        )

    TIMEOUT_IMMEDIATELY = 0

    def read_new_batch(self) -> list[Message] | None:
        msgs = []
        while True:
            try:
                msg = self.reader.read_next(timeout_millis=1000)
            except pulsar.Timeout:
                break
            msgs.append(msg)

        if msgs:
            return msgs
        else:
            return None
