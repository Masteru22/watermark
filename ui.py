import tkinter as tk
from PIL import ImageTk, Image
import config
import logic


days = ['Top-Left', 'Top-Right', 'Bottom-Left', 'Bottom-Right', 'Center']


canvas = None
frame_controls = None
input_text = None
input_size = None
choose_color_btn = None
opt = None
apply_btn = None
save_btn = None

def display_image(im):
    global canvas
    img_width, img_height = im.size
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    if img_width > canvas_width or img_height > canvas_height:
        im.thumbnail((canvas_width, canvas_height))
    img = ImageTk.PhotoImage(im)
    canvas.img = img
    canvas.delete("all")
    canvas.create_image(canvas_width / 2, canvas_height / 2, image=img, anchor=tk.CENTER)

def build_ui(window):
    global canvas, frame_controls, input_text, input_size, choose_color_btn, opt, apply_btn, save_btn

    frame_canvas = tk.Frame(window, width=int(config.WIDTH * 0.7), height=config.HEIGHT, bg="white")
    frame_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_canvas, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    frame_controls = tk.Frame(window, width=int(config.WIDTH * 0.3), height=config.HEIGHT, bg=config.WINDOW_COLOR)
    frame_controls.pack(side=tk.RIGHT, fill=tk.Y)

    # UPLOAD
    upload_btn = tk.Button(frame_controls, text="Upload Image", command=lambda: logic.upload(frame_controls, input_text, input_size, choose_color_btn, opt, apply_btn), bg=config.BUTTON_COLOR)
    upload_btn.pack(pady=10, fill=tk.X, padx=10)

    # TEXT
    input_text = tk.Entry(frame_controls, width=20)

    # FONT SIZE
    input_size = tk.Entry(frame_controls, width=20)

    # COLOR
    choose_color_btn = tk.Button(frame_controls, text="Select Color", command=logic.choose_color)

    # POSITION
    opt = tk.StringVar(value="Top-Left")

    # APPLY
    apply_btn = tk.Button(frame_controls, text="Apply Changes", command=lambda: logic.apply_changes(input_text, input_size, opt, frame_controls, save_btn), bg=config.BUTTON_COLOR)

    # SAVE
    save_btn = tk.Button(frame_controls, text="Save Changes", command=logic.save, bg=config.BUTTON_COLOR)

    return canvas, frame_controls, input_text, input_size, opt
