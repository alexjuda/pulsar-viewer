from unittest.mock import create_autospec, patch, AsyncMock
from pulsar_viewer.toga.main_window._vm import MainWindowVM
from pulsar_viewer.pulsar import PulsarPoller
import asyncio


class TestMainWindowVM:
    @staticmethod
    def test_factory():
        vm = MainWindowVM.standard()

        assert vm is not None
        assert vm._delegate is None
        assert isinstance(vm._poller, PulsarPoller)

    @staticmethod
    def test_polling_loop():
        # Given
        poller_mock = create_autospec(PulsarPoller)
        vm = MainWindowVM(poller=poller_mock)

        delegate_spy = create_autospec(MainWindowVM.Delegate)
        vm.register_delegate(delegate_spy)

        with patch.object(asyncio, "sleep", AsyncMock()) as mock_sleep:

            def _await_sleep_callback(*args, **kwargs):
                vm._should_continue_polling = False

            mock_sleep.side_effect = _await_sleep_callback

            # When
            coro = vm.polling_loop()
            try:
                coro.send(None)
            except StopIteration:
                pass

        # Then
        delegate_spy.append_rows.assert_called_once()
