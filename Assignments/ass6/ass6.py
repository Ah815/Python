"""
Employee Attendance & Payroll Management System
Core Python only — no OOP, no databases, no Pandas/NumPy.
Files used:
    data/employees.json
    data/attendance.json
    data/payroll.json
    salary_slips/*.txt
"""

import json
import os
from datetime import datetime, date

# ---------------------------------------------------------------- constants
DATA_DIR      = "data"
SLIP_DIR      = "salary_slips"
EMP_FILE      = os.path.join(DATA_DIR, "employees.json")
ATT_FILE      = os.path.join(DATA_DIR, "attendance.json")
PAY_FILE      = os.path.join(DATA_DIR, "payroll.json")

COMPANY_NAME      = "Acme Corporation Pvt. Ltd."
WORKING_DAYS      = 26
STANDARD_HOURS    = 8
VALID_STATUSES    = ("Present", "Absent", "Leave", "Half Day")


# ================================================================ file I/O
def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(SLIP_DIR, exist_ok=True)


def load_json(path, default):
    """Load JSON; return default on missing / empty / invalid file."""
    try:
        if not os.path.exists(path):
            return default
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return default
            data = json.loads(content)
            return data if isinstance(data, type(default)) else default
    except (json.JSONDecodeError, OSError) as e:
        print(f"  [warn] Could not read {path}: {e}. Using empty data.")
        return default


def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        print(f"  [error] Could not save {path}: {e}")


# Global in-memory stores
employees  = {}   # emp_id -> dict
attendance = []   # list of dicts
payroll    = []   # list of dicts


def load_all():
    global employees, attendance, payroll
    ensure_dirs()
    employees  = load_json(EMP_FILE, {})
    attendance = load_json(ATT_FILE, [])
    payroll    = load_json(PAY_FILE, [])


def save_all():
    save_json(EMP_FILE, employees)
    save_json(ATT_FILE, attendance)
    save_json(PAY_FILE, payroll)


# ================================================================ helpers
def pause():
    input("\nPress Enter to continue...")


def safe_float(prompt, positive=True):
    while True:
        try:
            val = float(input(prompt).strip())
            if positive and val <= 0:
                print("  Value must be positive.")
                continue
            return val
        except ValueError:
            print("  Invalid number. Try again.")


def safe_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  Invalid integer. Try again.")


def ask_date(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("  Use format YYYY-MM-DD.")


def ask_month(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return datetime.strptime(s, "%Y-%m").strftime("%Y-%m")
        except ValueError:
            print("  Use format YYYY-MM.")


def ask_time(prompt):
    """Accept HH:MM (24h) or hh:MM AM/PM; return minutes since midnight."""
    s = input(prompt).strip().upper()
    for fmt in ("%H:%M", "%I:%M %p", "%I:%M%p"):
        try:
            t = datetime.strptime(s, fmt)
            return t.hour * 60 + t.minute
        except ValueError:
            continue
    return None


def minutes_to_str(m):
    h, mm = divmod(m, 60)
    return f"{h:02d}:{mm:02d}"


def next_emp_id():
    if not employees:
        return "EMP001"
    nums = [int(k[3:]) for k in employees if k.startswith("EMP") and k[3:].isdigit()]
    return f"EMP{max(nums) + 1:03d}"


# ================================================================ Module 1: Employee Management
def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = next_emp_id()
    print(f"  Generated Employee ID: {emp_id}")
    name = input("  Name: ").strip()
    if not name:
        print("  Name cannot be empty."); return
    dept = input("  Department: ").strip()
    desig = input("  Designation: ").strip()
    salary = safe_float("  Monthly Basic Salary: ")
    jdate = ask_date("  Joining Date (YYYY-MM-DD): ")

    employees[emp_id] = {
        "id": emp_id,
        "name": name,
        "department": dept,
        "designation": desig,
        "salary": salary,
        "joining_date": jdate.isoformat(),
    }
    save_all()
    print(f"  ✓ Employee {emp_id} added.")


def search_employee():
    emp_id = input("\nEnter Employee ID: ").strip().upper()
    emp = employees.get(emp_id)
    if not emp:
        print("  Employee not found."); return
    print_employee(emp)


def print_employee(e):
    print(f"  ID: {e['id']} | Name: {e['name']} | Dept: {e['department']} | "
          f"Desig: {e['designation']} | Salary: {e['salary']:.2f} | Joined: {e['joining_date']}")


def display_employees():
    if not employees:
        print("\n  No employees registered."); return
    print("\n--- All Employees ---")
    for e in employees.values():
        print_employee(e)


def update_employee():
    emp_id = input("\nEmployee ID to update: ").strip().upper()
    emp = employees.get(emp_id)
    if not emp:
        print("  Not found."); return
    print("  Leave blank to keep current value.")
    name = input(f"  Name [{emp['name']}]: ").strip()
    if name: emp['name'] = name
    dept = input(f"  Department [{emp['department']}]: ").strip()
    if dept: emp['department'] = dept
    desig = input(f"  Designation [{emp['designation']}]: ").strip()
    if desig: emp['designation'] = desig
    sal_in = input(f"  Salary [{emp['salary']}]: ").strip()
    if sal_in:
        try:
            s = float(sal_in)
            if s <= 0:
                print("  Salary must be positive; unchanged.")
            else:
                emp['salary'] = s
        except ValueError:
            print("  Invalid salary; unchanged.")
    save_all()
    print("  ✓ Updated.")


def employee_menu():
    while True:
        print("\n=== Employee Management ===")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Display All Employees")
        print("0. Back")
        ch = input("Choice: ").strip()
        if ch == "1": add_employee()
        elif ch == "2": search_employee()
        elif ch == "3": update_employee()
        elif ch == "4": display_employees()
        elif ch == "0": return
        else: print("  Invalid choice.")


# ================================================================ Module 2: Attendance
def record_attendance():
    print("\n--- Record Attendance ---")
    emp_id = input("  Employee ID: ").strip().upper()
    if emp_id not in employees:
        print("  Unknown employee."); return
    d = ask_date("  Date (YYYY-MM-DD): ")
    status = input("  Status (Present/Absent/Leave/Half Day): ").strip().title()
    if status not in VALID_STATUSES:
        print("  Invalid status."); return

    for a in attendance:
        if a["emp_id"] == emp_id and a["date"] == d.isoformat():
            print("  Duplicate: attendance already recorded for that date."); return

    record = {
        "emp_id": emp_id,
        "date": d.isoformat(),
        "status": status,
        "check_in": None,
        "check_out": None,
        "hours": 0.0,
        "overtime": 0.0,
    }
    attendance.append(record)
    save_all()
    print("  ✓ Attendance recorded.")


def record_check_in_out():
    print("\n--- Record Check-In / Check-Out ---")
    emp_id = input("  Employee ID: ").strip().upper()
    if emp_id not in employees:
        print("  Unknown employee."); return
    d = ask_date("  Date (YYYY-MM-DD): ").isoformat()

    rec = None
    for a in attendance:
        if a["emp_id"] == emp_id and a["date"] == d:
            rec = a; break
    if rec is None:
        rec = {"emp_id": emp_id, "date": d, "status": "Present",
               "check_in": None, "check_out": None, "hours": 0.0, "overtime": 0.0}
        attendance.append(rec)

    cin = ask_time("  Check-In  (HH:MM or hh:MM AM/PM): ")
    cout = ask_time("  Check-Out (HH:MM or hh:MM AM/PM): ")
    if cin is None or cout is None:
        print("  Invalid time input."); return
    if cout <= cin:
        print("  Check-out must be later than check-in."); return

    worked = (cout - cin) / 60.0
    overtime = max(0.0, worked - STANDARD_HOURS)
    rec.update({
        "check_in": minutes_to_str(cin),
        "check_out": minutes_to_str(cout),
        "hours": round(worked, 2),
        "overtime": round(overtime, 2),
    })
    save_all()
    print(f"  ✓ Worked {worked:.2f} h, Overtime {overtime:.2f} h.")


def view_attendance_for_month():
    print("\n--- View Attendance for Month ---")
    emp_id = input("  Employee ID: ").strip().upper()
    if emp_id not in employees:
        print("  Unknown employee."); return
    month = ask_month("  Month (YYYY-MM): ")
    rows = [a for a in attendance if a["emp_id"] == emp_id and a["date"].startswith(month)]
    if not rows:
        print("  No records."); return
    print(f"\n  Records for {emp_id} — {month}")
    print("  Date         Status     In      Out     Hours  OT")
    for r in sorted(rows, key=lambda x: x["date"]):
        print(f"  {r['date']}  {r['status']:<9}  {str(r['check_in'] or '-'):<6}  "
              f"{str(r['check_out'] or '-'):<6}  {r['hours']:<5}  {r['overtime']}")


def attendance_summary(emp_id, month):
    rows = [a for a in attendance if a["emp_id"] == emp_id and a["date"].startswith(month)]
    summary = {"Present": 0, "Absent": 0, "Leave": 0, "Half Day": 0,
               "overtime_hours": 0.0, "total_hours": 0.0}
    for r in rows:
        summary[r["status"]] = summary.get(r["status"], 0) + 1
        summary["overtime_hours"] += r.get("overtime", 0.0)
        summary["total_hours"]   += r.get("hours", 0.0)
    # Half day counts as half present for payroll purposes
    summary["paid_present"] = summary["Present"] + 0.5 * summary["Half Day"]
    summary["unpaid_days"]  = summary["Absent"] + 0.5 * summary["Half Day"]
    summary["overtime_hours"] = round(summary["overtime_hours"], 2)
    summary["total_hours"]    = round(summary["total_hours"], 2)
    return summary


def show_attendance_summary():
    print("\n--- Attendance Summary ---")
    emp_id = input("  Employee ID: ").strip().upper()
    if emp_id not in employees:
        print("  Unknown employee."); return
    month = ask_month("  Month (YYYY-MM): ")
    s = attendance_summary(emp_id, month)
    print(f"  Present  : {s['Present']}")
    print(f"  Absent   : {s['Absent']}")
    print(f"  Leave    : {s['Leave']}")
    print(f"  Half Day : {s['Half Day']}")
    print(f"  Overtime : {s['overtime_hours']} h")
    print(f"  Total hrs: {s['total_hours']} h")


def attendance_menu():
    while True:
        print("\n=== Attendance Management ===")
        print("1. Record Attendance (Status)")
        print("2. Record Check-In / Check-Out")
        print("3. View Attendance for Month")
        print("4. Attendance Summary")
        print("0. Back")
        ch = input("Choice: ").strip()
        if ch == "1": record_attendance()
        elif ch == "2": record_check_in_out()
        elif ch == "3": view_attendance_for_month()
        elif ch == "4": show_attendance_summary()
        elif ch == "0": return
        else: print("  Invalid choice.")


# ================================================================ Module 3: Payroll
def calculate_payroll(emp, summary):
    daily = emp["salary"] / WORKING_DAYS
    ot_rate = daily / STANDARD_HOURS
    ot_comp = summary["overtime_hours"] * ot_rate
    deduction = daily * summary["unpaid_days"]
    gross = emp["salary"] + ot_comp
    net = gross - deduction
    return {
        "daily_salary": round(daily, 2),
        "overtime_rate": round(ot_rate, 2),
        "overtime_compensation": round(ot_comp, 2),
        "unpaid_deduction": round(deduction, 2),
        "gross_salary": round(gross, 2),
        "net_salary": round(net, 2),
    }


def find_payroll(emp_id, month):
    for p in payroll:
        if p["emp_id"] == emp_id and p["month"] == month:
            return p
    return None


def process_payroll():
    print("\n--- Process Payroll ---")
    emp_id = input("  Employee ID: ").strip().upper()
    emp = employees.get(emp_id)
    if not emp:
        print("  Unknown employee."); return
    month = ask_month("  Payroll Month (YYYY-MM): ")

    existing = find_payroll(emp_id, month)
    if existing:
        ans = input("  Payroll already exists. Revise? (y/n): ").strip().lower()
        if ans != "y":
            print("  Skipped."); return

    s = attendance_summary(emp_id, month)
    calc = calculate_payroll(emp, s)

    record = {
        "emp_id": emp_id,
        "name": emp["name"],
        "department": emp["department"],
        "designation": emp["designation"],
        "month": month,
        "basic_salary": emp["salary"],
        "present": s["Present"],
        "absent": s["Absent"],
        "leave": s["Leave"],
        "half_day": s["Half Day"],
        "unpaid_days": s["unpaid_days"],
        "overtime_hours": s["overtime_hours"],
        **calc,
    }

    if existing:
        payroll[payroll.index(existing)] = record
    else:
        payroll.append(record)
    save_all()

    write_salary_slip(record)
    print(f"  ✓ Payroll processed. Net salary: {record['net_salary']:.2f}")
    print(f"  ✓ Salary slip saved to {SLIP_DIR}/")


def write_salary_slip(p):
    path = os.path.join(SLIP_DIR, f"{p['emp_id']}_{p['month']}.txt")
    lines = [
        "=" * 52,
        f"{COMPANY_NAME:^52}",
        "SALARY SLIP".center(52),
        "=" * 52,
        f"Employee ID   : {p['emp_id']}",
        f"Employee Name : {p['name']}",
        f"Department    : {p['department']}",
        f"Designation   : {p['designation']}",
        f"Payroll Month : {p['month']}",
        "-" * 52,
        f"Basic Salary        : {p['basic_salary']:.2f}",
        f"Present Days        : {p['present']}",
        f"Absent Days         : {p['absent']}",
        f"Leave Days          : {p['leave']}",
        f"Half Days           : {p['half_day']}",
        f"Unpaid Days (calc)  : {p['unpaid_days']}",
        "-" * 52,
        f"Daily Salary        : {p['daily_salary']:.2f}",
        f"Overtime Hours      : {p['overtime_hours']}",
        f"Overtime Rate (hr)  : {p['overtime_rate']:.2f}",
        f"Overtime Compensation: {p['overtime_compensation']:.2f}",
        f"Unpaid Deduction    : {p['unpaid_deduction']:.2f}",
        "-" * 52,
        f"Gross Salary        : {p['gross_salary']:.2f}",
        f"NET SALARY          : {p['net_salary']:.2f}",
        "=" * 52,
    ]
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    except OSError as e:
        print(f"  [error] slip: {e}")


# ================================================================ Module 4: Reports
def report_attendance():
    print("\n--- Attendance Report ---")
    month = ask_month("  Month (YYYY-MM): ")
    rows = [a for a in attendance if a["date"].startswith(month)]
    if not rows:
        print("  No attendance records for that month."); return
    print(f"  {'ID':<8} {'Name':<20} {'Present':<8} {'Absent':<7} {'Leave':<6} {'Half':<5} {'OT(h)'}")
    for emp_id, emp in employees.items():
        s = attendance_summary(emp_id, month)
        if s["Present"] + s["Absent"] + s["Leave"] + s["Half Day"] == 0:
            continue
        print(f"  {emp_id:<8} {emp['name'][:20]:<20} {s['Present']:<8} "
              f"{s['Absent']:<7} {s['Leave']:<6} {s['Half Day']:<5} {s['overtime_hours']}")


def report_monthly_payroll():
    print("\n--- Monthly Payroll Report ---")
    month = ask_month("  Month (YYYY-MM): ")
    rows = [p for p in payroll if p["month"] == month]
    if not rows:
        print("  No payroll records."); return
    print(f"  {'ID':<8} {'Name':<20} {'Basic':<10} {'OT':<8} {'Deduct':<8} {'Net':<10}")
    total = 0.0
    for p in rows:
        print(f"  {p['emp_id']:<8} {p['name'][:20]:<20} {p['basic_salary']:<10.2f} "
              f"{p['overtime_compensation']:<8.2f} {p['unpaid_deduction']:<8.2f} {p['net_salary']:<10.2f}")
        total += p['net_salary']
    print(f"  TOTAL NET PAYROLL: {total:.2f}")


def report_salary_history():
    emp_id = input("\nEmployee ID: ").strip().upper()
    rows = [p for p in payroll if p["emp_id"] == emp_id]
    if not rows:
        print("  No history."); return
    print(f"  {'Month':<10} {'Basic':<10} {'OT':<8} {'Deduct':<8} {'Net':<10}")
    for p in sorted(rows, key=lambda x: x["month"]):
        print(f"  {p['month']:<10} {p['basic_salary']:<10.2f} {p['overtime_compensation']:<8.2f} "
              f"{p['unpaid_deduction']:<8.2f} {p['net_salary']:<10.2f}")


def report_department_summary():
    print("\n--- Department-Wise Payroll Summary ---")
    month = ask_month("  Month (YYYY-MM): ")
    rows = [p for p in payroll if p["month"] == month]
    if not rows:
        print("  No payroll records."); return
    dept_totals = {}
    for p in rows:
        d = p["department"]
        dept_totals.setdefault(d, {"count": 0, "net": 0.0})
        dept_totals[d]["count"] += 1
        dept_totals[d]["net"]   += p["net_salary"]
    print(f"  {'Department':<20} {'Employees':<10} {'Total Net'}")
    grand = 0.0
    for d, v in dept_totals.items():
        print(f"  {d:<20} {v['count']:<10} {v['net']:.2f}")
        grand += v["net"]
    print(f"  GRAND TOTAL NET SALARY EXPENSE: {grand:.2f}")


def report_total_expense():
    print("\n--- Total Monthly Salary Expense ---")
    month = ask_month("  Month (YYYY-MM): ")
    total = sum(p["net_salary"] for p in payroll if p["month"] == month)
    print(f"  Total net salary expense for {month}: {total:.2f}")


def report_employee_attendance_summary():
    print("\n--- Employee Attendance Summary ---")
    emp_id = input("  Employee ID: ").strip().upper()
    if emp_id not in employees:
        print("  Unknown employee."); return
    month = ask_month("  Month (YYYY-MM): ")
    s = attendance_summary(emp_id, month)
    print(f"  {emp_id} — {employees[emp_id]['name']}")
    print(f"  Present  : {s['Present']}")
    print(f"  Absent   : {s['Absent']}")
    print(f"  Leave    : {s['Leave']}")
    print(f"  Half Day : {s['Half Day']}")
    print(f"  Overtime : {s['overtime_hours']} h")


def reports_menu():
    while True:
        print("\n=== Reports ===")
        print("1. Attendance Report")
        print("2. Monthly Payroll Report")
        print("3. Employee Salary History")
        print("4. Department-Wise Payroll Summary")
        print("5. Total Monthly Salary Expense")
        print("6. Employee Attendance Summary")
        print("0. Back")
        ch = input("Choice: ").strip()
        if ch == "1": report_attendance()
        elif ch == "2": report_monthly_payroll()
        elif ch == "3": report_salary_history()
        elif ch == "4": report_department_summary()
        elif ch == "5": report_total_expense()
        elif ch == "6": report_employee_attendance_summary()
        elif ch == "0": return
        else: print("  Invalid choice.")


# ================================================================ Main
def main_menu():
    while True:
        print("\n" + "=" * 40)
        print(" EMPLOYEE ATTENDANCE & PAYROLL SYSTEM")
        print("=" * 40)
        print("1. Employee Management")
        print("2. Attendance Management")
        print("3. Payroll Processing")
        print("4. Reports")
        print("0. Exit")
        ch = input("Choice: ").strip()
        try:
            if ch == "1": employee_menu()
            elif ch == "2": attendance_menu()
            elif ch == "3": process_payroll()
            elif ch == "4": reports_menu()
            elif ch == "0":
                save_all()
                print("Data saved. Goodbye.")
                return
            else:
                print("  Invalid choice.")
        except KeyboardInterrupt:
            print("\n  Interrupted — saving data...")
            save_all()
            return
        except Exception as e:
            print(f"  [unexpected] {e}")


if __name__ == "__main__":
    load_all()
    main_menu()