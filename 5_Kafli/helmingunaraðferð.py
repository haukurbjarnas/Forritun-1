def f(x)


if f(a)*f(b) >= 0:
    print("Bisection method fails.")
    return None
a_n = a
b_n = b
while (b_n-a_n)/2>tol:
    m_n = (a_n + b_n)/2
    f_m_n = f(m_n)
    if f(a_n)*f_m_n < 0:
        a_n = a_n
        b_n = m_n
    elif f(b_n)*f_m_n < 0:
        a_n = m_n
        b_n = m_n
    elif f_m_n == 0:
        print("Found exact solution.")
        return m_n
return (a_n + b_n)/2