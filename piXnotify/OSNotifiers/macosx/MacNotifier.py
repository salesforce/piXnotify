import pync

from piXnotify.OSNotifiers.AbstractNotifier import AbstractNotifier


class MacNotifier(AbstractNotifier):
    def __init__(self):
        super().__init__()

    def _notify(self):
        args = {"title": self.title}
        self.set_if_not_none(args, "url")
        self.set_if_not_none(args, "activate")
        self.set_if_not_none(args, "execute")
        self.set_if_not_none(args, "groupid")
        self.set_if_not_none(args, "sound")
        self.set_if_not_none(args, "appIcon")

        pync.notify(self.message, **args)
