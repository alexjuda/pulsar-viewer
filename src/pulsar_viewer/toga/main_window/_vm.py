from typing import Protocol
from ._structs import MessageRow


class MainWindowVM:
    """
    View Model for the main window.
    """

    class Delegate(Protocol):
        def prepend_rows(self, rows: list[MessageRow]): ...
        def append_rows(self, rows: list[MessageRow]): ...

    _delegate: Delegate | None = None
    # This will get removed soon. It's just to demo the refresh mechanics.
    _refresh_counter: int = 0

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

        assert self._delegate is not None
        self._delegate.prepend_rows(
            [
                MessageRow(
                    title=f"Refresh {self._refresh_counter}",
                    subtitle="This row was lazy loaded.",
                ),
            ]
        )
