from flask import Flask, render_template, request
from PIL import Image
from datetime import datetime
import pandas as pd
import io
import base64

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        data = pd.read_csv("log.csv")
    except:
        data = pd.DataFrame(columns = ["image_name", "time"])

    # Check if an image file was uploaded
    if 'image' not in request.files:
        return 'No image file uploaded'

    # Get the uploaded image file
    image_file = request.files['image']
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
   
    #log
    filename = image_file.filename if image_file.filename != "" else "Unknown"
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data.loc[data.shape[0]] = [filename, current_datetime]

    # Create an in-memory buffer to store the image
    image_buffer = io.BytesIO()

    # Open the image using Pillow
    image = Image.open(image_file)

    # Process the image (add your image processing code here)
    processed_image = image.convert("L")  # Example: convert the image into greyscale
    
    # Save the image to the buffer in PNG format
    processed_image.save(image_buffer, format='PNG')

    # Move the buffer's file pointer to the beginning
    image_buffer.seek(0)

    # Encode the image as base64
    encoded_image = base64.b64encode(image_buffer.getvalue()).decode('utf-8')

    # Generate the data URI for the image
    image_uri = f"data:image/png;base64,{encoded_image}"

    data.to_csv("log.csv", index = False)
    data = data.to_html()
    # Return the processed image as a response without saving
    return render_template('index.html', processed_image_url=image_uri, input_image=image_data, table = data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8081)
