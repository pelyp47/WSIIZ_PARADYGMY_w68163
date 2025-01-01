import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('hospital.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)''')

c.execute('''CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    duration INTEGER NOT NULL,
    patient_name TEXT NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
)''')

conn.commit()

def admin_menu():
    while True:
        print("\n=== Menu Administratora ===")
        print("1. Dodaj lekarza")
        print("2. Wyświetl harmonogram lekarza")
        print("3. Wyświetl listę lekarzy")
        print("4. Wyloguj")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            add_doctor()
        elif choice == '2':
            view_schedule()
        elif choice == '3':
            list_doctors()
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór!")

def add_doctor():
    name = input("Podaj nazwisko lekarza: ")
    c.execute("INSERT INTO doctors (name) VALUES (?)", (name,))
    conn.commit()
    print("Lekarz został dodany.")

def view_schedule():
    doctor_id = int(input("Podaj ID lekarza: "))
    c.execute("SELECT * FROM appointments WHERE doctor_id = ?", (doctor_id,))
    appointments = c.fetchall()
    if appointments:
        print("\nHarmonogram lekarza:")
        for appt in appointments:
            print(f"ID wizyty: {appt[0]}, Data: {appt[2]}, Godzina: {appt[3]}, Czas trwania: {appt[4]}h, Pacjent: {appt[5]}")
    else:
        print("Brak wizyt dla tego lekarza.")

def list_doctors():
    c.execute("SELECT * FROM doctors")
    doctors = c.fetchall()
    if doctors:
        print("\nLista lekarzy:")
        for doc in doctors:
            print(f"ID: {doc[0]}, Nazwisko: {doc[1]}")
    else:
        print("Brak lekarzy w bazie danych.")

def patient_menu():
    while True:
        print("\n=== Menu Pacjenta ===")
        print("1. Wyświetl listę lekarzy")
        print("2. Zarezerwuj wizytę")
        print("3. Wyświetl harmonogram lekarza na najbliższy tydzień")
        print("4. Wyloguj")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            list_doctors()
        elif choice == '2':
            book_appointment()
        elif choice == '3':
            view_week_schedule()
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór!")

def book_appointment():
    list_doctors()
    doctor_id = int(input("Podaj ID lekarza, do którego chcesz się umówić: "))
    date = input("Podaj datę wizyty (YYYY-MM-DD): ")
    time = input("Podaj godzinę wizyty (HH:MM): ")
    duration = int(input("Podaj czas trwania wizyty w godzinach: "))
    patient_name = input("Podaj swoje imię i nazwisko: ")

    today = datetime.now()
    appointment_date = datetime.strptime(date, "%Y-%m-%d")
    if appointment_date < today or appointment_date > today + timedelta(days=7):
        print("Wizytę można rezerwować tylko na najbliższy tydzień.")
        return

    c.execute("SELECT * FROM appointments WHERE doctor_id = ? AND date = ?", (doctor_id, date))
    appointments = c.fetchall()
    is_available = True

    available_slots = []
    start_time = datetime.strptime("08:00", "%H:%M")
    end_time = datetime.strptime("18:00", "%H:%M")

    for hour in range(8, 18):
        slot_start = datetime.strptime(f"{hour:02}:00", "%H:%M")
        slot_end = slot_start + timedelta(hours=1)
        available_slots.append((slot_start, slot_end))

    for appt in appointments:
        appt_start = datetime.strptime(appt[3], "%H:%M")
        appt_duration = timedelta(hours=appt[4])
        appt_end = appt_start + appt_duration
        available_slots = [(start, end) for start, end in available_slots if end <= appt_start or start >= appt_end]

    new_start = datetime.strptime(time, "%H:%M")
    new_end = new_start + timedelta(hours=duration)

    if not any(start <= new_start < end and new_end <= end for start, end in available_slots):
        print("Lekarz jest zajęty w wybranym czasie. Dostępne godziny:")
        for start, end in available_slots:
            print(f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
        return

    c.execute("INSERT INTO appointments (doctor_id, date, time, duration, patient_name) VALUES (?, ?, ?, ?, ?)", (doctor_id, date, time, duration, patient_name))
    conn.commit()
    print("Wizyta została zarezerwowana.")

def view_week_schedule():
    doctor_id = int(input("Podaj ID lekarza: "))
    today = datetime.now()
    week_later = today + timedelta(days=7)
    c.execute("SELECT * FROM appointments WHERE doctor_id = ? AND date BETWEEN ? AND ?", (doctor_id, today.strftime("%Y-%m-%d"), week_later.strftime("%Y-%m-%d")))
    appointments = c.fetchall()

    available_slots = []
    for day_offset in range(8):
        current_date = (today + timedelta(days=day_offset)).strftime("%Y-%m-%d")
        day_appointments = [appt for appt in appointments if appt[2] == current_date]

        day_slots = []
        start_time = datetime.strptime("08:00", "%H:%M")
        end_time = datetime.strptime("18:00", "%H:%M")
        for hour in range(8, 18):
            slot_start = datetime.strptime(f"{hour:02}:00", "%H:%M")
            slot_end = slot_start + timedelta(hours=1)
            day_slots.append((slot_start, slot_end))

        for appt in day_appointments:
            appt_start = datetime.strptime(appt[3], "%H:%M")
            appt_duration = timedelta(hours=appt[4])
            appt_end = appt_start + appt_duration
            day_slots = [(start, end) for start, end in day_slots if end <= appt_start or start >= appt_end]

        for slot_start, slot_end in day_slots:
            available_slots.append((current_date, slot_start.strftime("%H:%M"), slot_end.strftime("%H:%M")))

    if available_slots:
        print("\nDostępne godziny lekarza na najbliższy tydzień:")
        for date, start, end in available_slots:
            print(f"Data: {date}, {start} - {end}")
    else:
        print("Brak wolnych godzin w najbliższym tygodniu.")

def main():
    while True:
        print("\n=== System Rezerwacji Wizyt ===")
        print("1. Zaloguj jako administrator")
        print("2. Zaloguj jako pacjent")
        print("3. Wyjdź")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            username = input("Login: ")
            password = input("Hasło: ")
            if username == 'admin' and password == 'admin':
                admin_menu()
            else:
                print("Nieprawidłowy login lub hasło!")
        elif choice == '2':
            username = input("Login: ")
            password = input("Hasło: ")
            if username == 'user' and password == 'user':
                patient_menu()
            else:
                print("Nieprawidłowy login lub hasło!")
        elif choice == '3':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór!")

if __name__ == "__main__":
    main()

conn.close()