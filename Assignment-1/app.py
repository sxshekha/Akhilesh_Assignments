from flask import Flask, render_template
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Your personal data
YOUR_NAME = "Gemini AI" # Replace with your actual name
FAVORITE_MOVIES = [
    "2001: A Space Odyssey",
    "Inception",
    "Pulp Fiction",
    "Spirited Away",
    "The Matrix"
]

@app.route('/')
def home():
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Render the template and pass the data
    return render_template(
        'index.html',
        name=YOUR_NAME,
        current_time=current_time,
        movies=FAVORITE_MOVIES
    )

if __name__ == '__main__':
    # Run the app on all interfaces (0.0.0.0) for Docker
    app.run(host='0.0.0.0', port=5000)
