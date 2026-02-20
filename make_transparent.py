from PIL import Image

def make_logo_transparent(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        new_data = []
        # Target Grey: #343331 approx (52, 51, 49)
        # We will look for pixels close to this and make them transparent
        
        target = (52, 51, 49)
        tolerance = 20 # Adjust if needed

        for item in datas:
            # item is (r, g, b, a)
            if (abs(item[0] - target[0]) < tolerance and 
                abs(item[1] - target[1]) < tolerance and 
                abs(item[2] - target[2]) < tolerance):
                new_data.append((255, 255, 255, 0)) # Fully Transparent
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Saved transparent logo to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    make_logo_transparent("logo_croisia.png", "logo_croisia_transparent.png")
