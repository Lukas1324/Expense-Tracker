ausgaben = "CREATE TABLE IF NOT EXISTS ausgaben " \
"(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
"amount REAL, " \
"content TEXT, " \
"date DATE, " \
"created_at DATE DEFAULT CURRENT_TIMESTAMP," \
"label TEXT)"

tabellen = [ausgaben]