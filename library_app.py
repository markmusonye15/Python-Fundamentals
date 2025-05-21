import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import sql
from config import DB_CONF

def get_connection():
    """
    Establishes a connection to the PostgreSQL database using the provided configuration.
    
    Returns:
        conn: A connection object to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(**DB_CONF)
        print("CONNECTED SUCCESSFULLY")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def fetch_books():
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM books;")
        print("FETCHED BOOKS", cur.fetchall())
        return cur.fetchall()


def add_books(id, title, isbn, published_date, total_copies, available_copies, category_id):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO BOOKS (id, title, isbn, published_date, total_copies, available_copies, category_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
                    (id, title, isbn, published_date, total_copies, available_copies, category_id)
                    )


def add_category(title, description):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO categories (title, description)
            VALUES (%s, %s)
            RETURNING id;
        """,
                    (title, description)
                    )

# add_category("Self Improvement", "A self improvement category")
add_books(1, "Atomic Habits", "KNSJDVJSJBHD200", "10-05-1998", 1000, 50, 1)
