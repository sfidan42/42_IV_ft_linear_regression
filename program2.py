def train(data, lr=0.1, epochs=1000):

    def estimatePrice(mileage):
        return theta0 + theta1 * mileage

    theta0, theta1 = 0, 0
    mileage, price = data['km'].copy(), data['price'].copy()

    mileage /= max(mileage)
    price /= max(price)

    m = len(mileage)
    for _ in range(epochs):
        tmpTheta0 = lr * (1/m) * sum(estimatePrice(mileage) - price)
        tmpTheta1 = lr * (1/m) * sum((estimatePrice(mileage) - price) * mileage)
        theta0 -= tmpTheta0
        theta1 -= tmpTheta1

    theta0 *= max(data['price'])
    theta1 *= max(data['price']) / max(data['km'])

    with open('params.txt', 'w') as file:
        file.write(f'{theta0},{theta1}')

    return theta0, theta1
