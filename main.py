from PIL import Image
import os

IMAGES_DIR = 'mecha_images/' # game_images/, and model_images/
BASE_URL = 'https://acrylicosvallejo.com/en/categoria/hobby/mecha-color-en/page/'

"""TARGET_COLORS = [
    [242, 224, 111], # Straw
    [247, 249, 204], # Lemon Chiffon
    [74, 186, 163], # Ocean Blue
    [163, 247, 181], # Teal Deer
    [195, 66, 63] # English Vermillion
]"""

TARGET_COLORS = [
    [3, 233, 184] # Menoth White Base
]

VALLEJO_COLORS = [
    #{filename: '', color: [1, 1, 1]}
]

def get_color(filename):
    im = Image.open(filename) # Can be many different formats.
    pix = im.load()
    return pix[200,450]  # Get the RGBA Value of the a pixel of an image

def load_colors():
    for filename in os.listdir(IMAGES_DIR):
        VALLEJO_COLORS.append({
            'filename': filename,
            'color': get_color(os.path.join(IMAGES_DIR, filename))
        })

def find_winning_color(target_color):
    winning_color = 'NONE'
    winning_color_score = 999

    for vcolor in VALLEJO_COLORS:
        cscore = abs(vcolor['color'][0] - target_color[0]) + abs(vcolor['color'][1] - target_color[1]) + abs(vcolor['color'][2] - target_color[2])
        
        if cscore < 60:
            print(vcolor['filename'], cscore)

        if cscore < winning_color_score:
            winning_color = vcolor['filename']
            winning_color_score = cscore
    print(winning_color)
    print(winning_color_score)

if __name__ == "__main__":
    load_colors()

    for tcolor in TARGET_COLORS:
        find_winning_color(tcolor)
