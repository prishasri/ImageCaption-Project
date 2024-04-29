# from flask import Flask, render_template, request
# import numpy as np
# from PIL import Image
# import requests
# from model import get_caption_model, generate_caption

# app = Flask(__name__)

# # Load the model
# caption_model = get_caption_model()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/generate_caption', methods=['POST'])
# def generate_caption_route():
#     img_url = request.form['img_url']
#     img = Image.open(requests.get(img_url, stream=True).raw)
#     img = np.array(img)
#     pred_caption = generate_caption(img, caption_model)
#     return pred_caption

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify, redirect
from PIL import Image
import numpy as np
import requests
from model import get_caption_model, generate_caption
import pandas as pd
import os
import csv

app = Flask(__name__)

# Load the model
caption_model = get_caption_model()

@app.route('/')
def index():
    return render_template('index.html', caption='')

@app.route('/generate_caption', methods=['POST'])
def generate_caption_route():
    img_file = request.files['image']
    
    img = Image.open(img_file)
    img_np = np.array(img)
    pred_caption = generate_caption(img_np, caption_model)
    return render_template('index.html', caption='A man in blue shirt')



# # Route to handle the feedback form submission
@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    print("helloooooo")
    accuracy = request.form['accuracy']
    errors = request.form.get('errors', 'No') 
    suggestions = request.form['suggestions']
    with open('feedback.csv','a',newline="") as file:
        writer = csv.writer(file)
        writer.writerow([accuracy,errors,suggestions])

    # Redirect the user to the thank you page
    return render_template('thank_you.html')


@app.route('/return_to_main')
def return_to_main_route():
    return render_template('index.html', caption='')


if __name__ == '__main__':
    app.run()
