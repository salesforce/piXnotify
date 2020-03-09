#  Copyright (c) 2020, salesforce.com, inc.
#   * All rights reserved.
#   * SPDX-License-Identifier: BSD-3-Clause
#   * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

from abc import ABC, abstractmethod


class AbstractNotifier(ABC):
    def __init__(self):
        self.title = "defaultTitle"
        self.message = ""
        self.appIcon = None
        self.activate = None
        self.execute = None
        self.url = None
        self.groupid = None
        self.sound = None

    def set_if_not_none(self, args_dict, parameter, custom_parameter=None):
        if custom_parameter is None:
            custom_parameter = parameter

        if getattr(self, parameter) is not None:
            args_dict[custom_parameter] = getattr(self, parameter)

    def notify(self):
        if self.title is None:
            raise ValueError("Title cannot be empty")
        self._notify()
        self.__init__()

    def set_title(self, title):
        self.title = title
        return self

    def set_app_icon(self, app_icon):
        self.appIcon = app_icon
        return self

    def set_message(self, message):
        self.message = message
        return self

    def set_activate(self, activate_path):
        self.activate = activate_path
        return self

    def set_url(self, url_path):
        self.url = url_path
        return self

    def set_group(self, group_id):
        self.groupid = group_id
        return self

    def set_sound(self, sound):
        self.sound = sound
        return self

    def set_execute(self, execute):
        self.execute = execute
        return self

    @abstractmethod
    def _notify(self):
        pass
