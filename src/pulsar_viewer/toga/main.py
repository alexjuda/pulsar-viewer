import toga

from .app import AppCtrl


def main():
    app_controller = AppCtrl.standard()
    app = toga.App(
        formal_name="Pulsar Viewer",
        app_id="com.alexjuda.pulsarviewer",
        startup=app_controller.startup,
    )
    app.main_loop()


if __name__ == "__main__":
    main()
