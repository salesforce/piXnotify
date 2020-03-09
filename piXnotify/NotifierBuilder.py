#  Copyright (c) 2020, salesforce.com, inc.
#   * All rights reserved.
#   * SPDX-License-Identifier: BSD-3-Clause
#   * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

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
