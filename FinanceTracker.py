# Calculates various tax and pension contributions
# And take home pay, given a salary and pension information

#All required inputs

#Salary
my_salary = 54335

#Input Pension %s - Salary Sacrifice Scheme
my_pension_pct = 0.06
employer_pension_pct = 0.15

#Input other Salary Sacrifice
my_sal_sac_monthly = 150
my_sal_sac_annual = my_sal_sac_monthly * 12


#Tax & NI info

#Input Tax Code
my_tax_code = 1257

#Income Tax
basic_rate_upper = 37700
higher_rate_upper = 125140
tax_allowance_th = 100000
# additional_rate_taxable is any remaining taxable income over 125,140
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




def calc_pension(my_salary, my_pension_pct, employer_pension_pct):
    #Takes required inputs to calculate pension contributions from
    #Employee, Employer, and calculates Total
    my_pension_cont = my_salary * my_pension_pct
    employer_pension_cont = my_salary * employer_pension_pct
    total_pension_pct = my_pension_pct + employer_pension_pct
    total_pension_cont = my_salary * total_pension_pct
    
    return my_pension_cont, employer_pension_cont, total_pension_cont




my_pension_cont, employer_pension_cont, total_pension_cont = calc_pension(my_salary, my_pension_pct, employer_pension_pct)
pension_conts = [my_pension_cont, employer_pension_cont, total_pension_cont]
for contribution in pension_conts:
    print("Annual Contributions: ", contribution)
    print("Monthly Contributions: ", contribution/12)




def calc_net_of_sal_sac(my_salary, my_pension_cont, my_sal_sac_annual):
    #Calculates pre-tax income, net of salary sacrifice
    net_of_sal_sac = my_salary - (my_pension_cont + my_sal_sac_annual)
    return net_of_sal_sac




net_of_sal_sac = calc_net_of_sal_sac(my_salary, my_pension_cont, my_sal_sac_annual)
print(net_of_sal_sac)




def calc_tax_free_allowance(net_of_sal_sac, my_tax_code, tax_allowance_th, higher_rate_upper):
    #Calculates personal tax allowance using pre-tax income, net of salary sacrifice
    #Which is reduced by £1 for every £2 earned over the tax allownace threshold
    default_tax_free_allowance = my_tax_code * 10
    print("Default tax free allowance based on tax code: ", default_tax_free_allowance)
    
    if net_of_sal_sac > tax_allowance_th:
        #Reduce tax free allowance by £1 for every £2 over higher rate th, until 0.
        delta = net_of_sal_sac - tax_allowance_th
        reduction = delta // 2
        print("Income Net of Salary Sacrifice is greater than the personal allowance threshold of: ", 
              tax_allowance_th, " by: ", reduction)
        
        if reduction < default_tax_free_allowance:
            my_tax_free_allowance = default_tax_free_allowance - reduction
            print("Reducing your personal allowance by: ", delta)
        
        else:
            my_tax_free_allowance = 0
            print("Reducing your personal allowance by: ", default_tax_free_allowance)
        
    else:
        my_tax_free_allowance = default_tax_free_allowance
        
    print("Your tax free allowance is: ", my_tax_free_allowance)
    
    return my_tax_free_allowance
    




my_tax_free_allowance = calc_tax_free_allowance(net_of_sal_sac, my_tax_code, tax_allowance_th, higher_rate_upper)




def calc_actual_taxable_income(net_of_sal_sac, my_tax_free_allowance):
    actual_taxable_income = net_of_sal_sac - my_tax_free_allowance
    return actual_taxable_income




actual_taxable_income = calc_actual_taxable_income(net_of_sal_sac, my_tax_free_allowance)
print("You will pay tax on: ", actual_taxable_income)




#Calculate Tax
def calc_tax(my_tax_free_allowance, actual_taxable_income, basic_rate_upper, basic_rate_pct,
            net_of_sal_sac, additional_rate_pct, higher_rate_upper, higher_rate_pct):
    
    #0% Tax paid up to the tax free allownace
    print("You pay 0% tax up to your tax free allowance of: ", my_tax_free_allowance)
    
    #20% Tax up to the basic rate upper limit, after the allowance    
    if actual_taxable_income >= basic_rate_upper:
        basic_rate_tax = basic_rate_upper * basic_rate_pct
        print("You will pay ", basic_rate_pct*100, "% tax on ", basic_rate_upper, ", which is: ", basic_rate_tax)
    else:
        basic_rate_tax = actual_taxable_income * basic_rate_pct  
        print("You will pay ", basic_rate_pct*100, "% tax on ", actual_taxable_income, ", which is: ", basic_rate_tax)
    
    #40% Tax up to the higher rate upper limit - not lowered by the allowance
    my_higher_rate_lower_limit = basic_rate_upper + my_tax_free_allowance
    if net_of_sal_sac > my_higher_rate_lower_limit:
        if net_of_sal_sac <= higher_rate_upper:
            higher_rate_taxable = net_of_sal_sac - my_higher_rate_lower_limit
            higher_rate_tax = higher_rate_taxable * higher_rate_pct
            print("You will pay ", higher_rate_pct*100, "% tax on ", higher_rate_taxable, ", which is: ", higher_rate_tax)
        else:
            higher_rate_taxable = higher_rate_upper - my_higher_rate_lower_limit
            higher_rate_tax = higher_rate_taxable * higher_rate_pct
            print("You will pay ", higher_rate_pct*100, "% tax on ", higher_rate_taxable, ", which is: ", higher_rate_tax)
    else:
        higher_rate_taxable = 0
        higher_rate_tax = 0
    
    #45% Tax on anything over the higher rate upper limit - not reduced by the allowance
    if net_of_sal_sac > higher_rate_upper:
        additional_rate_taxable = net_of_sal_sac - higher_rate_upper
        additional_rate_tax = additional_rate_taxable * additional_rate_pct
        print("You will pay ", additional_rate_pct*100, "% tax on ", additional_rate_taxable, ", which is: ",
              additional_rate_tax)
    else:
        additional_rate_taxable = 0
        additional_rate_tax = 0
    
    return additional_rate_tax, higher_rate_tax, basic_rate_tax




additional_rate_tax, higher_rate_tax, basic_rate_tax = calc_tax(my_tax_free_allowance, 
    actual_taxable_income, basic_rate_upper, basic_rate_pct,
    net_of_sal_sac, additional_rate_pct, higher_rate_upper, higher_rate_pct)

print(additional_rate_tax, higher_rate_tax, basic_rate_tax)
print(additional_rate_tax/12, higher_rate_tax/12, basic_rate_tax/12)




def calc_ni(ni_primary_th, ni_uel_th, net_of_sal_sac, ni_primary_pct, ni_uel_pct):
    primary_ni_taxable = ni_uel_th - ni_primary_th
    upper_ni_taxable = net_of_sal_sac - ni_uel_th
    
    if net_of_sal_sac < ni_uel_th:
        my_ni_primary = (net_of_sal_sac - ni_primary_th) * ni_primary_pct
        my_ni_upper = 0
    else:
        my_ni_primary = primary_ni_taxable * ni_primary_pct
        my_ni_upper = upper_ni_taxable * ni_uel_pct
    
    return my_ni_primary, my_ni_upper




my_ni_primary, my_ni_upper = calc_ni(ni_primary_th, ni_uel_th, net_of_sal_sac, ni_primary_pct, ni_uel_pct)
print(my_ni_primary, my_ni_upper)




#Calculate Student Loan
def calc_student_loan(net_of_sal_sac, student_loan_info, my_sl_plan, my_postgrad):
    global my_sl_tax
    my_sl_plan_key = "Plan " + str(my_sl_plan)
    my_sl_threshold = student_loan_info['threshold'][my_sl_plan_key]
    my_sl_pct = student_loan_info['percentage'][my_sl_plan_key]
    
    if net_of_sal_sac < my_sl_threshold:
        my_sl_taxable = 0
    else:
        my_sl_taxable = net_of_sal_sac - my_sl_threshold
        my_sl_tax = my_sl_taxable * my_sl_pct
        
    return my_sl_tax
    




my_sl_tax = calc_student_loan(net_of_sal_sac, student_loan_info, my_sl_plan, my_postgrad)
print(my_sl_tax)





def calc_takehome(net_of_sal_sac, my_sl_tax, additional_rate_tax, higher_rate_tax, basic_rate_tax, my_ni_primary, my_ni_upper):
    total_tax = my_sl_tax + additional_rate_tax + higher_rate_tax + basic_rate_tax + my_ni_primary + my_ni_upper
    my_takehome = net_of_sal_sac - total_tax
    
    return my_takehome





my_takehome = calc_takehome(net_of_sal_sac, my_sl_tax, additional_rate_tax,
                            higher_rate_tax, basic_rate_tax, my_ni_primary, my_ni_upper)

print(my_takehome)
print(my_takehome/12)



