from PIL import Image
from collections import Counter
import textwrap

def get_dominant_colors(image_path, num_colors=5):
    try:
        image = Image.open(image_path)
        image = image.convert('RGBA')
        image = image.resize((150, 150)) # Resize for speed
        pixels = list(image.getdata())
        
        # Filter out transparent pixels and extremely light/dark pixels if needed
        # We want to find the "Grey". 
        # Heuristic: R~G~B and not pure black/white
        valid_pixels = []
        for r, g, b, a in pixels:
            if a < 128: continue # Skip transparent
            valid_pixels.append((r, g, b))

        if not valid_pixels:
            return "No opaque pixels found"

        counts = Counter(valid_pixels)
        common = counts.most_common(num_colors)
        
        print(f"Top {num_colors} colors:")
        for color, count in common:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
            print(f"Color: {color} Hex: {hex_color} Count: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_dominant_colors('logo_croisia.png', 10)
