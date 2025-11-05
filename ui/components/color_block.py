# ui/components/color_block.py

import tkinter as tk
from utils.color_picker import ColorWheelPicker
from utils.color_utils import parse_color, rgb_to_hex, rgb_to_name

def create_color_block(parent, label, initial_color):
    frame = tk.LabelFrame(parent, text=label, padx=10, pady=5)
    frame.pack(fill="x", pady=5)

    name_var = tk.StringVar()
    rgb_var = tk.StringVar()
    hex_var = tk.StringVar()

    def update_fields_from_rgb(rgb):
        name_var.set(rgb_to_name(rgb))
        rgb_var.set(f"{rgb[0]},{rgb[1]},{rgb[2]}")
        hex_var.set(rgb_to_hex(rgb))
        wheel.set_color(rgb_to_hex(rgb))

    def update_from_rgb_entry():
        try:
            rgb = parse_color(rgb_var.get())
            update_fields_from_rgb(rgb)
        except ValueError as e:
            print(f"⚠️ {e}")

    def update_from_hex_entry():
        try:
            rgb = parse_color(hex_var.get())
            update_fields_from_rgb(rgb)
        except ValueError as e:
            print(f"⚠️ {e}")

    # Name
    tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w")
    tk.Entry(frame, textvariable=name_var, width=15, state="readonly").grid(row=0, column=1)

    # RGB
    tk.Label(frame, text="RGB:").grid(row=1, column=0, sticky="w")
    rgb_entry = tk.Entry(frame, textvariable=rgb_var, width=15)
    rgb_entry.grid(row=1, column=1)
    rgb_entry.bind("<FocusOut>", lambda e: update_from_rgb_entry())
    rgb_entry.bind("<Return>", lambda e: update_from_rgb_entry())

    # Hex
    tk.Label(frame, text="Hex:").grid(row=2, column=0, sticky="w")
    hex_entry = tk.Entry(frame, textvariable=hex_var, width=15)
    hex_entry.grid(row=2, column=1)
    hex_entry.bind("<FocusOut>", lambda e: update_from_hex_entry())
    hex_entry.bind("<Return>", lambda e: update_from_hex_entry())

    # Color wheel
    wheel = ColorWheelPicker(
        frame,
        radius=60,
        callback=lambda rgb: update_fields_from_rgb(rgb)
    )
    wheel.grid(row=0, column=2, rowspan=3, padx=10)

    # Initialize
    try:
        rgb = parse_color(initial_color)
        update_fields_from_rgb(rgb)
    except ValueError:
        print(f"⚠️ Invalid initial color: {initial_color}")

    return {
        "frame": frame,
        "name_var": name_var,
        "rgb_var": rgb_var,
        "hex_var": hex_var,
        "wheel": wheel
    }