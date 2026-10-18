"""
AI-Based Career Recommendation System (Core Python)
---------------------------------------------------
Constraints followed: no classes, no try/except, no external libraries.
(sqlite3 and datetime ship with Python, and are used only for the optional bonus.)
"""

import sqlite3
from datetime import datetime
import random

DB_NAME = "career.db"

# ------------------------------------------------------------------
# DATA: options shown to the user
# ------------------------------------------------------------------
SUBJECTS = ["Mathematics", "Physics", "Biology", "Chemistry", "Computer Science",
            "English", "Business Studies", "Art", "Economics", "Education"]

SKILLS = ["Problem Solving", "Communication", "Creativity", "Mathematics",
          "Programming", "Designing", "Networking", "Security", "Research",
          "Leadership"]

INTERESTS = ["Technology", "Healthcare", "Business", "Arts", "Teaching"]

WORK_STYLES = ["Office Work", "Remote Work", "Team-Based Work",
               "Creative Work", "Field Work"]

QUOTES = [
    "The future belongs to those who prepare for it today.",
    "Choose a job you love, and you will never work a day in your life.",
    "Skills pay the bills, but passion builds the career.",
    "Every expert was once a beginner.",
    "Your career is a journey, not a destination.",
]

# ------------------------------------------------------------------
# DATA: career dataset (nested dictionary)
# "match" holds keywords (lowercase) and how much each is worth.
# ------------------------------------------------------------------
CAREERS = {
    "Data Scientist": {
        "description": "Analyzes data to solve business problems and predict trends.",
        "skills": "Python, Statistics, Machine Learning",
        "scope": "High demand in AI and analytics industries.",
        "match": {"mathematics": 2, "programming": 2, "problem solving": 1,
                  "research": 1, "technology": 1, "computer science": 1,
                  "remote work": 1},
    },
    "AI Engineer": {
        "description": "Builds intelligent systems that learn from data.",
        "skills": "Python, Deep Learning, Mathematics",
        "scope": "One of the fastest-growing fields worldwide.",
        "match": {"programming": 2, "mathematics": 2, "problem solving": 1,
                  "technology": 1, "computer science": 1, "research": 1,
                  "remote work": 1},
    },
    "Web Developer": {
        "description": "Designs and builds websites and web applications.",
        "skills": "HTML, CSS, JavaScript, Problem Solving",
        "scope": "Strong demand with plenty of freelance and remote work.",
        "match": {"programming": 2, "designing": 1, "creativity": 1,
                  "technology": 1, "computer science": 1, "remote work": 1,
                  "problem solving": 1},
    },
    "Software Engineer": {
        "description": "Designs, develops and tests software systems.",
        "skills": "Programming, Algorithms, Teamwork",
        "scope": "Steady global demand across nearly every industry.",
        "match": {"programming": 2, "problem solving": 2, "technology": 1,
                  "computer science": 1, "team-based work": 1,
                  "mathematics": 1},
    },
    "Doctor": {
        "description": "Diagnoses and treats illnesses and promotes health.",
        "skills": "Biology, Communication, Decision Making",
        "scope": "Always in demand; excellent respect and job security.",
        "match": {"biology": 2, "healthcare": 3, "chemistry": 1,
                  "communication": 1, "research": 1, "field work": 1,
                  "problem solving": 1},
    },
    "Graphic Designer": {
        "description": "Creates visual content for brands, media and products.",
        "skills": "Creativity, Adobe Tools, Typography",
        "scope": "Growing demand in advertising, media and digital branding.",
        "match": {"creativity": 2, "designing": 2, "art": 2, "arts": 2,
                  "creative work": 2, "remote work": 1},
    },
    "Digital Marketer": {
        "description": "Promotes products and brands through online channels.",
        "skills": "Communication, SEO, Social Media, Analytics",
        "scope": "Booming as businesses move online.",
        "match": {"communication": 2, "business": 2, "business studies": 1,
                  "creativity": 1, "economics": 1, "remote work": 1,
                  "team-based work": 1},
    },
    "Cybersecurity Analyst": {
        "description": "Protects systems and networks from cyber attacks.",
        "skills": "Networking, Security, Problem Solving",
        "scope": "Critical shortage of professionals worldwide.",
        "match": {"security": 3, "networking": 3, "problem solving": 1,
                  "technology": 1, "computer science": 1, "programming": 1},
    },
    "Accountant": {
        "description": "Manages financial records, taxes and audits.",
        "skills": "Mathematics, Accuracy, Financial Reporting",
        "scope": "Stable demand in every business and organization.",
        "match": {"mathematics": 2, "economics": 2, "business": 2,
                  "business studies": 2, "office work": 1,
                  "problem solving": 1},
    },
    "Teacher": {
        "description": "Educates and mentors students in a chosen subject.",
        "skills": "Communication, Patience, Leadership",
        "scope": "Constant demand, with growth in online education.",
        "match": {"teaching": 3, "education": 2, "communication": 2,
                  "leadership": 1, "english": 1, "team-based work": 1},
    },
}


# ------------------------------------------------------------------
# INPUT HELPERS (validation using loops, no try/except)
# ------------------------------------------------------------------
def show_options(options):
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])


def get_name():
    while True:
        name = input("Enter your name: ").strip()
        if name != "" and name.replace(" ", "").isalpha():
            return name.title()
        print("  Invalid name. Please use letters only.")


def get_age():
    while True:
        age = input("Enter your age: ").strip()
        if age.isdigit() and 5 <= int(age) <= 100:
            return int(age)
        print("  Invalid age. Enter a number between 5 and 100.")


def get_qualification():
    while True:
        q = input("Enter your qualification (e.g. Matric, Intermediate, BS): ").strip()
        if q != "":
            return q
        print("  Qualification cannot be empty.")


def get_single_choice(title, options):
    print("\n" + title)
    show_options(options)
    while True:
        choice = input("Enter option number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("  Invalid choice. Pick a number from 1 to " + str(len(options)) + ".")


def get_multi_choice(title, options):
    print("\n" + title + " (enter numbers separated by commas, e.g. 1,3,5)")
    show_options(options)
    while True:
        raw = input("Your choices: ").strip()
        parts = raw.split(",")
        chosen = []
        valid = raw != ""
        for p in parts:
            p = p.strip()
            if p.isdigit() and 1 <= int(p) <= len(options):
                item = options[int(p) - 1]
                if item not in chosen:
                    chosen.append(item)
            else:
                valid = False
        if valid and len(chosen) > 0:
            return chosen
        print("  Invalid input. Use valid numbers separated by commas.")


def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        if answer == "n" or answer == "no":
            return False
        print("  Please type y or n.")


def collect_user_data():
    print("\n--- Basic Information ---")
    user = {}
    user["name"] = get_name()
    user["age"] = get_age()
    user["qualification"] = get_qualification()

    print("\n--- Academic Interests ---")
    user["favorite_subject"] = get_single_choice("Choose your FAVORITE subject:", SUBJECTS)
    user["strong_subject"] = get_single_choice("Choose your STRONGEST subject:", SUBJECTS)

    print("\n--- Skills ---")
    user["skills"] = get_multi_choice("Select your skills:", SKILLS)

    print("\n--- Career Interests ---")
    user["interests"] = get_multi_choice("Select your career interests:", INTERESTS)

    print("\n--- Work Style ---")
    user["work_style"] = get_single_choice("Choose your preferred work style:", WORK_STYLES)
    return user


# ------------------------------------------------------------------
# RECOMMENDATION LOGIC
# ------------------------------------------------------------------
def build_tags(user):
    """Combine all user answers into one lowercase list for matching."""
    tags = []
    tags.append(user["favorite_subject"].lower())
    tags.append(user["strong_subject"].lower())
    tags.append(user["work_style"].lower())
    for s in user["skills"]:
        tags.append(s.lower())
    for i in user["interests"]:
        tags.append(i.lower())
    return tags


def apply_rules(tags, scores):
    """Rule-based bonuses using if statements (10 rules)."""
    if "programming" in tags and "mathematics" in tags:
        scores["Data Scientist"] += 3
        scores["AI Engineer"] += 2
    if "creativity" in tags and "designing" in tags:
        scores["Graphic Designer"] += 3
        scores["Web Developer"] += 1
    if "biology" in tags and "healthcare" in tags:
        scores["Doctor"] += 4
    if "communication" in tags and "business" in tags:
        scores["Digital Marketer"] += 3
    if "technology" in tags and "problem solving" in tags:
        scores["Software Engineer"] += 3
    if "security" in tags and "networking" in tags:
        scores["Cybersecurity Analyst"] += 4
    if "programming" in tags and "designing" in tags:
        scores["Web Developer"] += 3
    if "teaching" in tags and "communication" in tags:
        scores["Teacher"] += 3
    if "mathematics" in tags and "economics" in tags:
        scores["Accountant"] += 3
    elif "business studies" in tags and "office work" in tags:
        scores["Accountant"] += 2
    if "programming" in tags and "research" in tags:
        scores["AI Engineer"] += 2
    return scores


def analyze_careers(user):
    """Return a list of (career, percentage) sorted best first."""
    tags = build_tags(user)
    scores = {}
    for career in CAREERS:
        score = 0
        for keyword in CAREERS[career]["match"]:
            if keyword in tags:
                score += CAREERS[career]["match"][keyword]
        scores[career] = score

    scores = apply_rules(tags, scores)

    results = []
    for career in scores:
        if scores[career] > 0:
            max_points = sum(CAREERS[career]["match"].values()) + 3
            percent = int(scores[career] * 100 / max_points)
            if percent > 100:
                percent = 100
            results.append((career, percent))

    # sort by percentage, highest first (simple selection sort)
    for i in range(len(results)):
        best = i
        for j in range(i + 1, len(results)):
            if results[j][1] > results[best][1]:
                best = j
        results[i], results[best] = results[best], results[i]

    return results[:5]


# ------------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------------
def show_welcome():
    print("=" * 44)
    print("   AI-Based Career Recommendation System")
    print("=" * 44)
    print("Welcome! Answer a few questions about yourself")
    print("and we will suggest careers that suit you.")
    print("Instructions: type the NUMBER of your choice.")
    print("=" * 44)


def show_career_details(results):
    print("\n" + "-" * 44)
    print("RECOMMENDED CAREERS")
    print("-" * 44)
    if len(results) == 0:
        print("No strong match found. Try selecting more skills and interests.")
        return
    for i in range(len(results)):
        name = results[i][0]
        info = CAREERS[name]
        print("\n" + str(i + 1) + ". Recommended Career: " + name +
              "  (Match: " + str(results[i][1]) + "%)")
        print("   Description    : " + info["description"])
        print("   Required Skills: " + info["skills"])
        print("   Future Scope   : " + info["scope"])


def build_report(user, results):
    line = "=" * 44
    text = "\n========== Career Analysis Report ==========\n"
    text += "Name: " + user["name"] + "\n"
    text += "Age: " + str(user["age"]) + "\n"
    text += "Qualification: " + user["qualification"] + "\n"
    text += "Favorite Subject: " + user["favorite_subject"] + "\n"
    text += "Strongest Subject: " + user["strong_subject"] + "\n"
    text += "Skills: " + ", ".join(user["skills"]) + "\n"
    text += "Interests: " + ", ".join(user["interests"]) + "\n"
    text += "Work Style: " + user["work_style"] + "\n"
    text += "Recommended Careers:\n"
    if len(results) == 0:
        text += "  None found\n"
    for i in range(len(results)):
        text += "  " + str(i + 1) + ". " + results[i][0] + " (" + str(results[i][1]) + "%)\n"
    text += line + "\n"
    return text


def save_report_to_file(user, report):
    filename = user["name"].replace(" ", "_").lower() + "_career_report.txt"
    f = open(filename, "w")
    f.write(report)
    f.close()
    print("Report saved to " + filename)


# ------------------------------------------------------------------
# DATABASE (SQLite, bonus)
# ------------------------------------------------------------------
def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            qualification TEXT,
            favorite_subject TEXT,
            strong_subject TEXT,
            skills TEXT,
            interest TEXT,
            career TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_to_database(user, results):
    careers = []
    for r in results:
        careers.append(r[0])
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students
        (name, age, qualification, favorite_subject, strong_subject,
         skills, interest, career, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user["name"], user["age"], user["qualification"],
          user["favorite_subject"], user["strong_subject"],
          ", ".join(user["skills"]), ", ".join(user["interests"]),
          ", ".join(careers), datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()
    print("Record saved to database.")


def print_rows(rows):
    if len(rows) == 0:
        print("No records found.")
        return
    for row in rows:
        print("-" * 44)
        print("ID: " + str(row[0]) + " | " + row[9])
        print("Name: " + row[1] + " | Age: " + str(row[2]) + " | " + row[3])
        print("Favorite/Strong Subject: " + row[4] + " / " + row[5])
        print("Skills: " + row[6])
        print("Interests: " + row[7])
        print("Recommended: " + row[8])
    print("-" * 44)


def view_all_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    print_rows(rows)


def search_records():
    name = input("Enter name to search: ").strip()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("%" + name + "%",))
    rows = cursor.fetchall()
    conn.close()
    print_rows(rows)


def delete_record():
    rec_id = input("Enter the record ID to delete: ").strip()
    if not rec_id.isdigit():
        print("Invalid ID.")
        return
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (int(rec_id),))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted > 0:
        print("Record deleted.")
    else:
        print("No record with that ID.")


# ------------------------------------------------------------------
# EXTRA: career search
# ------------------------------------------------------------------
def career_search():
    word = input("Search careers by keyword: ").strip().lower()
    found = False
    for name in CAREERS:
        info = CAREERS[name]
        if word != "" and (word in name.lower() or word in info["description"].lower()
                           or word in info["skills"].lower()):
            print("\n- " + name + ": " + info["description"])
            print("  Skills: " + info["skills"])
            found = True
    if not found:
        print("No careers matched that keyword.")


# ------------------------------------------------------------------
# MAIN FLOW
# ------------------------------------------------------------------
def run_analysis():
    again = True
    while again:
        user = collect_user_data()
        print("\nAnalyzing your profile...")
        results = analyze_careers(user)
        show_career_details(results)

        report = build_report(user, results)
        print(report)

        save_to_database(user, results)
        if ask_yes_no("Save the report to a text file?"):
            save_report_to_file(user, report)

        print("\nMotivation: " + random.choice(QUOTES))
        again = ask_yes_no("\nWould you like to try again?")


def main_menu():
    init_database()
    show_welcome()
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Get career recommendation")
        print("2. View previous records")
        print("3. Search saved users")
        print("4. Search careers")
        print("5. Delete a record")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            run_analysis()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            search_records()
        elif choice == "4":
            career_search()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            print("\nThank you for using the Career Recommendation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main_menu()