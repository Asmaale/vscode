import sqlite3

# إنشاء اتصال بقاعدة البيانات أو فتحها إذا كانت موجودة
conn = sqlite3.connect('appointments.db')
cursor = conn.cursor()

# إنشاء جدول لتخزين بيانات المواعيد
cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    status TEXT
)
''')

conn.commit()
conn.close()
