# ui/logic/generator.py

from gif_engine import generate_gif_frames, export_gif
from utils.color_utils import parse_color
from PIL import ImageTk
import tkinter as tk

def preview_animation(canvas, text, font_name, font_size, text_color, bg_color,
                      frame_duration, total_duration, cursor_enabled, cursor_char, blink_rate):
    """
    Renders the first frame of the animation on the preview canvas.
    """
    try:
        text_rgb = parse_color(text_color)
        bg_rgb = parse_color(bg_color)

        frames = generate_gif_frames(
            text=text,
            font_name=font_name,
            font_size=font_size,
            text_color=text_rgb,
            bg_color=bg_rgb,
            frame_duration=frame_duration,
            total_duration=total_duration,
            cursor_enabled=cursor_enabled,
            cursor_char=cursor_char,
            blink_rate=blink_rate
        )

        if frames:
            img = ImageTk.PhotoImage(frames[0])
            canvas.config(width=img.width(), height=img.height())
            canvas.image = img  # Prevent garbage collection
            canvas.delete("all")
            canvas.create_image(0, 0, anchor="nw", image=img)

    except Exception as e:
        print(f"⚠️ Preview failed: {e}")

def generate_gif(output_path, text, font_name, font_size, text_color, bg_color,
                 frame_duration, total_duration, cursor_enabled, cursor_char, blink_rate,
                 overwrite=False):
    """
    Generates and exports the full animated GIF.
    """
    try:
        text_rgb = parse_color(text_color)
        bg_rgb = parse_color(bg_color)

        frames = generate_gif_frames(
            text=text,
            font_name=font_name,
            font_size=font_size,
            text_color=text_rgb,
            bg_color=bg_rgb,
            frame_duration=frame_duration,
            total_duration=total_duration,
            cursor_enabled=cursor_enabled,
            cursor_char=cursor_char,
            blink_rate=blink_rate
        )

        export_gif(frames, output_path, overwrite=overwrite)
        print(f"✅ GIF saved to {output_path}")

    except Exception as e:
        print(f"⚠️ GIF generation failed: {e}")