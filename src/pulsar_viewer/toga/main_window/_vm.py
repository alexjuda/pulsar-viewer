import asyncio
from typing import Protocol

from ._structs import MessageRow
from ...pulsar import PulsarPoller


class MainWindowVM:
    """
    View Model for the main window. Doesn't directly depend on `toga`.
    """

    class Delegate(Protocol):
        def prepend_rows(self, rows: list[MessageRow]): ...
        def append_rows(self, rows: list[MessageRow]): ...

    _delegate: Delegate | None = None
    # This will get removed soon. It's just to demo the refresh mechanics.
    _refresh_counter: int = 0
    # This will get removed soon. It's just to demo the polling mechanics.
    _poll_counter: int = 0

    # Allows breaking the loop during testing.
    _should_continue_polling: bool = True

    def __init__(self, poller: PulsarPoller):
        self._poller = poller

    @classmethod
    def standard(cls):
        return cls(
            # TODO: figure out how to configure these
            poller=PulsarPoller(
                pulsar_url="pulsar://localhost:6650",
                topic_fq="persistent://public/default/hello1",
            )
        )

    def register_delegate(self, delegate: Delegate):
        self._delegate = delegate

    @property
    def initial_rows(self) -> list[MessageRow]:
        messages = self._poller.read_new_batch()

        return [
            MessageRow(title="Message X", subtitle=msg.payload.decode())
            for msg in messages
        ]

    def on_refresh(self):
        self._refresh_counter += 1

        if delegate := self._delegate:
            delegate.prepend_rows(
                [
                    MessageRow(
                        title=f"Refresh {self._refresh_counter}",
                        subtitle="This row was lazy loaded.",
                    ),
                ]
            )

    async def polling_loop(self):
        while self._should_continue_polling:
            if self._delegate is None:
                continue

            new_batch = self._poller.read_new_batch()
            new_rows = [
                MessageRow(
                    title="Added message",
                    subtitle=msg.payload.decode(),
                )
                for msg in new_batch
            ]
            self._delegate.append_rows(new_rows)

            await asyncio.sleep(1)
