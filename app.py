from src.services.supabase_service import get_all_contacts
from src.services.zapi_service import send_message


def main():
    table = 'contacts'

    contacts = get_all_contacts(table)

    for user in contacts:
        msg = f'Olá {user.get("name")}, tudo bem com você?'
        
        send_message(msg, user.get("phone_number"))


if __name__ == "__main__":
    main()
