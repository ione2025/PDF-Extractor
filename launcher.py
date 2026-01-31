"""
PDF Extractor Pro - Desktop Launcher
Starts the Flask application and opens the browser automatically.
"""
import os
import sys
import webbrowser
import time
import threading
from app import app

def open_browser():
    """Open the default browser after a short delay."""
    time.sleep(2)  # Wait for server to start
    webbrowser.open('http://localhost:5000')

def main():
    """Main launcher function."""
    print("=" * 60)
    print("PDF Extractor Pro - Desktop Application")
    print("=" * 60)
    print("\nStarting web server...")
    print("The application will open in your default browser.")
    print("\nAccess URL: http://localhost:5000")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    
    # Open browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start Flask app
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n\nShutting down PDF Extractor Pro...")
        sys.exit(0)

if __name__ == '__main__':
    main()
