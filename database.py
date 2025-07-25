
import sqlite3

conn = sqlite3.connect('bot.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS downloads (
    url TEXT,
    platform TEXT,
    count INTEGER DEFAULT 1
)''')
conn.commit()

def add_user(user_id):
    cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()

def count_users():
    cursor.execute('SELECT COUNT(*) FROM users')
    return cursor.fetchone()[0]

def add_download(url, platform):
    cursor.execute('SELECT count FROM downloads WHERE url = ? AND platform = ?', (url, platform))
    result = cursor.fetchone()
    if result:
        cursor.execute('UPDATE downloads SET count = count + 1 WHERE url = ? AND platform = ?', (url, platform))
    else:
        cursor.execute('INSERT INTO downloads (url, platform) VALUES (?, ?)', (url, platform))
    conn.commit()

def get_top_download(platform):
    cursor.execute('SELECT url, count FROM downloads WHERE platform = ? ORDER BY count DESC LIMIT 1', (platform,))
    return cursor.fetchone()
