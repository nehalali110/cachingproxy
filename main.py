import sys
from requests import Request
import uvicorn
from utils.helpers import validate_arguments
from pydantic import ValidationError
from requests.exceptions import RequestException
from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()

@app.get("/{full_path:path}")
def test_endpoint(full_path:str, request: Request):
    return Res

def main():
    try:
        port, remote_srvr = validate_arguments(sys.argv)
        print(f"Port: {port} Remote Server: {remote_srvr}")
        print("Starting the server...")
        uvicorn.run("main:app", port=port ,reload=True)

    except (IndexError, ValidationError, ValueError):
        print("Usage: caching-proxy --port <number> --origin <url>")
        return

    except RequestException:
        remote_url = sys.argv[4]
        print(f"Invalid origin url: {remote_url}")

if __name__ == "__main__":
    main()
