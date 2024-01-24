from repo.contacts import ContactRepo
from schemas.contact import Contact, ContactCreate, ContactUpdate


class ContactService:
    def __init__(self, db):
        self.repo = ContactRepo(db=db)

    def get_all_contacts(self) -> list[Contact]:
        all_contacts_from_db = self.repo.get_all()
        result = [Contact.from_orm(item) for item in all_contacts_from_db]
        return result

    def create_new(self, contact_item: ContactCreate) -> Contact:
        new_item_from_db = self.repo.create(contact_item)
        contact_item = Contact.from_orm(new_item_from_db)
        return contact_item

    def get_by_id(self, id: int) -> Contact:
        contact_item = self.repo.get_by_id(id)
        return Contact.from_orm(contact_item)

    def update_contact(self, id: int, contact_item: ContactUpdate) -> Contact:
        contact_item = self.repo.update_contact(id, contact_item)
        return Contact.from_orm(contact_item)

    def contact_delete(self, id: int):
        self.repo.del_by_id(id)

    def find_contact(self, search_key: str) -> list[Contact]:
        all_found_contacts = self.repo.find_contact(search_key)
        result = [Contact.from_orm(item) for item in all_found_contacts]
        return result

    def get_birthdays(self) -> list[Contact]:
        all_contacts = self.repo.get_birthdays()
        result = [Contact.from_orm(item) for item in all_contacts]
        return result
