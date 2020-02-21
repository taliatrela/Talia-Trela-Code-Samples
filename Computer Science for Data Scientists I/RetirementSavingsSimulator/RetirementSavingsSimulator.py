#     This script simulates retirement savings. It asks the user for their current savings in four broad categories: cash,
# bank savings, bond investments, and stock investments. They are asked for a starting and ending percentage for each
# of these broad categories, their current age and their desired retirment age, and the amount that they wish to invest
# each year. They could also choose to increase the annual giving by a certain percentage. Each year, the portfolio is 
# balanced in order to keep to the correct percentages.
#     The files "stocks.txt" and "bonds.txt" were given in order to simulate future returns, and a constant return rate of 
# 2% was used for bank savings.
#     The savings in each broad category for each year is saved in a file called "retirementsimulation.txt". Different 
# retirement plans are plotted for comparisons at the end.



import matplotlib.pyplot as plt

# I saved the bonds.txt and stocks.txt files in the same directory as this script, so they are part of
# my project folder. 
with open("stocks.txt", "r") as myfile:
    stock_list = [float(i) for i in myfile.read().split('\n')]

with open("bonds.txt", 'r') as myfile:
    bond_list = [float(i) for i in myfile.read().split('\n')]

# I am going to make the stock list and bond list twice as long, so that way there can be a 100 year age range
# between the starting age and retirement age (even though this is not likely). I will do this by just repeating the
# stock list and bond list values, to simulate 100 years of changes in stock/bond returns.

stock_list.extend(stock_list)
bond_list.extend(bond_list)


class Cash:
    def __init__(self, amount, starting_percent, ending_percent, age_range):
        self.amount = amount
        self.starting_percent = starting_percent
        self.ending_percent = ending_percent
        self.age_range = int(age_range)
        self.percent_change = (ending_percent - starting_percent) / (age_range - 1)


class BankAccount(Cash):
    def __init__(self, amount, starting_percent, ending_percent, age_range):
        Cash.__init__(self, amount, starting_percent, ending_percent, age_range)

    def get_interest_on_account(self):
        self.amount *= 1.02


class BondInvestments(Cash):
    def __init__(self, amount, starting_percent, ending_percent, age_range):
        Cash.__init__(self, amount, starting_percent, ending_percent, age_range)

    def add_returns(self, year):
        self.amount *= (1 + bond_list[year])


class StockInvestments(Cash):
    def __init__(self, amount, starting_percent, ending_percent, age_range):
        Cash.__init__(self, amount, starting_percent, ending_percent, age_range)

    def add_returns(self, year):
        self.amount *= (1 + stock_list[year])


def make_sure_response_is_number(prompt):
    response = input(prompt)
    while response.isdigit() == False:
        response = input("Oops! Try again. Please enter only integers.\n" + prompt)
    return float(response)


def get_starting_and_ending_percents(prompt):
    response = input(prompt)
    while ',' not in response or len(response.split(',')) != 2 or (''.join(response.split(',')).isdigit() == False \
            and '.' not in response):
        response = input("Try again.\n" + prompt + 'Please respond with two comma separated numbers (no spaces).\n'
                                  'Example: "5,10"\n')
    return [float(i) for i in response.split(',')]


def make_retirement_plan(current_age, current_total, user_cash, user_savings, user_bonds, user_stocks, csv=False):

    global money_to_invest_each_year
    global annual_giving_percent

    ages = [current_age]
    yearly_value = [current_total]
    for year in range(user_cash.age_range):
        if annual_giving_percent != None:
            user_savings.get_interest_on_account()
            user_bonds.add_returns(year)
            user_stocks.add_returns(year)
            money_to_invest = money_to_invest_each_year * ((1 + (annual_giving_percent / 100))**year)
            total = user_cash.amount + user_savings.amount + user_bonds.amount + \
                    user_stocks.amount + money_to_invest
        else:
            user_savings.get_interest_on_account()
            user_bonds.add_returns(year)
            user_stocks.add_returns(year)
            total = user_cash.amount + user_savings.amount + user_bonds.amount + \
                    user_stocks.amount + money_to_invest_each_year

        age = year + (current_age + 1)
        ages.append(age)
        yearly_value.append(total)
        cash_percent = user_cash.starting_percent + (user_cash.percent_change * year)
        bank_savings_percent = user_savings.starting_percent + (user_savings.percent_change * year)
        bonds_percent = user_bonds.starting_percent + (user_bonds.percent_change * year)
        stocks_percent = user_stocks.starting_percent + (user_stocks.percent_change * year)
        # Re-balance the portfolio:
        user_cash.amount = cash_percent * total
        user_savings.amount = bank_savings_percent * total
        user_bonds.amount = bonds_percent * total
        user_stocks.amount = stocks_percent * total

        # Writes plan to file if csv == True
        if csv == True:
            with open("retirementsimulation.txt", "a") as myfile:
                myfile.write('\n' + ','.join([str(int(age)), str(user_cash.amount), str(user_savings.amount),
                                              str(user_bonds.amount),
                                              str(user_stocks.amount), str(total)]))

    return ages, yearly_value


if __name__ == '__main__':
    current_age = make_sure_response_is_number("What is your current age?\n")
    retirement_age = make_sure_response_is_number("What is your desired retirement age?\n")
    age_range = retirement_age - current_age

    current_cash = make_sure_response_is_number("How much do you currently have in your retirement savings as CASH?\n")

    current_savings = make_sure_response_is_number("How much do you currently have in your retirement savings as "
                                                   "BANK SAVINGS?\n")

    current_bonds = make_sure_response_is_number("How much do you currently have in your retirement savings as BOND "
                                                 "INVESTMENTS?\n")

    current_stocks = make_sure_response_is_number("How much do you currently have in your retirement savings as "
                                                  "STOCK INVESTMENTS?\n")

    total = current_cash + current_savings + current_bonds + current_stocks

    money_to_invest_each_year = make_sure_response_is_number("How much do you want to invest each year?\n")

    optional_annual_giving = input("Do you want to increase your annual giving by a certain percentage?"
                                   " Please enter 'yes' or 'no'.\n").lower().strip()
    annual_giving_percent = None
    if optional_annual_giving[0] == 'y':
        annual_giving_percent = make_sure_response_is_number("By what percentage do you want to increase your annual "
                                                             "giving by?\nDo not include the percent sign "
                                                             "in your response."
                                                             "\nEx: For a 1% increase, you would enter '1'.\n")

    print("\nFor the next few entries, please enter your responses as two integers separated by a comma, like '5,20'.\n"
          "For percentages, please respond using the actual percentage value.\nEx: For 5%, you would enter '5'; "
          "for 50%, you would enter '50'.\n")
    try:
        current_cash_percent, ending_cash_percent = get_starting_and_ending_percents("What is your desired starting "
        "percent and ending percent of your savings that you want saved as CASH?\n")


        current_bank_savings_percent, ending_bank_savings_percent = get_starting_and_ending_percents("What is your "
        "desired starting percent and ending percent of your savings that you want saved in the BANK?\n")

        current_bonds_percent, ending_bonds_percent = get_starting_and_ending_percents("What is your desired starting"
        " percent and ending percent of your savings that you want invested in BONDS?\n")


        current_stocks_percent, ending_stocks_percent = get_starting_and_ending_percents("What is your desired "
        "starting percent and ending percent of your savings that you want invested in STOCKS?\n")

        if (current_cash_percent + current_bank_savings_percent + current_bonds_percent + \
            current_stocks_percent != 100) or (ending_cash_percent + ending_bank_savings_percent + \
                                               ending_bonds_percent + ending_stocks_percent != 100):
            raise ValueError("Invalid percentages. Your starting and ending percentages should add up to 100.")

        user_cash = Cash(current_cash, current_cash_percent/100, ending_cash_percent/100, age_range)
        user_savings = BankAccount(current_savings, current_bank_savings_percent/100,
                                   ending_bank_savings_percent/100, age_range)
        user_bonds = BondInvestments(current_bonds, current_bonds_percent/100, ending_bonds_percent/100, age_range)
        user_stocks = StockInvestments(current_stocks, current_stocks_percent/100, ending_stocks_percent/100, age_range)


        with open("retirementsimulation.txt", "w") as myfile:
            myfile.write("Age,Cash,Savings,Bonds,Stocks,Total")
            total = current_cash + current_savings + current_bonds + current_stocks
            myfile.write('\n' + ','.join([str(int(current_age)), str(current_cash), str(current_savings),
                                          str(current_bonds), str(current_stocks), str(total)]))

        # User's Desired Plan
        ages , yearly_value = make_retirement_plan(current_age, total, user_cash, user_savings, user_bonds,
                                                   user_stocks, csv=True)


        # User's Desired Plan Graphed
        desired_plan = "{}% Cash, {}% Savings, {}% Bonds, {}% Stocks to\n" \
                       "{}% Cash, {}% Savings, {}% Bonds, {}% Stocks\n(YOUR Plan)".format(str(current_cash_percent),
                                                                             str(current_bank_savings_percent),
                                                                             str(current_bonds_percent),
                                                                             str(current_stocks_percent),
                                                                             str(ending_cash_percent),
                                                                             str(ending_bank_savings_percent),
                                                                             str(ending_bonds_percent),
                                                                             str(ending_stocks_percent))
        plt.plot(ages, yearly_value, 'o-', label=desired_plan)
    except ValueError as excpt:
        print(excpt)
        print("Cannot graph your desired plan.")


    # Alternative Plan 1
    cash_plan_1 = Cash(current_cash, 1, 0, age_range)
    savings_plan_1 = BankAccount(current_savings, 0, 0, age_range)
    bonds_plan_1 = BondInvestments(current_bonds, 0, .8, age_range)
    stocks_plan_1 = StockInvestments(current_stocks, 0, .2, age_range)

    ages_1, yearly_value_1 = make_retirement_plan(current_age, total, cash_plan_1,
                                                   savings_plan_1, bonds_plan_1, stocks_plan_1)
    # Plot Alternative Plan 1
    plt.plot(ages_1, yearly_value_1, 'mo-', label="100% Cash to 80% Bonds & 20% Stocks")

    # Alternative Plan 2
    cash_plan_2 = Cash(current_cash, 0, .2, age_range)
    savings_plan_2 = BankAccount(current_savings, 0, .8, age_range)
    bonds_plan_2 = BondInvestments(current_bonds, 0, 0, age_range)
    stocks_plan_2 = StockInvestments(current_stocks, 1, 0, age_range)

    ages_2, yearly_value_2 = make_retirement_plan(current_age, total, cash_plan_2,
                                                   savings_plan_2, bonds_plan_2, stocks_plan_2)
    # Plot Alternative Plan 2
    plt.plot(ages_2, yearly_value_2, 'go-', label="100% Stocks to 20% Cash & 80% Bank Savings")

    # Alternative Plan 3
    cash_plan_3 = Cash(current_cash, .5, .8, age_range)
    savings_plan_3 = BankAccount(current_savings, 0, .2, age_range)
    bonds_plan_3 = BondInvestments(current_bonds, 0, 0, age_range)
    stocks_plan_3 = StockInvestments(current_stocks, .5, 0, age_range)

    ages_3, yearly_value_3 = make_retirement_plan(current_age, total, cash_plan_3,
                                                   savings_plan_3, bonds_plan_3, stocks_plan_3)
    # Plot Alternative Plan 3
    plt.plot(ages_3, yearly_value_3, 'ro-', label="50% Cash and 50% Stocks to 80% Cash & 20% Bank Savings")

    # Alternative Plan 4
    cash_plan_4 = Cash(current_cash, 0, 0, age_range)
    savings_plan_4 = BankAccount(current_savings, 0, 0, age_range)
    bonds_plan_4 = BondInvestments(current_bonds, 1, .2, age_range)
    stocks_plan_4 = StockInvestments(current_stocks, 0, .8, age_range)

    ages_4, yearly_value_4 = make_retirement_plan(current_age, total, cash_plan_4,
                                                   savings_plan_4, bonds_plan_4, stocks_plan_4)
    # Plot Alternative Plan 4
    plt.plot(ages_4, yearly_value_4, 'ko-', label="100% Bonds to 20% Bonds & 80% Stocks")

    plt.xlabel('Age (years)')
    plt.ylabel('Retirement Savings Total Value ($)')
    plt.legend(shadow=True, loc="upper left")
    plt.title("Yearly Value of Different Retirement Plans")
    plt.ticklabel_format(axis='y', style='plain')
    # I found out how to format the y-axis so it doesn't switch to scientific notation for large numbers from:
    # https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html
    plt.show()
