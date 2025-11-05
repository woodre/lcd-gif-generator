import tkinter as tk
from ui.components.color_block import create_color_block
from ui.components.font_block import create_font_block
from ui.components.timing_block import create_timing_block
from ui.components.cursor_block import create_cursor_block
from ui.logic.generator import preview_animation, generate_gif

# === MAIN WINDOW ===
root = tk.Tk()
root.title("LCD GIF Generator")

# === TEXT INPUT ===
text_frame = tk.LabelFrame(root, text="Text", padx=10, pady=5)
text_frame.pack(fill="x", padx=10, pady=5)

text_entry = tk.Entry(text_frame, width=50)
text_entry.insert(0, "Hello, world!")
text_entry.pack(padx=5, pady=5)

# === COLOR SETTINGS ===
color_frame = tk.LabelFrame(root, text="Colors", padx=10, pady=5)
color_frame.pack(fill="x", padx=10, pady=5)

text_block = create_color_block(color_frame, "Text Color", "lime")
bg_block = create_color_block(color_frame, "Background Color", "black")

# === FONT SETTINGS ===
font_block = create_font_block(root, font_dir="fonts", on_font_change=lambda name, size: None)

# === TIMING SETTINGS ===
timing_block = create_timing_block(root)

# === CURSOR SETTINGS ===
cursor_block = create_cursor_block(root)

# === PREVIEW CANVAS ===
preview_frame = tk.LabelFrame(root, text="Preview", padx=10, pady=5)
preview_frame.pack(fill="both", expand=True, padx=10, pady=5)

preview_canvas = tk.Canvas(preview_frame, bg="white", width=300, height=100)
preview_canvas.pack()

# === ACTION BUTTONS ===
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

preview_button = tk.Button(button_frame, text="Preview", command=lambda: preview_animation(
    canvas=preview_canvas,
    text=text_entry.get(),
    font_name=font_block["font_var"].get(),
    font_size=font_block["font_size_var"].get(),
    text_color=text_block["hex_var"].get(),
    bg_color=bg_block["hex_var"].get(),
    frame_duration=timing_block["frame_duration_var"].get(),
    total_duration=timing_block["total_duration_var"].get(),
    cursor_enabled=cursor_block["cursor_enabled_var"].get(),
    cursor_char=cursor_block["cursor_char_var"].get(),
    blink_rate=cursor_block["blink_rate_var"].get()
))
preview_button.pack(side="left", padx=10)

generate_button = tk.Button(button_frame, text="Generate GIF", command=lambda: generate_gif(
    output_path="output.gif",
    text=text_entry.get(),
    font_name=font_block["font_var"].get(),
    font_size=font_block["font_size_var"].get(),
    text_color=text_block["hex_var"].get(),
    bg_color=bg_block["hex_var"].get(),
    frame_duration=timing_block["frame_duration_var"].get(),
    total_duration=timing_block["total_duration_var"].get(),
    cursor_enabled=cursor_block["cursor_enabled_var"].get(),
    cursor_char=cursor_block["cursor_char_var"].get(),
    blink_rate=cursor_block["blink_rate_var"].get(),
    overwrite=True
))
generate_button.pack(side="left", padx=10)

# === MAIN LOOP ===
root.mainloop()