#  Copyright (c) 2020, salesforce.com, inc.
#   * All rights reserved.
#   * SPDX-License-Identifier: BSD-3-Clause
#   * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
from os import path

from win10toast import ToastNotifier

from piXnotify.OSNotifiers.AbstractNotifier import AbstractNotifier


class WindowsNotifier(AbstractNotifier):
    def __init__(self):
        super().__init__()
        self.toaster = ToastNotifier()

    def set_app_icon(self, app_icon):
        if path.exists(app_icon):
            self.appIcon = app_icon
        return self

    def _notify(self):
        args = {}

        self.set_if_not_none(args, "sound")
        self.set_if_not_none(args, "appIcon", "icon_path")

        self.toaster.show_toast(self.title, self.message, **args)
