import uvicorn
import sys
import os

print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

print("Updated Python path:", sys.path)

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
