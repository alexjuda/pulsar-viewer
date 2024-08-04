from functools import cached_property

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

    @cached_property
    def data_source(self) -> toga.sources.ListSource:
        return toga.sources.ListSource(
            accessors=MessageRow._fields,
            data=self._vm.initial_rows,
        )

    @property
    def widget(self) -> toga.Widget:
        messages_view = toga.DetailedList(
            data=self.data_source,
            on_refresh=self._on_refresh,
        )

        return messages_view

    def _on_refresh(self, widget: toga.DetailedList, **kwargs):
        self._vm.on_refresh()

    def prepend_rows(self, rows: list[MessageRow]):
        for row in rows[::-1]:
            self.data_source.insert(0, row)

    def append_rows(self, rows: list[MessageRow]): ...
