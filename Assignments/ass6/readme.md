# Employee Attendance & Payroll Management System

This is my Core Python project for managing employee attendance and payroll. It's a
menu-driven console application that lets you register employees, mark their daily
attendance, track working hours and overtime, run monthly payroll, and print salary
slips. Everything is saved to JSON files so the data sticks around after you close it.

I built it without any external libraries — just the Python standard library. No OOP,
no databases, no Pandas or NumPy, because the brief said not to use them. I also kept
it as a single `main.py` file for simplicity, even though the brief suggested splitting
it into modules. It's easier to run this way and the code is still organized into clear
sections.

## What it does

The app is split into six modules that mirror the brief:

**Employee Management** — Add employees with an auto-generated ID (EMP001, EMP002,
etc.). You can search by ID, update any field, or list everyone. Salary has to be a
positive number or it won't save. Since IDs are generated automatically there's no way
to create a duplicate.

**Attendance Management** — Mark someone Present, Absent, Leave, or Half Day for any
date. The program refuses to add a second record for the same employee on the same
date, which was one of the requirements. You can pull up a monthly view of anyone's
attendance or get a summary with counts.

**Working Hours & Overtime** — Enter check-in and check-out times and the app works
out the total hours. Anything past 8 hours counts as overtime. It accepts both 24-hour
(`17:30`) and 12-hour (`05:30 PM`) formats, which was a small thing I added because
it's annoying to type one when you mean the other. Check-out must be after check-in,
and unparseable times are rejected.

**Payroll** — Pick an employee and a month, and the program pulls the salary and that
month's attendance, then runs all the formulas from the brief. If you try to run the
same month twice it asks you to confirm before overwriting.

**Salary Slips** — Each payroll run writes a `.txt` slip into `salary_slips/`. The
filename is `<EMPID>_<YYYY-MM>.txt` so they don't collide.

**Reports** — Six of them: attendance report for a month, monthly payroll report,
salary history for one employee, department-wise summary, total monthly expense, and
a per-employee attendance summary.

## Files and folders
