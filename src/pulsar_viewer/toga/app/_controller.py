import toga


class AppController:
    def startup(self, app: toga.App, **kwargs) -> toga.Widget:
        """
        Matches `toga.app.AppStartupMethod`. Returns content of the main window.
        """
        return toga.Label("Hello, world!")
