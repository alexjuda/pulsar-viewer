import toga
import toga.style

from ._vm import MainWindowVM
from ._structs import Message


class MainWindowCtrl:
    def __init__(self, vm: MainWindowVM):
        self._vm = vm

    @classmethod
    def standard(cls):
        vm = MainWindowVM.standard()
        ctrl = cls(vm=vm)
        vm.register_delegate(ctrl)
        return ctrl

    @property
    def widget(self) -> toga.Widget:
        messages_view = toga.Label("Messages\nwill\nshow up here.")
        return messages_view

    def prepend_messages(self, messages: list[Message]): ...

    def append_messages(self, messages: list[Message]): ...
