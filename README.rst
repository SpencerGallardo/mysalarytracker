MySalaryTracker
==================
MySalaryTracker is a program that helps freelancers and employees in a company to help keep track and calculate their net income.

Personas
========

Lia the Freelance Graphic Designer

Details
^^^^^^^

Lia is a Freelancer who works part-time and full-time at a company.
She is a young professional and likes to keep track of her finances and wants to plan her spending.
She is 27 years old and lived in Sunnyside, Queens with her dog.
Keeping track of her income and expenses are important for her to reach financial goals.

Goals
^^^^^
Lia wants to know exactly how much money she will be getting per paycheck in order to plan her spending for the 6-12 months.
This will allow her to save and budget for bug purchases such as a house, business or travels.

Problem Scenario
================

Overspending and missing financial goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lia realizes she has been overestimating her net income and his been overspending on her credit card and checking account. Her overall assests have dropped due to poor calculation.
She realizes she needs to plans her finances based on her fluctuating freelance checks this year in order to stay on track to make her fufuil her dreams of buying a house, business, or traveling.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^
Current alternatives is use a personal accountant to help give you an estimate on your net income.

Value Propistion
^^^^^^^^^^^^^^^^
The ability to be able to calculate your net income for per paycheck,monthly, and yearly after taxes. The ability to create a budget plan for any of those timeframes.

User Stories
============
As Lia the Graphic Desinger, I want to be able to calculate my net income from my salary in order to plan my financial year ahead and make milestone purchases and investments.

Scenario 01:
^^^^^^^^^^^

Lia: I just worked on a one day project working for menu redesign for about 10 hours and I billed at $20 an hour for this small business. I should probably deduct the current taxes in this state and deduct $5 for expenses from my overall paycheck. I'll calculcate my net income and how much I can save.
.. ::
  Do you want to input Monthly or Hourly? Hourly
  What is your hourly rate? 20
  How many hours did you work? 10
  What deductions are you charged? (For example: $1 + 20%) $5 + 8%
  Gross income: 200.0
  Net income: 179.0
  Total deductions: 21.0

Scenario 02:
^^^^^^^^^^^

Lia: I have a long term project that will pay me $5,000 for the month. Rent is due for $1,025 at the end of the month.
I need to know how much I will have left to spend on other expenses and savings
.. ::
  Do you want to input Monthly or Hourly? Monthly
  What is your gross income? 5000
  What deductions are you charged? (For example: $1 + 20%) $1025
  Gross income: 5000.0
  Net income: 3975.0
  Total deductions: 1025.0
  
Lia: I have $3,975 for the rest of the month in order to spend on other expenses and savings for this month.

Scenario 03:
^^^^^^^^^^^

Lia: I have 2 offers in two differente cities. The first company pays $35 an hour with a 30% tax rate and second company pays $30 an hour with a 20% tax rate. I would be working for 8 hours each day. Which should I choose? I will do the calculation on my daily pay and decide.

Company 1
.. ::
  Do you want to input Monthly or Hourly? Hourly
  What is your hourly rate? 35
  How many hours did you work? 8
  What deductions are you charged? (For example: $1 + 20%) 30%
  Gross income: 280.0
  Net income: 196.0
  Total deductions: 84.0
  
Company 2
.. ::
  Do you want to input Monthly or Hourly? Hourly
  What is your hourly rate? 30
  How many hours did you work? 8
  What deductions are you charged? (For example: $1 + 20%) 20%
  Gross income: 240.0
  Net income: 192.0
  Total deductions: 48.0


Although, it's very similar, maybe I will follow up with the first company's hourly offer. Although the first company has a higher deduction, the higher pay gives me a slightly higher return on net income. After a few days, that daily difference may add up.

**************
INSTRUCTIONS
**************

1. Installation
================

Download the module and execute the script. No extras are required to run it succesfully.

2. Executing mysalarytracker.py
=======================

Running the program will prompt you to several questions to easily calculate your net income.

Do you want to input Monthly or Hourly?

What is your hourly rate? or What is your gross income?
 
What deductions are you charged? (For example: $1 + 20%)

Results
^^^^^^^

Gross income - Entire sum of pay

Net income - Actual pay from check after deductions

Total deductions - Total sum of deductions
