"""
WSGI entry point for PDF Extractor Pro web application.
Use this file for production deployments with WSGI servers like Gunicorn or uWSGI.

Example usage:
    gunicorn wsgi:app
    gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
"""

from app import app

# For production deployment
application = app

if __name__ == "__main__":
    # This is only for development/testing
    app.run()
