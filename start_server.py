#!/usr/bin/env python
"""
Startup script for the expense tracker FastAPI application.
This script starts uvicorn with proper configuration to avoid file watching issues.
"""

import uvicorn
from uvicorn_config import config

if __name__ == "__main__":
    print("Starting Expense Tracker API...")
    print(f"Server will be available at: http://{config['host']}:{config['port']}")
    print("API documentation will be available at: http://127.0.0.1:8000/docs")
    print("Alternative docs at: http://127.0.0.1:8000/redoc")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        uvicorn.run(**config)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")