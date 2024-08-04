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
        mock_sleep = AsyncMock()

        with patch.object(asyncio, "sleep", mock_sleep):
            # Given
            poller_mock = create_autospec(PulsarPoller)
            delegate_spy = create_autospec(MainWindowVM.Delegate)
            vm = MainWindowVM(poller=poller_mock)
            vm.register_delegate(delegate_spy)

            def _stop_loop(*args, **kwargs):
                vm._should_continue_polling = False

            mock_sleep.side_effect = _stop_loop

            # When
            coro = vm.polling_loop()
            try:
                coro.send(None)
            except StopIteration:
                pass

            # Then
            delegate_spy.append_rows.assert_called_once()
