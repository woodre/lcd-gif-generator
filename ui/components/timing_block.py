import tkinter as tk

def create_timing_block(parent):
    frame = tk.LabelFrame(parent, text="Timing", padx=10, pady=5)
    frame.pack(fill="x", pady=5)

    frame_duration_var = tk.IntVar(value=100)
    total_duration_var = tk.IntVar(value=2000)

    frame_slider = tk.Scale(frame, from_=20, to=500, orient="horizontal", label="Frame Duration (ms)", variable=frame_duration_var)
    frame_slider.pack(fill="x", padx=5)

    total_slider = tk.Scale(frame, from_=500, to=10000, orient="horizontal", label="Total Duration (ms)", variable=total_duration_var)
    total_slider.pack(fill="x", padx=5)

    return {
        "frame": frame,
        "frame_duration_var": frame_duration_var,
        "total_duration_var": total_duration_var
    }