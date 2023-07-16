# Inputs required for the take_home_calcs functions and take_home_main

#Salary
my_salary = 54335

#Pension contribution %s
#Current formula is only for a salary sacrifice scheme
my_pension_pct = 0.06
employer_pension_pct = 0.15

#Other Salary Sacrifice
my_sal_sac_monthly = 150
my_sal_sac_annual = my_sal_sac_monthly * 12


#Tax & NI info

#Tax Code
my_tax_code = 1257

#Income Tax Thresholds
basic_rate_upper = 37700
#Income above (this + your allowance) is taxed at 40%, up to the next threshold
higher_rate_upper = 125140
#Is not changed by the allowance
tax_allowance_th = 100000
#After this, your allowance is reduced by £1 for every £2
#Any remaining taxable income over 125,140 is taxed at the additional rate

basic_rate_pct = 0.2
higher_rate_pct = 0.4
additional_rate_pct = 0.45

#National Insurance
ni_primary_th = 12570
ni_uel_th = 50270

ni_primary_pct = 0.12
ni_uel_pct = 0.02


#Student Loan Info

#My Student Loan Plan
my_sl_plan = 2
my_postgrad = False
#Repayment Dictionary
student_loan_info = {
    "threshold": {
        "Plan 1": 22015,
        "Plan 2": 27295,
        "Plan 4": 27660,
        "Plan 5": 25000,
        "Postgrad": 21000
    },
    "percentage": {
        "Plan 1": 0.09,
        "Plan 2": 0.09,
        "Plan 4": 0.09,
        "Plan 5": 0.09,
        "Postgrad": 0.06
    }
}