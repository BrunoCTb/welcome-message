from supabase import create_client
from src.config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def get_all_contacts(table_name, size_limit=3):
    resp = (
        supabase.table("contacts")
        .select("*", count="exact")
        .limit(size_limit)
        .execute()
    )

    if (resp.count < 1):
        print('Não há contatos no db')
        return []

    return resp.data
    


if __name__ == "__main__":
    get_all_contacts('contact')