import toga
import toga.style

from ._vm import MainWindowVM


class MainWindowCtrl:
    def __init__(self, vm: MainWindowVM):
        self._vm = vm

        switch = toga.Switch(text="Show full message")
        # Wrapping the switch in a box makes the control and the label clumped
        # together instead of stretched to till the container.
        switch_box = toga.Box(children=[switch])

        messages_view = toga.Label("Messages\nwill\nshow up here.")
        message_details_view = toga.Label("This will contain\nthe message at its full length.")
        split = toga.SplitContainer(content=(messages_view, message_details_view))

        self._box = toga.Box(
            children=[switch_box, split],
            style=toga.style.Pack(direction="column"),
        )

    @classmethod
    def standard(cls):
        return cls(vm=MainWindowVM.standard())

    @property
    def widget(self) -> toga.Widget:
        return self._box
