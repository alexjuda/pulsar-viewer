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
