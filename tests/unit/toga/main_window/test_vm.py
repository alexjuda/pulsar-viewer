from pulsar_viewer.toga.main_window._vm import MainWindowVM
from pulsar_viewer.pulsar import PulsarPoller


class TestMainWindowVM:
    @staticmethod
    def test_factory():
        vm = MainWindowVM.standard()

        assert vm is not None
        assert vm._delegate is None
        assert isinstance(vm._poller, PulsarPoller)
