import tkinter as tk

def create_cursor_block(parent):
    frame = tk.LabelFrame(parent, text="Cursor Settings", padx=10, pady=5)
    frame.pack(fill="x", pady=5)

    cursor_enabled_var = tk.BooleanVar(value=True)
    cursor_char_var = tk.StringVar(value="|")
    blink_rate_var = tk.IntVar(value=500)

    tk.Checkbutton(frame, text="Enable Blinking Cursor", variable=cursor_enabled_var).pack(anchor="w")
    tk.Label(frame, text="Cursor Character:").pack(anchor="w")
    tk.Entry(frame, textvariable=cursor_char_var, width=5).pack(anchor="w", padx=5)

    tk.Scale(frame, from_=100, to=1000, orient="horizontal", label="Blink Rate (ms)", variable=blink_rate_var).pack(fill="x", padx=5)

    return {
        "frame": frame,
        "cursor_enabled_var": cursor_enabled_var,
        "cursor_char_var": cursor_char_var,
        "blink_rate_var": blink_rate_var
    }