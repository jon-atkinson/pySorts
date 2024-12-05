import tkinter
from os import environ
from pathlib import Path
from sys import base_prefix
import platform

if not ("TCL_LIBRARY" in environ and "TK_LIBRARY" in environ):
    try:
        tkinter.Tk()
    except tkinter.TclError:
        tk_dir = "tcl" if platform.system() == "Windows" else "lib"
        tk_path = Path(base_prefix) / tk_dir
        environ["TCL_LIBRARY"] = str(next(tk_path.glob("tcl8.*")))
        environ["TK_LIBRARY"] = str(next(tk_path.glob("tk8.*")))


def main():
    tk = tkinter.Tk()
    tk.mainloop()


if __name__ == "__main__":
    main()
