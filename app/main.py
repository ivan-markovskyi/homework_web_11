from fastapi import FastAPI, Depends, Request
from api.contact_items import router as contact_router
from models import contact
from depenedencies.database import engine, SessionLocal, get_db

contact.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(contact_router, prefix="/contact")


@app.get("/")
async def health_check():
    print()
    return {"OK": True}
