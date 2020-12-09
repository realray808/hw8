Customers = {"Customer_3": [4, 3, 5, 2, 1],
             "Customer_5": [1, 3, 4, 2, 5],
             "Customer_1": [5, 4, 3, 2, 1],
             "Customer_4": [4, 5, 2, 1, 3],
             "Customer_2": [2, 3, 4, 1, 5],
             "Customer_10": [3, 1, 2, 4, 5],
             "Customer_11": [2, 5, 1, 4, 3],
             "Customer_16": [1, 2, 4, 5, 3],
             "Customer_22": [5, 1, 3, 4, 2],
             "Customer_100": [3, 2, 1, 4, 5]}


def ranking_order(score, pos, value=0):
    if pos > 0:
        for i in score[:pos-1]:
            if i <= score[pos-1]:
                value += 1
        ranking_order(score, pos-1, value)

    return value


def test():
    while 1:
        customer = input("Please enter the customer name =>")
        if not Customers.get(customer):
            print("Please enter a valid customer name")
            break


if __name__ == '__main__':
    dismiss = ranking_order([4, 3, 5, 2, 1], 5)
    print(dismiss)