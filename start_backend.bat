@echo off

start "" http://127.0.0.1:8000/docs

call venv\Scripts\activate

uvicorn app.main:app --reload