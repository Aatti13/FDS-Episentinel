import uvicorn
import os
from dotenv import load_dotenv
from app import app

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

if __name__ == "__main__":
  uvicorn.run(app, host=HOST, port=PORT)
  # print(f"HOST: {HOST}\nPORT: {PORT}")