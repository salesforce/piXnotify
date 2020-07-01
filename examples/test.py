from piXnotify import notifier


def notify_with_title():
    notifier.set_title("Title").notify()


def notify_with_message():
    notifier.set_title("Title").set_message("Message").notify()


def notify_with_icon():
    notifier.set_title("Title").set_app_icon(
        "http://pngimg.com/uploads/github/github_PNG83.png"
    ).notify()


if __name__ == "__main__":
    notify_with_title()
    notify_with_message()
    notify_with_icon()
