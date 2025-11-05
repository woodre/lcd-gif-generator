import tkinter as tk
from tkinter import Canvas
import math
from colorsys import hsv_to_rgb, rgb_to_hsv
from utils.color_utils import parse_color

class ColorWheelPicker(tk.Frame):
    def __init__(self, master, radius=100, callback=None):
        super().__init__(master)
        self.radius = radius
        self.callback = callback  # Called with (r, g, b) when selection changes
        self.canvas = Canvas(self, width=2 * radius, height=2 * radius, highlightthickness=0)
        self.canvas.pack()
        self._draw_wheel()
        self.selector = self.canvas.create_oval(0, 0, 0, 0, outline="white", width=2)
        self.canvas.bind("<Button-1>", self._on_click)

    def _draw_wheel(self):
        for angle in range(360):
            for r in range(self.radius):
                h = angle / 360
                s = r / self.radius
                v = 1
                rgb = hsv_to_rgb(h, s, v)
                x = self.radius + r * math.cos(angle * math.pi / 180)
                y = self.radius + r * math.sin(angle * math.pi / 180)
                self.canvas.create_line(x, y, x + 1, y, fill=self._rgb_to_hex(rgb))

    def _on_click(self, event):
        dx = event.x - self.radius
        dy = event.y - self.radius
        dist = (dx**2 + dy**2)**0.5
        if dist > self.radius:
            return
        h = (math.atan2(dy, dx) * 180 / math.pi) % 360 / 360
        s = dist / self.radius
        v = 1
        r, g, b = hsv_to_rgb(h, s, v)
        self._move_selector(event.x, event.y)
        if self.callback:
            self.callback((int(r * 255), int(g * 255), int(b * 255)))

    def _move_selector(self, x, y):
        self.canvas.coords(self.selector, x - 5, y - 5, x + 5, y + 5)

    def _rgb_to_hex(self, rgb):
        r, g, b = [int(c * 255) for c in rgb]
        return f"#{r:02x}{g:02x}{b:02x}"

    def set_color(self, color_str):
        try:
            r, g, b = parse_color(color_str)
            h, s, _ = rgb_to_hsv(r / 255, g / 255, b / 255)
            angle = h * 2 * math.pi
            radius = s * self.radius
            x = self.radius + radius * math.cos(angle)
            y = self.radius + radius * math.sin(angle)
            self._move_selector(x, y)
        except Exception as e:
            print(f"⚠️ Could not set color on wheel: {e}")