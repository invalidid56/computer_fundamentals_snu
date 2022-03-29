# 강준서 식물생산과학부 2022-14673
# finance.py
# define finance methods to solve problem

# rate : interest rate per period
# nper : total number of payment periods in the investment
# pv : present value
def fv(rate, nper, pv):
    return pv*(1+rate)**nper

