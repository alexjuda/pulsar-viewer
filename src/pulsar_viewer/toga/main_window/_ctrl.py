import toga

from ._vm import MainWindowVM


class MainWindowCtrl:
    def __init__(self, vm: MainWindowVM):
        self._vm = vm

        self._switch = toga.Switch(text="a switch")
        self._messages_view = toga.Label("Messages\nwill\nshow up here.")
        self._box = toga.Box(children=[self._switch, self._messages_view])

    @classmethod
    def standard(cls):
        return cls(vm=MainWindowVM.standard())

    @property
    def widget(self) -> toga.Widget:
        return self._box
