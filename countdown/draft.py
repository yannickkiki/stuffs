def create_time_image(n_hours=0, n_minutes=0, n_seconds=0):
    formatime = lambda n: str(n).zfill(2)
    time_str = f"{formatime(n_hours)}:{formatime(n_minutes)}:{formatime(n_seconds)}"
    img = Image.new('RGB', (410, 100))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 100)
    draw.text((0, 0), time_str, font=font)
    return img


images = list()
filenames = [f"images/dog.{i}.jpg" for i in range(1, 20)]
for filename in filenames:
    images.append(imageio.imread(filename))
campaign_n_hours = 1     
images
imageio.mimsave('movie.gif', images)