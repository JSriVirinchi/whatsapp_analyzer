# WhatsApp Chat Analyzer

A privacy-first web application for analyzing WhatsApp chat exports.

## Step 1 - Project Scaffolding ✅

This step sets up the basic project structure with:
- Frontend: React 18 + TypeScript + Vite + TailwindCSS v3 + shadcn/ui
- Backend: FastAPI with CORS enabled
- Health endpoint for testing

**Fixed Issues:**
- Resolved TailwindCSS v4 PostCSS configuration issues by downgrading to v3
- Both servers now run correctly without errors

## Setup Instructions

### Backend
1. Install Python dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

2. Run the backend server:
   ```bash
   python3 -m uvicorn backend.main:app --reload --port 8000
   ```

3. Test the health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

### Frontend
1. Install dependencies:
   ```bash
   cd frontend && npm install
   ```

2. Run the development server:
   ```bash
   cd frontend && npm run dev
   ```

3. Open http://localhost:5173 in your browser

### Running Both Servers
Open two terminal windows:
- Terminal 1: `python3 -m uvicorn backend.main:app --reload --port 8000`
- Terminal 2: `cd frontend && npm run dev`

## Project Structure
```
whatsapp_analyzer/
├── backend/                      # Backend Python code
│   ├── __init__.py
│   ├── main.py                   # FastAPI application
│   └── requirements.txt          # Python dependencies
├── frontend/                     # Frontend React code
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── lib/
│   │       └── utils.ts          # shadcn/ui utilities
│   ├── components.json           # shadcn/ui configuration
│   ├── tailwind.config.js        # TailwindCSS configuration
│   ├── package.json              # Frontend dependencies
│   └── vite.config.ts            # Vite configuration
└── README.md                     # This file
```

## Next Steps
- Step 2: File upload API
- Step 3: WhatsApp parser
- Step 4: Global summary metrics
- And more...
