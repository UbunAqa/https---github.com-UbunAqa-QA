
# def calculate(gross, state):

#     state_tax = {"AB":10, "TS":5, "ND":6}
#     sol = gross - (gross*0.1)

#     if state in state_tax:
#         sol = sol - (gross * state_tax[state]/100)
#         print("Your sol income after all the heavy is: " + str(sol))
#         return sol
#     else:
#         print("State is not founded")
#         return None


# x = calculate(100000,'AB')

# print(x)



def calculate(gross, state):

    state_tax = {"AB":10, "TS":5, "ND":6}
    
    federal_tax = 0.1

    if state in state_tax:
        sol = (gross * federal_tax * state_tax[state]/100)
        print("Your sol income after all the heavy is: " + str(sol))
        return sol
    else:
        print("State is not founded")
        return None


x = calculate(100000,'AB')
