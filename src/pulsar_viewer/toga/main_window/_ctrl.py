import toga
import toga.sources
import toga.style

from ._vm import MainWindowVM
from ._structs import MessageRow


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
        data_source = toga.sources.ListSource(
            accessors=MessageRow._fields,
            data=self._vm.initial_rows,
        )
        messages_view = toga.DetailedList(data=data_source)

        return messages_view

    def prepend_rows(self, rows: list[MessageRow]): ...

    def append_rows(self, rows: list[MessageRow]): ...
