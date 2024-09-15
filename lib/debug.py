#!/usr/bin/env python3
# lib/testing/debug.py

import ipdb
from __init__ import CONN, CURSOR
from department import Department

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th floor")
print(payroll)

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)

hr.name = "HR"
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)

print("Delete Payroll")
payroll.delete()
print(payroll)

ipdb.set_trace()
