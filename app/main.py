from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, timedelta
from typing import Optional
from app.core.supabase_client import supabase

app = FastAPI(
    title="OT DETA Backend",
    description="Surgical OT Management System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "OT DETA API", "status": "running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Server is running!"}

@app.get("/api/doctors/")
async def get_doctors():
    try:
        response = supabase.table('doctors')\
            .select('*')\
            .eq('is_active', True)\
            .order('name')\
            .execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
