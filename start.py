import os
import subprocess
import time
import sys

port = os.environ.get("PORT", "8000")

api_process = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "uvicorn",
        "api:app",
        "--host",
        "0.0.0.0",
        "--port",
        port
    ]
)

time.sleep(3)

try:
    subprocess.run(
        [
            sys.executable,
            "app.py"
        ],
        check=True
    )
finally:
    api_process.terminate()
