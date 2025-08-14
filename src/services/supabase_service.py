from supabase import create_client
from src.config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def insert_row(table_name, name, phone_number):
    _ = (
        supabase.table(table_name)
        .insert({"name": name, "phone_number": phone_number})
        .execute()
    )

def select_all(table_name):
    return (    
        supabase.table(table_name)
        .select("*")
        .execute())


if __name__ == "__main__":
    pass