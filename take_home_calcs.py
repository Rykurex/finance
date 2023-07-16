# All functions required to calculated take home pay

def calc_pension(my_salary, my_pension_pct, employer_pension_pct):
    # Takes required inputs to calculate pension contributions from
    # Employee, Employer, and calculates Total
    my_pension_cont = my_salary * my_pension_pct
    employer_pension_cont = my_salary * employer_pension_pct
    total_pension_pct = my_pension_pct + employer_pension_pct
    total_pension_cont = my_salary * total_pension_pct

    return my_pension_cont, employer_pension_cont, total_pension_cont


def calc_net_of_sal_sac(my_salary, my_pension_cont, my_sal_sac_annual):
    #Calculates pre-tax income, net of salary sacrifice
    net_of_sal_sac = my_salary - (my_pension_cont + my_sal_sac_annual)
    return net_of_sal_sac


def calc_tax_free_allowance(net_of_sal_sac, my_tax_code, tax_allowance_th, higher_rate_upper):
    # Calculates personal tax allowance using pre-tax income, net of salary sacrifice
    # Which is reduced by £1 for every £2 earned over the tax allownace threshold
    default_tax_free_allowance = my_tax_code * 10
    print("Default tax free allowance based on tax code: ", default_tax_free_allowance)

    if net_of_sal_sac > tax_allowance_th:
        # Reduce tax free allowance by £1 for every £2 over higher rate th, until 0.
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


def calc_actual_taxable_income(net_of_sal_sac, my_tax_free_allowance):
    actual_taxable_income = net_of_sal_sac - my_tax_free_allowance
    return actual_taxable_income


def calc_tax(my_tax_free_allowance, actual_taxable_income, basic_rate_upper, basic_rate_pct,
             net_of_sal_sac, additional_rate_pct, higher_rate_upper, higher_rate_pct):
    # 0% Tax paid up to the tax free allownace
    print("You pay 0% tax up to your tax free allowance of: ", my_tax_free_allowance)

    # 20% Tax up to the basic rate upper limit, after the allowance
    if actual_taxable_income >= basic_rate_upper:
        basic_rate_tax = basic_rate_upper * basic_rate_pct
        print("You will pay ", basic_rate_pct * 100, "% tax on ", basic_rate_upper, ", which is: ", basic_rate_tax)
    else:
        basic_rate_tax = actual_taxable_income * basic_rate_pct
        print("You will pay ", basic_rate_pct * 100, "% tax on ", actual_taxable_income, ", which is: ", basic_rate_tax)

    # 40% Tax up to the higher rate upper limit - not lowered by the allowance
    my_higher_rate_lower_limit = basic_rate_upper + my_tax_free_allowance
    if net_of_sal_sac > my_higher_rate_lower_limit:
        if net_of_sal_sac <= higher_rate_upper:
            higher_rate_taxable = net_of_sal_sac - my_higher_rate_lower_limit
            higher_rate_tax = higher_rate_taxable * higher_rate_pct
            print("You will pay ", higher_rate_pct * 100, "% tax on ", higher_rate_taxable, ", which is: ",
                  higher_rate_tax)
        else:
            higher_rate_taxable = higher_rate_upper - my_higher_rate_lower_limit
            higher_rate_tax = higher_rate_taxable * higher_rate_pct
            print("You will pay ", higher_rate_pct * 100, "% tax on ", higher_rate_taxable, ", which is: ",
                  higher_rate_tax)
    else:
        higher_rate_taxable = 0
        higher_rate_tax = 0

    # 45% Tax on anything over the higher rate upper limit - not reduced by the allowance
    if net_of_sal_sac > higher_rate_upper:
        additional_rate_taxable = net_of_sal_sac - higher_rate_upper
        additional_rate_tax = additional_rate_taxable * additional_rate_pct
        print("You will pay ", additional_rate_pct * 100, "% tax on ", additional_rate_taxable, ", which is: ",
              additional_rate_tax)
    else:
        additional_rate_taxable = 0
        additional_rate_tax = 0

    return additional_rate_tax, higher_rate_tax, basic_rate_tax


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


def calc_student_loan(net_of_sal_sac, student_loan_info, my_sl_plan):
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


def calc_postgrad(net_of_sal_sac, my_postgrad, student_loan_info):
    if my_postgrad == True:
        postgrad_key = "Postgrad"
        postgrad_threshold = student_loan_info['threshold'][postgrad_key]
        my_postgrad_pct = student_loan_info['percentage'][postgrad_key]

        my_postgrad_taxable = net_of_sal_sac - postgrad_threshold
        my_postgrad_tax = my_postgrad_taxable * my_postgrad_pct

        return my_postgrad_tax

    else:
        my_postgrad_tax = 0
        return my_postgrad_tax



def calc_takehome(net_of_sal_sac, my_sl_tax, additional_rate_tax, higher_rate_tax, basic_rate_tax, my_ni_primary,
                  my_ni_upper):
    total_tax = my_sl_tax + additional_rate_tax + higher_rate_tax + basic_rate_tax + my_ni_primary + my_ni_upper
    my_takehome = net_of_sal_sac - total_tax

    return my_takehome