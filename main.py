try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from routes import router
except Exception as e:
    print(f"Import error in main.py: {e}")
    raise

app = FastAPI()

# Configure CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)