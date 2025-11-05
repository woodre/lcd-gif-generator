import tkinter as tk
from tkinter import font
import os

def create_font_block(parent, font_dir, on_font_change):
    frame = tk.LabelFrame(parent, text="Font Settings", padx=10, pady=5)
    frame.pack(fill="x", pady=5)

    font_var = tk.StringVar()
    font_size_var = tk.IntVar(value=16)

    # Load fonts
    available_fonts = sorted(set(font.families()))
    if font_dir and os.path.isdir(font_dir):
        for fname in os.listdir(font_dir):
            if fname.lower().endswith(".ttf"):
                available_fonts.append(fname)

    font_dropdown = tk.OptionMenu(frame, font_var, *available_fonts)
    font_dropdown.config(width=20)
    font_dropdown.pack(side="left", padx=5)

    font_size_slider = tk.Scale(frame, from_=8, to=48, orient="horizontal", label="Size", variable=font_size_var)
    font_size_slider.pack(side="left", padx=10)

    def on_change(*_):
        on_font_change(font_var.get(), font_size_var.get())

    font_var.trace_add("write", on_change)
    font_size_var.trace_add("write", on_change)

    return {
        "frame": frame,
        "font_var": font_var,
        "font_size_var": font_size_var
    }