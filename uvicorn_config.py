# Uvicorn configuration to avoid watching virtual environment
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configuration for uvicorn
reload_excludes = [
    "env/*",
    "venv/*",
    ".venv/*",
    "__pycache__/*",
    "*.pyc",
    ".git/*",
    ".pytest_cache/*",
    "*.log"
]

# Convert relative paths to absolute paths for better reliability
reload_excludes_abs = []
for pattern in reload_excludes:
    if not os.path.isabs(pattern):
        reload_excludes_abs.append(os.path.join(current_dir, pattern))
    else:
        reload_excludes_abs.append(pattern)

# Uvicorn server configuration
config = {
    "app": "main:app",
    "host": "127.0.0.1",
    "port": 8000,
    "reload": True,
    "reload_excludes": reload_excludes,
    "access_log": True,
    "log_level": "info"
}