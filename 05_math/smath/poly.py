# 2022-14673 강준서 식물생산과학부
# poly.py - polynomials
#
from math import sqrt


# Polynomial Equation Solver
#
# coefficients : list of coefficients. for example [2, 3, 4] for 2x^2 + 3x + 4
# return list of solutions. for examaple [-1, 1] for x^2 - 1 = 0


def solve(coefficients):
    error = False
    warning_message = 'Warning: {0} ({1})'
    error_type = ''
    error_cause = ''
    exponent = len(coefficients) - 1

    if exponent == 1:
        if coefficients[0] == 0:
            if coefficients[1] != 0:
                error = True
                error_type = 'undefined'
                error_cause = 'there is no possible solution'
            else:
                error = True
                error_type = 'indeterminate'
                error_cause = '0/0 form'
        else:
            ans = -coefficients[1] / coefficients[0]
            return [ans]

        if error:
            print(warning_message.format(error_type, error_cause))
            return float('nan')
    elif exponent == 2:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]

        D = b ** 2 - 4 * a * c

        if D > 0:
            ans1 = (-b + sqrt(D)) / (2 * a)
            ans2 = (-b + sqrt(D)) / (2 * a)
            return [ans1, ans2]

        elif D == 0:
            ans = (-b) / (2 * a)
            return [ans]

        elif D < 0:
            ir = sqrt(-D) / (2*a)
            real = -b / (2 * a)
            ans1 = complex(real, ir)
            ans2 = complex(real, -ir)
            return [ans1, ans2]

    else:
        print("can't solve! {0}".format(str(coefficients)))
        return None
