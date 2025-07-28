# the list / to do list with two parts to each [0] / [1]
cartons = [
    ["Not almond milk", "Wrong logo"],
    ["Not almond milk", "Right logo"],
    ["Almond milk", "Wrong logo"],
    ["Almond milk", "Right logo"],
]

cart = []

wrongCartonsLookAt = 0

for carton in cartons:
    typeofmilk = carton[0]
    logo = carton[1]
    if typeofmilk == "Almond milk" and logo == "Right logo":
        cart.append(carton)
        break
    else:
        wrongCartonsLookAt += 1

if len(cart) == 0:
    cart.append("Beer")

print("I looked at " + str(wrongCartonsLookAt) + " cartons that were not"
" almond=painted-like-a-cow brand almond milk.")

