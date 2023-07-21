# THE PIL IS PYTHON IMAGING LIBRARY AND IS THE LIBRARY CHOSEN FOR THIS PROJECT
# FROM IT WAS IMPORTED IMAGE, IMAGEDRAW AND IMAGEFONT
# GLOB IS A LIBRARY THAT HELPS TO SORT THROUGH FILES AND WILL BE IMPORTANT IN GETTING OUR PICTURE FOLDER
from PIL import Image, ImageDraw, ImageFont
import glob
import tkinter as tk

window = tk.Tk()
window.geometry('400x400')
entry_path = ''
file_label = tk.Label(text='Enter your picture File Path here:', font=('Arial', 10, 'bold'))
file_label.pack()
file_entry = tk.Entry(width=45)
file_entry.pack(pady=(0, 20))
extension_label = tk.Label(text='Enter your picture File Extension here:', font=('Arial', 8, 'bold'))
extension_label.pack()
extension_entry = tk.Entry(width=5)
extension_entry.pack(pady=(0, 20))
message_label = tk.Label(text='Enter your copyright warning here:', font=('Arial', 8, 'bold'))
message_label.pack()
message_entry = tk.Entry(width=45)
message_entry.pack(pady=(0, 20))


# "C:/Users/user/Pictures/Camera Roll/*.jpg"


# THIS HELPS TO SORT THROUGH THIS PATH AND ENDS UP IN A CAMERA ROLL FOLDER
# THE * HELPS TO CHECK FOR EVERY JPG FILE THAT EXISTS IN THAT FOLDER
def create_watermark():
    returned_file_path = file_entry.get()
    file_extension = extension_entry.get()
    watermark = message_entry.get()
    picture_list = glob.glob(f'{returned_file_path}/*.{file_extension}')
    for im in picture_list:
        # THE IMAGE CLASS CALLS THE INDIVIDUAL IMAGES AND CONVERTS TO RGBA
        # WHERE A MEANS ALPHA AND HELPS TO ALTER THE OPACITY OF THE COLOR, 0 MEANS TOTALLY OPAQUE
        original_image = Image.open(im).convert('RGBA')
        image_size = original_image.size
        width = int(original_image.width + 200)
        height = int(original_image.height + 200)
        font = ImageFont.truetype('arial.ttf', size=25)
        text = watermark
        text_size = (200, 40)
        # THE LOGIC HERE IS TO CREATE A NEW IMAGE OF THE SAME SIZE AS THE ORIGINAL
        # THIS WOULD HELPS US TO HOLD THE WATERMARK TEXT WHICH CAN BE ALTERED
        # THE IMAGEDRAW.DRAW METHOD HELPS TO MAKE A PICTURE TO BE DRAWN ON AND WE DO THIS TO ALL PICTURES
        watermark_image = Image.new("RGBA", image_size, color=(255, 255, 255, 0))
        text_image = Image.new("RGBA", text_size, color=(255, 255, 255, 0))
        original_drawing = ImageDraw.Draw(original_image)
        watermark_drawing = ImageDraw.Draw(watermark_image)
        # THIS TEXT_DRAW IS ANOTHER PICTURE THAT WILL HOLD THE TEXT
        # BUT WILL BE PLACED IN THE WATERMARK IMAGE USING THE PASTE METHOD
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((0, 0), text, fill=(255, 255, 255, 80), font=font)
        rotated_text_image = text_image.rotate(angle=25, expand=True)
        for n in range(6):
            width -= 250
            for i in range(6):
                height -= 80 * int(i)
                text_position = (width, height)
                # THE PASTE METHOD PASTES THE ROTATED_TEXT_IMAGE IN THE WATERMARK_IMAGE
                # I BELIEVE IT IS USED TO JOIN PICTURES OF DIFFERENT SIZES
                watermark_image.paste(im=rotated_text_image, box=text_position)
            height = original_image.height
        # THE ALPHA_COMPOSITE JOINS PICTURES OF THE SAME SIZE AND IT JOINS THE TWO PICTURES IT RECEIVES
        combined_images = Image.alpha_composite(original_image, watermark_image)
        # THE SAVE METHOD SAVES THE IMAGE TO A FOLDER USING THE GIVEN PATH
        combined_images.save('C:/Users/user/Pictures/CopyrightImage.png')
        # THE SHOW METHOD SHOWS THE IMAGE ON THE SYSTEM
        combined_images.show()


button = tk.Button(text='Enter', width=10, font=('Arial', 10, 'bold'),
                   command=create_watermark)
button.pack(pady=(20, 0))


window.mainloop()
