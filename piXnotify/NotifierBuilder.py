import sys

class NotifierBuilder(object):
    @staticmethod
    def build():
        if sys.platform.startswith('darwin'):
            mod = __import__('piXnotify.OSNotifiers.macosx.MacNotifier', fromlist=['.'])
            notifier = mod.MacNotifier()
            return notifier
        elif sys.platform.startswith('linux'):
            mod = __import__('piXnotify.OSNotifiers.linux.LinuxNotifier', fromlist=['.'])
            notifier = mod.LinuxNotifier()
            return notifier
        elif sys.platform.startswith('win'):
            mod = __import__('piXnotify.OSNotifiers.windows.WindowsNotifier', fromlist=['.'])
            notifier = mod.WindowsNotifier()
            return notifier
        else:
            raise Exception("Platform Not Supported")
