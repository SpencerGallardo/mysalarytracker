#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My Salary Tracker by SpencerGallardo"""
import re


def p2f(x):
    return float(x.strip('%'))/100

hourly = ["hourly", "Hourly", "hour", "Hour", "h", "H"]
monthly = ["monthly", "Monthly", "month", "Month", "m", "M"]

"""Ask for hourly or monthly"""
hourly_or_monthly = raw_input("Do you want to input Monthly or Hourly? ")


if hourly_or_monthly in hourly:
    # Ask for number of hours
    rate = raw_input("What is your hourly rate? ")
    rate = float(re.findall('\d+', rate)[0])

    # Ask for number of hours
    hours = raw_input("How many hours did you work? ")
    hours = float(re.findall('\d+', hours)[0])

    # Calculate Gross income
    gross = rate * hours

    # Ask user for deductions
    deductions = raw_input("What deductions are you charged? (For example: $1 + 20%) ")
    money_deducted = re.search(ur'([£$€])(\d+(?:\.\d{2})?)', deductions)
    if not money_deducted:
        money_deducted = None
    else:
        money_deducted = money_deducted.groups()
        money_deducted = money_deducted[1]
        money_deducted = float(money_deducted)
    percentage_deducted = re.findall(r'\d+%', deductions)
    if not percentage_deducted:
        percentage_deducted = None
    else:
        percentage_deducted = percentage_deducted[0]
        percentage_deducted = p2f(percentage_deducted)

    if percentage_deducted == None and money_deducted != None:
        total_deductions = money_deducted
    elif money_deducted == None and percentage_deducted!= None:
        total_after_percentage = gross * percentage_deducted
        total_deductions = total_after_percentage
    elif money_deducted != None and percentage_deducted != None:
        total_after_percentage = gross * percentage_deducted
        total_deductions = total_after_percentage + money_deducted

    net_income = gross - total_deductions

    # Show user
    print "Gross income: " + str(gross)
    print "Net income: " + str(net_income)
    print "Total deductions: " + str(total_deductions)
elif hourly_or_monthly in monthly:
    # Ask for gross
    gross = raw_input("What is your gross income? ")
    gross = float(re.findall('\d+', gross.replace(',', ''))[0])

    # Ask user for deductions
    deductions = raw_input("What deductions are you charged? (For example: $1 + 20%) ")
    money_deducted = re.search(ur'([£$€])(\d+(?:\.\d{2})?)', deductions)
    if not money_deducted:
        money_deducted = None
    else:
        money_deducted = money_deducted.groups()
        money_deducted = money_deducted[1]
        money_deducted = float(money_deducted)
    percentage_deducted = re.findall(r'\d+%', deductions)
    if not percentage_deducted:
        percentage_deducted = None
    else:
        percentage_deducted = percentage_deducted[0]
        percentage_deducted = p2f(percentage_deducted)

    if percentage_deducted == None and money_deducted != None:
        total_deductions = money_deducted
    elif money_deducted == None and percentage_deducted!= None:
        total_after_percentage = gross * percentage_deducted
        total_deductions = total_after_percentage
    elif money_deducted != None and percentage_deducted != None:
        total_after_percentage = gross * percentage_deducted
        total_deductions = total_after_percentage + money_deducted

    net_income = gross - total_deductions

    # Show user
    print "Gross income: " + str(gross)
    print "Net income: " + str(net_income)
    print "Total deductions: " + str(total_deductions)
else:
    print "Please pick either Hourly or Monthly"



