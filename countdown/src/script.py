import imageio
from PIL import Image, ImageDraw, ImageFont
import numpy
import sys
import pygifsicle


# IMAGES_SIZE = (410, 100)
# FONT_SIZE = 100

IMAGES_SIZE = (246, 60)
FONT_SIZE = 60

class Time:
    def __init__(self, n_hours=0, n_minutes=0, n_seconds=0):
        self.n_hours = n_hours
        self.n_minutes = n_minutes
        self.n_seconds = n_seconds
        
    def __str__(self):
        formatime = lambda n: str(n).zfill(2)
        return f"{formatime(self.n_hours)}:{formatime(self.n_minutes)}:{formatime(self.n_seconds)}"
    
    @property
    def is_up(self):
        return (self.n_hours, self.n_minutes, self.n_seconds) == (0, 0, 0)
    
    def get_n_seconds(self):
        return self.n_hours * 3600 + self.n_minutes * 60 + self.n_seconds
    
    def decrease_one_second(self):
        if self.n_seconds != 0:
            self.n_seconds -= 1
        elif self.n_minutes != 0:
            self.n_minutes -= 1
            self.n_seconds = 59
        elif self.n_hours != 0:
            self.n_hours -= 1
            self.n_minutes = 59
            self.n_seconds = 59
        else:
            raise Exception("Time is up")
        
    def get_image(self, fmt='img', bg_color=None, text_color=None):
        bg_color = bg_color or "#000000"
        text_color = text_color or "#FFFFFF"
        img = Image.new(mode='RGB', size=IMAGES_SIZE, color=bg_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("font.ttf", FONT_SIZE)
        draw.text((0, 0), str(self), font=font, fill=text_color)
        
        if fmt == 'img':
            return img
        
        if fmt == 'array':
            return numpy.array(img)


def generate_gif(location, n_hours, n_minutes, n_seconds, n_seconds_to_decrease=None):
    time = Time(n_hours, n_minutes, n_seconds)
    images = list()
    n = time.get_n_seconds()
    for _ in range(n):
        images.append(time.get_image(fmt='array'))
        time.decrease_one_second()
    images.append(time.get_image(fmt='array'))
    print("Size: ", sys.getsizeof(images))
    imageio.mimsave(location, images, duration='1')
    pygifsicle.optimize(location)


if __name__ == "__main__":
    gif_filename = 'timere.gif'
    generate_gif(gif_filename, 0, 1, 0)
