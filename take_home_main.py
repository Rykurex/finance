import take_home_calcs
import take_home_inputs

my_pension_cont, employer_pension_cont, total_pension_cont = take_home_calcs.calc_pension(take_home_inputs.my_salary,
                                                                                          take_home_inputs.my_pension_pct,
                                                                                          take_home_inputs.employer_pension_pct)
pension_conts = [my_pension_cont, employer_pension_cont, total_pension_cont]
for contribution in pension_conts:
    print("Annual Contributions: ", contribution)
    print("Monthly Contributions: ", contribution/12)
