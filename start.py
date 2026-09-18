import os
import subprocess
import sys
import time


api_process = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "uvicorn",
        "api:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000"
    ]
)

time.sleep(5)

try:
    port = os.environ.get("PORT", "7860")

    subprocess.run(
        [
            sys.executable,
            "app.py"
        ],
        check=True,
        env={
            **os.environ,
            "PORT": port
        }
    )

finally:
    api_process.terminate()
    api_process.wait()
