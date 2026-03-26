from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.backend.routes.chat import router as chat_router

app = FastAPI()

# CORS configuration
origins = ["*"]  # Update this with your allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Integrate chat routes
app.include_router(chat_router)
