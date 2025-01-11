import sqlite3

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct TEXT NOT NULL
    )
''')

cursor.executemany('''
    INSERT INTO questions (text, option_a, option_b, option_c, option_d, correct)
    VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("Python'da yapay zeka geliştirmek için en yaygın kullanılan kütüphane hangisidir?",
     "NumPy", "TensorFlow", "Flask", "Pandas", "TensorFlow"),
    ("Bir yapay zeka modelinin doğruluğunu ölçmek için kullanılan metriklerden biri nedir?",
     "Eğitim Hızı", "Doğruluk (Accuracy)", "Grafik Çizimi", "Bellek Kullanımı", "Doğruluk (Accuracy)"),
    ("Python'da yapay zeka için veri hazırlarken kullanılan kütüphane hangisidir?",
     "Matplotlib", "Scikit-learn", "Seaborn", "PyTorch", "Scikit-learn"),
    ("Yapay sinir ağları (Artificial Neural Networks) oluşturmak için kullanılan Python kütüphanesi hangisidir?",
     "NumPy", "TensorFlow", "OpenCV", "Keras", "Keras")
])

conn.commit()
conn.close()

print("Veritabanı başarıyla oluşturuldu ve sorular eklendi!")