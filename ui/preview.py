# ui/preview.py

import os
from PIL import Image, ImageDraw, ImageFont

def list_fonts(font_dir="assets/fonts"):
    return [f for f in os.listdir(font_dir) if f.lower().endswith(".ttf")]

def render_preview(text, font_file, canvas_size=(240, 240), font_size=24):
    font_path = os.path.join("assets/fonts", font_file)
    font = ImageFont.truetype(font_path, font_size)
    img = Image.new("RGB", canvas_size, "black")
    draw = ImageDraw.Draw(img)
    text_width, _ = draw.textsize(text, font=font)
    x = 10 # or center: (canvas_size[0] - text_width) // 2

    y = canvas_size[1] // 2 - font_size // 2
    draw.text((x,y), text, font=font, fill="text_color")
    img.show()

if __name__ == "__main__":
    fonts = list_fonts()
    print("Available fonts:")
    for i, f in enumerate(fonts):
        print(f"{i+1}. {f}")

    choice = int(input("\nSelect a font by number: ")) - 1
    text = input("Enter preview text: ")

    render_preview(text, fonts[choice])