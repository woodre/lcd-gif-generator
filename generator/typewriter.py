from PIL import Image, ImageDraw, ImageFont
from utils.color_utils import parse_color
import os

def generate_typewriter_gif(
    text,
    output_path,
    font_path,
    font_size=24,
    frame_duration=100,
    text_color="lime",
    background_color="black",
    method="pillow",  # or "imageio"
    blink_cursor=False,
    blink_interval=2,  # number of blinks per character
    alignment="left",  # "left", "center", "right"
    cursor_char="|"
):
    frames = []
    font = ImageFont.truetype(font_path, font_size)
    canvas_size = (max(300, font.getlength(text + cursor_char) + 40), 240)

    text_color = parse_color(text_color)
    background_color = parse_color(background_color)

    # Typing frames with optional blinking
    for i in range(1, len(text) + 1):
        base_text = text[-i:] if alignment == "right" else text[:i]
        blink_frames = blink_interval * 2 if blink_cursor else 1

        for b in range(blink_frames):
            show_cursor = blink_cursor and (b % 2 == 0)

            img = Image.new("RGB", canvas_size, background_color)
            draw = ImageDraw.Draw(img)
            draw.rectangle([0, 0, canvas_size[0], canvas_size[1]], fill=background_color)

            bbox = font.getbbox(base_text)
            text_width = bbox[2] - bbox[0]

            if alignment == "center":
                x = (canvas_size[0] - text_width) // 2
            elif alignment == "right":
                x = canvas_size[0] - text_width - 10
            else:
                x = 10

            y = canvas_size[1] // 2 - font_size // 2
            draw.text((x, y), base_text, font=font, fill=text_color)

            if show_cursor:
                cursor_x = x + font.getlength(base_text)
                draw.text((cursor_x, y), cursor_char, font=font, fill=text_color)

            frames.append(img)

    # Final steady blinking cursor after full text
    if blink_cursor:
        for b in range(blink_interval * 2):
            show_cursor = (b % 2 == 0)

            img = Image.new("RGB", canvas_size, background_color)
            draw = ImageDraw.Draw(img)
            draw.rectangle([0, 0, canvas_size[0], canvas_size[1]], fill=background_color)            

            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]

            if alignment == "center":
                x = (canvas_size[0] - text_width) // 2
            elif alignment == "right":
                x = canvas_size[0] - text_width - 10
            else:
                x = 10

            y = canvas_size[1] // 2 - font_size // 2
            draw.text((x, y), text, font=font, fill=text_color)

            if show_cursor:
                cursor_x = x + font.getlength(text)
                draw.text((cursor_x, y), cursor_char, font=font, fill=text_color)

            frames.append(img)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if method == "imageio":
        import imageio
        imageio.mimsave(output_path, frames, duration=frame_duration / 1000)
    else:
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=frame_duration,
            loop=0,
            disposal=2
        )

    print(f"✅ GIF saved to {output_path}")