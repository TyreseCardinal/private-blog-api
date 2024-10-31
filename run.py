# run.py
from app import create_app
from config import config

# Specify the environment ('development' or 'production')
app = create_app('development')  # Create the app instance with the specified config

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development; set to False in production
