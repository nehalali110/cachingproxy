import sys
import uvicorn
from utils.helpers import validate_arguments
from pydantic import ValidationError

def main():
    try:
        port, remote_srvr = validate_arguments(sys.argv)
        print(f"Port: {port} Remote Server: {remote_srvr}")

    except (IndexError, ValidationError, ValueError):
        print("Usage: caching-proxy --port <number> --origin <url>")
        return

if __name__ == "__main__":
    main()
