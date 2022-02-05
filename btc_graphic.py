import matplotlib.pyplot as plt

x = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
y = [0.0008, 0.39, 3.14, 12, 120, 300, 450, 1000, 20000, 17675, 13796, 29000, 38800]

plt.bar(x, y, color="#f7931a")
plt.plot(x, y, color="k")

plt.title("Valorização do Bitcoin (2009-2021)")
plt.xlabel("Ano")
plt.ylabel("Valor em U$")
plt.show()