from typing import Protocol
from ._structs import Message


class MainWindowVM:
    """
    View Model for the main window.
    """

    class Delegate(Protocol):
        def prepend_messages(self, messages: list[Message]): ...

        def append_messages(self, messages: list[Message]): ...

    _delegate: Delegate | None = None

    @classmethod
    def standard(cls):
        return cls()

    def register_delegate(self, delegate: Delegate):
        self._delegate = delegate
