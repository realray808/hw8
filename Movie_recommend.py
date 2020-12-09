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


def ranking_order(score, pos=4, value=0):
    if pos < 1:
        return value
    else:
        for i in score[:pos]:
            if i <= score[pos]:
                value += 1
    return ranking_order(score, pos-1, value)


def nearest_user(u1, customer):
    u1_dismiss = ranking_order(Customers.get(u1))
    diff = 100
    match = {}
    for i, j in customer.items():
        if i != u1:
            if abs(ranking_order(j) - u1_dismiss) < diff:
                match = {i}
                diff = abs(ranking_order(j) - u1_dismiss)
            if abs(ranking_order(j) - u1_dismiss) == diff:
                match.add(i)
    return match


def test():
    while 1:
        customer = input("Please enter the customer name =>")
        if not Customers.get(customer):
            print("Please enter a valid customer name")
            break
        print(customer)
        u1 = ranking_order(Customers.get(customer))
        u1_favorite = Customers.get(customer).index(max(Customers.get(customer)))+1
        print("The dissimilarity metric for this customer is %d" % u1)
        line = "----------------------------------------\n" + \
               "Similar User(s) And Recommendations:\n" + \
               "----------------------------------------"
        print(line)
        for i in nearest_user(customer, Customers):
            print(i)
            i_favorite = Customers.get(i).index(max(Customers.get(customer)))+1
            if i_favorite == u1_favorite:
                print("No recommendations for this user now")
            else:
                print("Customers who chose movie number %d also chose movie number %d" % (u1_favorite, i_favorite))


if __name__ == '__main__':
    test()
    # print(ranking_order([1,2,3,4,5]))
    # print(nearest_user("Customer_4", Customers))