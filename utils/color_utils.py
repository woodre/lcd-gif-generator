# utils/color_utils.py

from PIL import ImageColor

def rgb_to_hex(rgb):
    """Convert an (R, G, B) tuple to a hex color string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def rgb_to_name(rgb):
    """Convert an (R, G, B) tuple to a named color if possible, else hex."""
    try:
        name = ImageColor.getcolor(rgb, "RGB")
        for color_name in ImageColor.colormap:
            if ImageColor.getrgb(color_name) == rgb:
                return color_name
    except ValueError:
        pass
    return rgb_to_hex(rgb)

def parse_color(color_input):
    """
    Accepts named colors (e.g. 'lime'), hex codes (e.g. '#00FF00'), or RGB strings (e.g. '0,255,0').
    Returns an (R, G, B) tuple or raises ValueError for invalid formats.
    """
    color_input = color_input.strip()

    # RGB string: "255,255,255"
    if "," in color_input:
        try:
            parts = tuple(map(int, color_input.split(",")))
            if len(parts) == 3 and all(0 <= c <= 255 for c in parts):
                return parts
            raise ValueError
        except ValueError:
            raise ValueError(f"Invalid RGB format: {color_input}")

    # Hex code or named color
    try:
        return ImageColor.getrgb(color_input)
    except ValueError:
        raise ValueError(f"Unknown color format: {color_input}")