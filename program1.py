def predict(data):

    mileage = data['km']

    with open("params.txt", "r") as file:
        str1, str2 = file.readline().split(',')
        theta0 = float(str1)
        theta1 = float(str2)
        
        def estimatePrice(mileage):
            return theta0 + theta1 * mileage

        return estimatePrice(mileage)
