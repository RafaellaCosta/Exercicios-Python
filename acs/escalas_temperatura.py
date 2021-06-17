t_fahrenheit = float(input())

t_celsius = (t_fahrenheit - 32) * 5/9

t_kelvin = t_celsius + 273.15

print(f"""Convertendo {t_fahrenheit:.2f} graus Fahrenheit temos:
    {t_celsius:.2f} graus Celsius e {t_kelvin:.2f} Kelvin""")
