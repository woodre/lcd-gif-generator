import tkinter.messagebox as messagebox
import os
import re

def slugify(text):
    return re.sub(r'[^a-zA-Z0-9_]', '', text.replace(" ", "_")).lower()

def get_safe_output_path(filename, folder="output", extension="gif"):
    safe_filename = slugify(filename)
    output_path = os.path.join(folder, f"{safe_filename}.{extension}")

    if os.path.exists(output_path):
        confirm = messagebox.askyesno("File Exists", f"'{output_path}' already exists. Overwrite?")
        if not confirm:
            raise FileExistsError(f"File '{output_path}' already exists, user cancelled.")

    return output_path