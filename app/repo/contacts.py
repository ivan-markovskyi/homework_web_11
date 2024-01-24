from datetime import datetime
from models.contact import ContactDB
from sqlalchemy import or_


class ContactRepo:
    def __init__(self, db) -> None:
        self.db = db

    def get_all(self) -> list[ContactDB]:
        return self.db.query(ContactDB).filter()

    def create(self, contact_item):
        new_item = ContactDB(**contact_item.dict())
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def get_by_id(self, id):
        return self.db.query(ContactDB).filter(ContactDB.id == id).first()

    def update_contact(self, id, contact_item):
        current_contact = self.db.query(ContactDB).filter(ContactDB.id == id).first()
        if current_contact:
            current_contact.first_name = contact_item.first_name
            current_contact.last_name = contact_item.last_name
            current_contact.email = contact_item.email
            current_contact.phone_number = contact_item.phone_number
            current_contact.birthday = contact_item.birthday
            current_contact.description = contact_item.description
        self.db.add(current_contact)
        self.db.commit()
        self.db.refresh(current_contact)
        return current_contact

    def del_by_id(self, id):
        current_contact = self.db.query(ContactDB).filter(ContactDB.id == id).first()
        self.db.delete(current_contact)
        self.db.commit()

    def find_contact(self, search_key):
        contacts = (
            self.db.query(ContactDB)
            .filter(
                or_(
                    ContactDB.first_name.ilike(f"%{search_key}%"),
                    ContactDB.last_name.ilike(f"%{search_key}%"),
                    ContactDB.email.ilike(f"%{search_key}%"),
                )
            )
            .all()
        )

        return contacts

    def get_birthdays(self):
        result = []
        current_date = datetime.now()
        contacts = self.db.query(ContactDB).filter()
        for contact in contacts:
            contact_bd = datetime.strptime(contact.birthday, "%Y-%m-%d")
            contact_bd = contact_bd.replace(year=current_date.year)
            delta_days = contact_bd - current_date

            if (delta_days.days <= 6) and (delta_days.days >= 0):
                result.append(contact)
        return result
