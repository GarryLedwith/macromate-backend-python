# MacroMate Backend (Python & FastAPI)

This is the **Python backend** for MacroMate

---
## Features

- FastAPI-powered backend
- Modular routing 
- MongoDB Atlas integration via `pymongo`
- Environment variables for secrets 


## 📁 Project Structure

macromate-backend-python/
├── app/

│ ├── main.py # FastAPI app entrypoint

│ ├── routes/ # API routes (e.g., food, goals, weights)

│ ├── services/ # Business logic (e.g., Edamam integration)

│ ├── models/ # Pydantic models for validation

│ └── db.py # MongoDB connection

├── .env # Environment variables (excluded from Git)

├── requirements.txt # Python dependencies

└── README.md # This file

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-user/macromate-backend-python.git
cd macromate-backend-python
```
### 2. Create & Activate Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Configure Environment Variables
```
Create a .env file in the project root:
```
MONGO_URI=mongodb+srv://<user>:<pass>@<cluster>.mongodb.net/macromate_db
EDAMAM_APP_ID=your_edamam_app_id
EDAMAM_APP_KEY=your_edamam_app_key


#### Running the Server (Dev Mode)
```
uvicorn app.main:app --reload
```
App will run at: http://localhost:8000

Swagger Docs: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

### Dependencies
FastAPI
Uvicorn
Pymongo
Python Dotenv

### Future AI Features (Planned)
Smart meal labeling (based on time)

Daily macro summary via GPT

Personalized macro adjustment recommender

Food log anomaly detection

Nutrition chatbot assistant

## License
MIT License © 2025 Garry Ledwith



