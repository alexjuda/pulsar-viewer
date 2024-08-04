import asyncio
from typing import Protocol
from ._structs import MessageRow


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

    @classmethod
    def standard(cls):
        return cls()

    def register_delegate(self, delegate: Delegate):
        self._delegate = delegate

    @property
    def initial_rows(self) -> list[MessageRow]:
        return [
            MessageRow(title="A Title 1", subtitle="This is a subtitle."),
            MessageRow(title="A Title 2", subtitle="This is a subtitle."),
            MessageRow(title="A Title 3", subtitle="This is a subtitle."),
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
        while True:
            self._poll_counter += 1
            if delegate := self._delegate:
                delegate.append_rows(
                    [
                        MessageRow(
                            title=f"Poll number {self._poll_counter}",
                            subtitle="This row was dynamically added.",
                        ),
                    ]
                )

            await asyncio.sleep(1)
