from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WhatsApp Chat Analyzer",
    description="Privacy-first WhatsApp chat analysis API",
    version="1.0.0"
)

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "OK", "message": "WhatsApp Chat Analyzer API is running"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "WhatsApp Chat Analyzer API"}
