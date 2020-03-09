import notify2
from dbus.mainloop.glib import DBusGMainLoop
from piXnotify.OSNotifiers.AbstractNotifier import AbstractNotifier


class LinuxNotifier(AbstractNotifier):
    def __init__(self):
        my_native_main_loop = DBusGMainLoop(set_as_default=True)
        super().__init__()
        notify2.init("piXnotify", mainloop=my_native_main_loop)

    def _notify(self):
        args = {"message": self.message}
        self.set_if_not_none(args, "appIcon", custom_parameter="icon")
        notification = notify2.Notification(
            self.title,
            **args
        )
        notification.show()
