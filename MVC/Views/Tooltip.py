import tkinter as tk

class Tooltip:
    def __init__(self, widget, text, background="white", foreground="black"):
        self.background = background
        self.foreground = foreground
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.label = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, *args):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        self.label = tk.Label(self.tooltip, text=self.text, background=self.background, foreground=self.foreground)
        self.label.pack()

    def hide_tooltip(self, *args):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
            self.label = None

    def update_tooltip(self, text, background=None, foreground=None):
        if text:
            self.text = text
        if background:
            self.background = background
        if foreground:
            self.foreground = foreground
        if self.label:
            self.label.config(text=self.text, background=self.background, foreground=self.foreground)