import toga

from .app import AppCtrl


def main():
    app_controller = AppCtrl.standard()
    app = toga.App(
        formal_name="Pulsar Viewer",
        app_id="com.alexjuda.pulsarviewer",
        startup=app_controller.startup,
    )

    for task in app_controller.background_tasks:
        app.add_background_task(task)

    app.main_loop()


if __name__ == "__main__":
    main()
