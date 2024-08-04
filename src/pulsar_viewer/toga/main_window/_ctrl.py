from functools import cached_property

import toga

from ._vm import MainWindowVM


class MainWindowCtrl:
    def __init__(self, vm: MainWindowVM):
        self._vm = vm

    @classmethod
    def standard(cls):
        return cls(vm=MainWindowVM.standard())

    @cached_property
    def widget(self) -> toga.Widget:
        return toga.Label("Hello, world!")
