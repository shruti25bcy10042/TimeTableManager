# Timetable Manager for Students

# A timetable will store all classes as dictionaries inside a list
timetable = []

def add_class(subject, day, start_time, end_time):
    # Check if new class clashes with existing ones
    for cls in timetable:
        if cls["day"] == day:
            # Check if time overlaps
            if not (end_time <= cls["start"] or start_time >= cls["end"]):
                print(f"❌ Clash detected with {cls['subject']} ({cls['start']} - {cls['end']}) on {day}")
                return

    # If no clash, add the class
    timetable.append({
        "subject": subject,
        "day": day,
        "start": start_time,
        "end": end_time
    })
    print(f"✔ {subject} added successfully to your timetable.")

def display_timetable():
    if not timetable:
        print("Your timetable is empty.")
        return
    
    print("\n--- Your Timetable ---")
    for cls in timetable:
        print(f"{cls['day']}: {cls['subject']} ({cls['start']} - {cls['end']})")

# Main Program

while True:
    print("\n1. Add Class")
    print("2. View Timetable")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        day = input("Enter day (Mon/Tue/Wed/Thu/Fri): ")

        start_time = float(input("Enter start time (24 hr format, e.g., 9.5 for 9:30): "))
        end_time = float(input("Enter end time (24 hr format): "))

        add_class(subject, day, start_time, end_time)

    elif choice == "2":
        display_timetable()

    elif choice == "3":
        print("Exiting Timetable Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")