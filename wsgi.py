from app import app  # Import your Flask app instance

if __name__ == '__main__':
    app.run()  # Only for development purposes, not used in production

# This is the WSGI entry point
application = app
