from PIL import ImageFont

def get_font_name_from_path(font_path, fallback="Courier", size=24):
    """Extract the font family name from a .ttf path using PIL."""
    try:
        pil_font = ImageFont.truetype(font_path, size)
        return pil_font.getname()[0]
    except Exception as e:
        print(f"⚠️ Font load failed: {e}")
        return fallback