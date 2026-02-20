from PIL import Image
from collections import Counter
import sys

def get_dominant_colors(image_path, num_colors=3):
    try:
        image = Image.open(image_path)
        image = image.resize((150, 150)) # Resize for speed
        result = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
        result.putalpha(0)
        colors = result.getcolors(150*150)
        # Sort by count
        colors = sorted(colors, key=lambda x: x[0], reverse=True)
        
        print("Dominant Colors:")
        for count, color in colors:
            # color is a tuple (r, g, b)
            # convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            print(f"{hex_color} (Count: {count})")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_dominant_colors(sys.argv[1])
    else:
        print("Please provide an image path.")
