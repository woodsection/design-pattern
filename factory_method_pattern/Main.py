from tkinter import dialog
from factory.Factory import *


if __name__ == "__main__":
    dialog = None
    print("Enter the type you want('mac', 'html')")

    i = input().casefold()
    if i == "mac":
        dialog = MacDialog()
    elif i == "html":
        dialog = HtmlDialog()
    else:
        print("must type 'mac' or 'html'")

    dialog.renderWindow()
