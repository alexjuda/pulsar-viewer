import pulsar
from ._msg import Message
from functools import cached_property


class PulsarPoller:
    def __init__(self, pulsar_url: str, topic_fq: str):
        self._pulsar_url = pulsar_url
        self._topic_fq = topic_fq

    @property
    def pulsar_url(self) -> str:
        return self._pulsar_url

    @property
    def topic_fq(self) -> str:
        return self._topic_fq

    @cached_property
    def client(self):
        return pulsar.Client(service_url=self._pulsar_url)

    @cached_property
    def reader(self):
        return self.client.create_reader(
            topic=self._topic_fq,
            start_message_id=pulsar.MessageId.earliest,
        )

    def close(self):
        self.reader.close()

    # 1 millisecond
    TIMEOUT_IMMEDIATELY = 1

    def read_new_batch(self) -> list[Message]:
        msgs = []
        while True:
            try:
                pulsar_message = self.reader.read_next(
                    timeout_millis=self.TIMEOUT_IMMEDIATELY
                )
            except pulsar.Timeout:
                break
            msg = Message(payload=pulsar_message.data())
            msgs.append(msg)

        return msgs
