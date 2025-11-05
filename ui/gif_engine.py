from PIL import Image, ImageDraw, ImageFont
import os

def generate_gif_frames(text, font_name, font_size, text_color, bg_color,
                        frame_duration, total_duration,
                        cursor_enabled, cursor_char, blink_rate):
    """
    Generates a list of PIL Image frames for the animated GIF.
    """
    try:
        font = ImageFont.truetype(font_name, font_size)
    except IOError:
        font = ImageFont.load_default()

    frames = []
    chars = list(text)
    steps = len(chars) + 1  # include full text
    blink_interval = max(1, blink_rate // frame_duration)
    total_frames = max(1, total_duration // frame_duration)

    for i in range(total_frames):
        step = min(i, steps - 1)
        current_text = "".join(chars[:step])

        # Blinking cursor logic
        if cursor_enabled and (i % blink_interval) < (blink_interval // 2):
            current_text += cursor_char

        img = render_text_image(current_text, font, text_color, bg_color)
        frames.append(img)

    return frames

def render_text_image(text, font, text_color, bg_color):
    """
    Renders a single frame with the given text and font.
    """
    dummy_img = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    text_size = draw.textbbox((0, 0), text, font=font)
    width = text_size[2] - text_size[0] + 20
    height = text_size[3] - text_size[1] + 20

    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, font=font, fill=text_color)

    return img

def export_gif(frames, output_path, overwrite=False):
    """
    Saves the list of frames as an animated GIF.
    """
    if not frames:
        raise ValueError("No frames to export.")

    if os.path.exists(output_path) and not overwrite:
        raise FileExistsError(f"{output_path} already exists. Use overwrite=True to replace it.")

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=frames[0].info.get("duration", 100),
        loop=0
    )