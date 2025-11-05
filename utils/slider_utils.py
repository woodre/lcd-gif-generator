def sync_total_duration(frame_duration, total_slider, text):
    """Adjust total duration based on frame duration and text length."""
    num_frames = max(1, len(text))
    total = frame_duration * num_frames
    total = min(max(total, total_slider.cget("from")), total_slider.cget("to"))
    total_slider.set(total)

def sync_frame_duration(total_duration, frame_slider, text):
    """Adjust frame duration based on total duration and text length."""
    num_frames = max(1, len(text))
    new_frame = total_duration // num_frames
    new_frame = min(max(new_frame, frame_slider.cget("from")), frame_slider.cget("to"))
    frame_slider.set(new_frame)