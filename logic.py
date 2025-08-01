from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont, UnidentifiedImageError
import config
import ui

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def upload(frame_controls, input_text, input_size, choose_color_btn, opt, apply_btn):
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            config.image_path = file_path
            im = Image.open(file_path)
            config.current_image = im.copy()
            ui.display_image(im)


            import tkinter as tk
            tk.Label(frame_controls, text="Watermark Text:", bg=config.WINDOW_COLOR).pack(pady=(25, 5))
            input_text.pack(padx=10)

            tk.Label(frame_controls, text="Font Size:", bg=config.WINDOW_COLOR).pack(pady=(20, 5))
            input_size.pack(padx=10)

            choose_color_btn.pack(pady=20, fill=tk.X, padx=10)

            tk.Label(frame_controls, text="Position:", bg=config.WINDOW_COLOR).pack(pady=(20, 5))


            opt_menu = tk.OptionMenu(frame_controls, opt, *ui.days)
            opt_menu.pack(pady=5, fill=tk.X, padx=10)

            apply_btn.pack(pady=20, fill=tk.X, padx=10)

    except UnidentifiedImageError:
        messagebox.showerror('Upload Error', 'Image could not be read, please select a valid image file.')

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code[1]:
        config.selected_color = color_code[1]
    return config.selected_color

def apply_changes(input_text, input_size, opt, frame_controls, save_btn):
    if config.current_image is None:
        messagebox.showwarning("No Image", "Please upload an image first.")
        return

    text = input_text.get()
    try:
        size = int(input_size.get())
    except ValueError:
        size = 20
    color = config.selected_color
    position = opt.get()

    img = config.current_image.copy()
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", size)
    except:
        font = ImageFont.load_default()


    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    img_width, img_height = img.size

    pos_dict = {
        "Top-Left": (10, 10),
        "Top-Right": (img_width - text_width - 10, 10),
        "Bottom-Left": (10, img_height - text_height - 10),
        "Bottom-Right": (img_width - text_width - 10, img_height - text_height - 10),
        "Center": ((img_width - text_width) // 2, (img_height - text_height) // 2),
    }

    draw.text(pos_dict[position], text, fill=color, font=font)
    ui.display_image(img)
    config.current_image = img

    save_btn.pack(pady=10, fill='x', padx=10)


def save():

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All files", "*.*")])
    if file_path:
        config.current_image.save(file_path)
        messagebox.showinfo("Saved", "Image saved successfully!")
