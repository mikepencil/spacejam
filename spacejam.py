from os import path, mkdir
from PIL import Image
import pandas as pd
import numpy as np
import random

output_folder = "/Users/tylercreighton/Desktop/spacejam/jamsesh"
if not path.exists(output_folder):
    mkdir(output_folder)

backgrounds = ["space"]
planets1 = ["planet1", "planet2","planet3","planet4", "planet5","planet6", "planet7", "planet8","planet9","planet10", "planet11","planet12", "planet13", "planet14","planet15","planet16", "planet17","planet18", "planet19", "planet20"]

def generate_image(background, planet1, file_name):
   
    from random import seed
    from random import randint
    seed()
    for _ in range(1):
	Xcoord = randint(0,1000)
    for _ in range(1):
        Ycoord = randint(0,1000)
    for _ in range(1):
        size1 = randint(0,200)
    
    coordinates = (Xcoord, Ycoord)
    background_file = path.join("/Users/tylercreighton/Desktop/spacejam/background", f"{background}.png")
    background_image = Image.open(background_file)
    
    planet_file = path.join("/Users/tylercreighton/Desktop/spacejam/planets1", f"{planet1}.png")
    planet_image = Image.open(planet_file)
    planet_resize = planet_image.resize((size1, size1))
    background_image.paste(planet_resize, coordinates, mask=planet_resize)

    output_file = path.join(output_folder, f"{file_name}.png")
    background_image.save(output_file)
    
    
def generate_random_imgs(total_imgs):

    for num in range(total_imgs):
        
        background = np.random.choice(np.arange(0,len(backgrounds)), p=[1])
        background = backgrounds[background]
        
        planet1 = np.random.choice(np.arange(0,len(planets1)), p=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
        planet1 = planets1[planet1]
        
        generate_image(background, planet1, f"generated{num}")
        
generate_random_imgs(10)
    
