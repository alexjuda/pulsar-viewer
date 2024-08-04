import asyncio
from unittest.mock import create_autospec

from pulsar_viewer.toga.main_window._vm import MainWindowVM
from pulsar_viewer.pulsar import PulsarPoller

from ._async_mocker import AsyncMocker, trigger_coro


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

        def _sleep_callback():
            vm._should_continue_polling = False

        sleep_mocker = AsyncMocker(asyncio, "sleep", on_await=_sleep_callback)

        with sleep_mocker:
            # When
            coro = vm.polling_loop()
            trigger_coro(coro)

        # Then
        delegate_spy.append_rows.assert_called_once()
