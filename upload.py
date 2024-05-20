from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from keras.preprocessing.image import load_img
from model import process_image, predict_class

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# Path for saving uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app, photos)

# A simple home route
@app.route('/home', methods=['GET', 'POST'])
def home():
    welcome = "Hello, World !"
    return welcome

# The main route for upload and prediction
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        try:
            # Save the image
            filename = photos.save(request.files['photo'])
            print(f"Image saved as: {filename}")

            # Load the image
            image = load_img('./static/img/' + filename, target_size=(224, 224))
            print("Image loaded")

            # Process the image
            image = process_image(image)
            print("Image processed")

            # Make prediction
            prediction, percentage = predict_class(image)
            print(f"Prediction: {prediction}, Probability: {percentage}")

            # Remove any '%' from the percentage string and convert to float
            percentage_float = float(percentage.strip('%')) / 100

            # The answer which will be rendered back to the user
            answer = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Prediction Result</title>
            </head>
            <body style="font-family: Arial, sans-serif; background: linear-gradient(to bottom, #ffffff, #2a415a); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
                <div style="background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); width: 300px; text-align: center;">
                    <h1 style="font-size: 24px; margin-bottom: 20px;">Prediction Result</h1>
                    <p>For <strong>{filename}</strong>:</p>
                    <p>The prediction is: <strong>{prediction}</strong></p>
                    <p>With probability: <strong>{percentage_float:.2%}</strong></p>
                    <a href="/upload" style="background-color: #2a415a; color: #fff; padding: 10px 15px; text-decoration: none; border-radius: 5px;">Upload Another Image</a>
                </div>
            </body>
            </html>
            """
            return answer
        except Exception as e:
            print(f"Error: {e}")
            return f"<h1>Something went wrong: {e}</h1>"
    # Web page to show before the POST request containing the image
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
