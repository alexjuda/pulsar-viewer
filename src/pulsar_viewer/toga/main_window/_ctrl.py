import toga
import toga.style

from ._vm import MainWindowVM


class MainWindowCtrl:
    def __init__(self, vm: MainWindowVM):
        self._vm = vm

        switch = toga.Switch(text="Show full message", on_change=self._on_switch_change)
        # Wrapping the switch in a box makes the control and the label clumped
        # together instead of stretched to till the container.
        self._switch_box = toga.Box(children=[switch])

        self._messages_view = toga.Label("Messages\nwill\nshow up here.")
        self._message_details_view = toga.Label("This will contain\nthe message at its full length.")
        self._split = toga.SplitContainer(content=(self._messages_view, self._message_details_view))

        self._box = toga.Box(
            children=[self._switch_box, self._split],
            style=toga.style.Pack(direction="column"),
        )

    @classmethod
    def standard(cls):
        return cls(vm=MainWindowVM.standard())

    @property
    def widget(self) -> toga.Widget:
        self._box = toga.Box(
            children=[self._switch_box, self._split],
            style=toga.style.Pack(direction="column"),
        )
        return self._box

    def _on_switch_change(self, switch: toga.Switch, **kwargs):
        self._box.clear()

        if switch.value:
            self._box.add(self._switch_box, self._split)
        else:
            self._box.add(self._switch_box, self._messages_view)

