import toga

from ._app_controller import AppController


def main():
    app_controller = AppController()
    app = toga.App(
        formal_name="Pulsar Viewer",
        app_id="com.alexjuda.pulsarviewer",
        startup=app_controller.startup,
    )
    app.main_loop()


if __name__ == "__main__":
    main()
