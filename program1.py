def predict(data = None):
    if data is None:
        mileage = int(input("Enter the mileage of the car: "))
    else:
        mileage = data['km']
    try:
        with open("params.txt", "r") as file:
            str1, str2 = file.readline().split(',')
            theta0 = float(str1)
            theta1 = float(str2)
    except FileNotFoundError:
        print("File 'params.txt' not found. Using default values for thetas.")
        theta0 = 0
        theta1 = 0

    def estimatePrice(mileage):
        return theta0 + theta1 * mileage

    return estimatePrice(mileage)
