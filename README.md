# Social Posts

A Twitter-like messaging and posting app.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Starting the Servers](#starting-the-servers)
- [Accessing the App](#accessing-the-app)

## Prerequisites

Before getting started, ensure you have the following installed:

- **Node.js** (v16 or higher) - [Download it here](https://nodejs.org/)
- **Python 3.8+** - [Download it here](https://www.python.org/downloads/)

## Setup Instructions

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/your-username/social-posts.git
cd social-posts
```

### 2. Install Frontend Dependencies (Vite)

Navigate to the root of the project and install the frontend dependencies:

```bash
npm install
```

### 3. Set Up Python Virtual Environment (Backend)

#### On Mac:

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

#### On Windows:

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

## Starting the Servers

### 1. Start the Frontend (Vite)

Run the following command to start the frontend development server:

```bash
npm run dev
```

This will start the frontend on http://localhost:5173/.

### 2. Start the Backend (Python)

#### On Mac:

```bash
./.venv/bin/python backend/app.py
```

#### On Mac/Windows (if virtual environment is activated):

```bash
python backend/app.py
```

This will start the backend API on http://127.0.0.1:8000/.

## Accessing the App

Once the servers are running:

- **Frontend (UI)**: http://localhost:5173/
- **Backend API**: http://127.0.0.1:8000/
