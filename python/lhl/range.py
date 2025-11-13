import time

bacteria = "🌭"
generations = 10

for generation in range(0, generations):
    bacteria = bacteria *2
    print(bacteria)
    time.sleep(0.5)
