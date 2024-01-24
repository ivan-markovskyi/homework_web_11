from fastapi import APIRouter, Depends
from schemas.contact import Contact, ContactCreate, ContactUpdate
from depenedencies.database import get_db, SessionLocal
from services.contacts import ContactService

router = APIRouter()


@router.get("/")
async def list_contacts(db: SessionLocal = Depends(get_db)) -> list[Contact]:
    contact_items = ContactService(db=db).get_all_contacts()
    return contact_items


@router.get("/{id}")
async def get_detail(id: int, db: SessionLocal = Depends(get_db)) -> Contact:
    contact_item = ContactService(db=db).get_by_id(id)
    return contact_item


@router.post("/")
async def create_contact(
    contact_item: ContactCreate, db: SessionLocal = Depends(get_db)
) -> Contact:
    new_item = ContactService(db=db).create_new(contact_item)
    return new_item


@router.put("/{id}")
async def update_contact(
    id: int, contact_item: ContactUpdate, db: SessionLocal = Depends(get_db)
) -> Contact:
    updated_item = ContactService(db=db).update_contact(id, contact_item)
    return updated_item


@router.delete("/{id}")
async def contact_delete(id: int, db: SessionLocal = Depends(get_db)):
    ContactService(db=db).contact_delete(id)
    # return {"ok": True}


@router.get("/search/")
async def find_contact(
    search_key: str, db: SessionLocal = Depends(get_db)
) -> list[Contact]:
    contact_items = ContactService(db=db).find_contact(search_key)
    return contact_items


@router.get("/birthdays/")
async def get_birthdays(db: SessionLocal = Depends(get_db)) -> list[Contact]:
    contact_items = ContactService(db=db).get_birthdays()
    return contact_items
