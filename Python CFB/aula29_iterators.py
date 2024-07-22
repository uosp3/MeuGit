#https://www.youtube.com/watch?v=FuuYavr-Bu8&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=29
carros=["HRV","Polo","Jetta","Cruze","Fusion","Golf","Focus","Onyx", "Fit"]

itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break