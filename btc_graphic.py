import matplotlib.pyplot as mpl

# Eixo X simboliza o ano, eixo Y simboliza o valor em dólar
x = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
y = [0.0008, 0.39, 3.14, 12, 120, 300, 450, 1000, 20000, 17675, 13796, 29000, 38800]

# Cria o gráfico de barras e a linha de crescimento do valor
mpl.bar(x, y, color="#f7931a")
mpl.plot(x, y, color="k")

# Cria as legendas do gráfico
mpl.title("Valorização do Bitcoin (2009-2021)")
mpl.xlabel("Ano")
mpl.ylabel("Valor em U$")

# Exibe o gráfico
mpl.show()
