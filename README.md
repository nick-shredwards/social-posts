# social-posts
A twitter like messaging and posting app


Local Development Setup
Prerequisites
Node.js (https://nodejs.org/)
Python 3.8+

1. Clone the repository
2. Install frontend dependencies (Vite)
npm install

3. Set up Python virtual environment (backend)
Mac
python3 -m venv .venv
source .venv/bin/activate
cd backend
pip install -r requirements.txt

Windows
python -m venv .venv
.venv\Scripts\activate
cd backend
pip install -r requirements.txt

4. Start the servers
Vite frontend
npm run dev

Python backend
# From the project root (Mac)
./.venv/bin/python backend/app.py
# Or, if activated (Mac/Windows)
python app.py

5. Access the app
Frontend: http://localhost:5173/
Backend API: http://127.0.0.1:8000/