# main.py

from generator.typewriter import generate_typewriter_gif
from utils.file_utils import get_safe_output_path
import os

# Load available fonts
font_dir = "assets/fonts"
fonts = [f for f in os.listdir(font_dir) if f.lower().endswith(".ttf")]

print("Available fonts:")
for i, f in enumerate(fonts):
    print(f"{i+1}. {f}")

choice = int(input("\nSelect a font by number: ")) - 1
text = input("Enter text to animate: ")
filename = input("Enter output filename (without extention): ")
text_color = input("Enter text color (e.g., lime, #00FF00, or 0,255,0): ")
background_color = input("Enter background color (e.g., black, #000000, or 255,255,255): ")

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Generate GIF
generate_typewriter_gif(
    text=text,
    output_path=get_safe_output_path(filename),
    font_path=os.path.join(font_dir, fonts[choice]),
    font_size=24,
    frame_duration=100,
    text_color=text_color,
    background_color=background_color
)