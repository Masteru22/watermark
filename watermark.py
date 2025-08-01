import tkinter as tk
import config
import logic
import ui

window = tk.Tk()
window.title("Watermark")
window.geometry(f"{config.WIDTH}x{config.HEIGHT}")
logic.center_window(window)
window.configure(background=config.WINDOW_COLOR)

canvas, frame_controls, input_text, input_size, opt = ui.build_ui(window)

window.mainloop()
