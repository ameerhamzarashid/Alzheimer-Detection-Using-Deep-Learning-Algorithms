from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Load your deep learning model
model = load_model(r'C:\Users\Ameer Hamza\OneDrive\Desktop\Final Year Project\Frontend\Models\HybridVGG.h5')

# Define any preprocessing function if needed
def preprocess_image(image_file):
    img = Image.open(image_file)
    img = img.resize((224, 224))  # Resize the image to match the input size of your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to be between 0 and 1
    return img_array

@app.route('/home')
def index():
    return render_template('home.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

# Define the routes

@app.route('/alzheimer', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        preprocessed_image = preprocess_image(file)
        
        # Make prediction using your model
        prediction = model.predict(preprocessed_image)
        predicted_class = np.argmax(prediction)
        
        # Map predicted class index to class label
        class_names = ['Mild Demented', 'Moderate Demented', 'Very Mild Demented', 'Non Demented']
        predicted_label = class_names[predicted_class]

        # Return the predicted label as plain text response
        return predicted_label
    except Exception as e:
        error_message = str(e)
        return 'Error: ' + error_message

@app.route('/alzheimer', methods=['GET'])
def alzheimer_page():
    return render_template('alzheimer.html')

# Define route for the Results page
@app.route('/results')
def results():
    # Handle results page content and history here
    prediction_history = [
        {
            'date': '2023-08-01',
            'stage': 'Mild',
            'confidence': 0.87,
        },
        # Add more prediction history data as needed
    ]
    return render_template('results.html', prediction_history=prediction_history)

# Define route for the FAQs page
@app.route('/faqs')
def faqs():
    # Add the FAQs content here
    return render_template('faqs.html')

# Define route for the Team Information page
@app.route('/team_information')
def team_information():
    # Add team information content here
    return render_template('team_information.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
