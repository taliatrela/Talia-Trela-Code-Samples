# This script simulates PowerBall, but ignores the PowerPlay options. It allows the user to purchase
# a certain number of PowerBall tickets. Each time the user plays, it generates a winning ticket, and shows how much the user
# won, spent, and lost.

# There is also a manual test section at the end that verifies that the correct amount is returned.

import random


class PowerBallTicket:

    ticket_cost = 2
    list_of_white_balls = []
    list_of_red_balls = []
    jackpot = 100000000
    for number in range(1,70):
        list_of_white_balls.append(number)
    for number in range(1,27):
        list_of_red_balls.append(number)

    def __init__(self, white1=0, white2=0, white3=0, white4=0, white5=0, red=0):
        self.white1 = white1
        self.white2 = white2
        self.white3 = white3
        self.white4 = white4
        self.white5 = white5
        self.red = red

        copy_of_list_of_white_balls = PowerBallTicket.list_of_white_balls[:]

        list_of_white_balls_on_ticket = [self.white1, self.white2, self.white3, self.white4, self.white5]

        if self.white1 == 0:
            for index in range(len(list_of_white_balls_on_ticket)):
                    random_index = random.randint(0, len(copy_of_list_of_white_balls) - 1)
                    list_of_white_balls_on_ticket[index] = copy_of_list_of_white_balls[random_index]
                    copy_of_list_of_white_balls.remove(list_of_white_balls_on_ticket[index])
            self.white1 = list_of_white_balls_on_ticket[0]
            self.white2 = list_of_white_balls_on_ticket[1]
            self.white3 = list_of_white_balls_on_ticket[2]
            self.white4 = list_of_white_balls_on_ticket[3]
            self.white5 = list_of_white_balls_on_ticket[4]
            self.red = random.randint(1, 26)


    def __str__(self):
        return "{} {} {} {} {} {}".format(self.white1, self.white2, self.white3, self.white4, self.white5, self.red)

    def get_winnings(self, other):
        user_white_balls = [self.white1, self.white2, self.white3, self.white4, self.white5]
        winning_white_balls = [other.white1, other.white2, other.white3, other.white4, other.white5]
        num_matching_white_balls = 0
        total_winnings = 0
        for white_ball in user_white_balls:
            if white_ball in winning_white_balls:
                num_matching_white_balls += 1

        if self.red == other.red and num_matching_white_balls == 5:
            total_winnings = 100000000
        elif num_matching_white_balls == 5:
            total_winnings = 1000000
        elif self.red == other.red and num_matching_white_balls == 4:
            total_winnings = 50000
        elif num_matching_white_balls == 4:
            total_winnings = 100
        elif self.red == other.red and num_matching_white_balls == 3:
            total_winnings = 100
        elif num_matching_white_balls == 3:
            total_winnings = 7
        elif self.red == other.red and num_matching_white_balls == 2:
            total_winnings = 7
        elif self.red == other.red and num_matching_white_balls == 1:
            total_winnings = 4
        elif self.red == other.red:
            total_winnings = 4

        return total_winnings



def get_num_tickets():
    num_tickets = input("How many Powerball Tickets would you like to purchase?\n").strip()
    while num_tickets.isdigit() == False:
        num_tickets = input("How many Powerball Tickets would you like to purchase? "
                            "Please enter only integers.\n").strip()
    num_tickets = int(num_tickets)
    return num_tickets


def get_tickets(num_tickets):
    list_of_purchased_tickets = []
    global total_spent

    choose_own_numbers = input("Do you want to choose your own numbers for your tickets?"
                               " Please enter 'yes' or 'no'.\n").lower().strip()

    if choose_own_numbers[0] == 'y':

        for ticket in range(1, num_tickets + 1):
            white_numbers = input("Enter five numbers from 1 to 69 for the white balls"
                                  " for Ticket #{} (Ex: '1 2 3 4 5')\n".format(ticket)).split()
            if len(white_numbers) != 5:
                raise ValueError('Invalid response for white numbers. Response should be five numbers'
                                 ' between 1 and 69 and entered like "1 2 3 4 5"')
            for num in white_numbers:
                if num.isdigit() == False or int(num) < 1 or int(num) > 69:
                    raise ValueError('Invalid response for white numbers. Response should be five numbers'
                                     ' between 1 and 69 and entered like "1 2 3 4 5"')

            red_number = input("Enter a number from 1 to 26 for the red Powerball"
                               " for Ticket #{}:\n".format(ticket)).strip()
            if red_number.isdigit() == False or int(red_number) < 1 or int(red_number) > 26:
                raise ValueError('Invalid Powerball choice. Response should be an integer from 1 - 26.')

            white_numbers = [int(num) for num in white_numbers]
            red_number = int(red_number)
            list_of_purchased_tickets.append(PowerBallTicket(white_numbers[0], white_numbers[1], white_numbers[2],
                                                             white_numbers[3], white_numbers[4], red_number))
            total_spent += PowerBallTicket.ticket_cost

    elif choose_own_numbers[0] == 'n':
        for ticket in range(num_tickets):
            list_of_purchased_tickets.append(PowerBallTicket())
            total_spent += PowerBallTicket.ticket_cost

    else:
        raise ValueError('Invalid response.')

    return list_of_purchased_tickets


def go_again():
    keep_going = input("\nWould you like to play Powerball again?\n").lower().strip()
    while keep_going[0] != 'y' and keep_going[0] != 'n':
        keep_going = input("Would you like to play Powerball again? Please enter 'yes' or 'no'.\n").lower().strip()
    return keep_going



total_spent = 0
total_won = 0
net_loss = 0
keep_going = 'y'
while keep_going[0] == 'y':
    winnings_for_this_round = 0
    winning_ticket = PowerBallTicket()
    try:
        num_tickets = get_num_tickets()

        list_of_purchased_tickets = get_tickets(num_tickets)

        print()
        for index in range(len(list_of_purchased_tickets)):
            #print("PowerBall Ticket #{}:".format(index + 1), list_of_purchased_tickets[index])
            winnings = list_of_purchased_tickets[index].get_winnings(winning_ticket)
            total_won += winnings
            winnings_for_this_round += winnings

        net_loss = total_won - total_spent
        print("Winning Ticket:", winning_ticket)
        print("\n%23s: %9s" % ("Winnings for this round", '$' + str(winnings_for_this_round)))
        print("%23s: %9s" % ("Total spent", '$' + str(total_spent)))
        print("%23s: %9s" % ("Total winnings", '$' + str(total_won)))
        print("%23s: %9s" % ("Net loss", '-$' + str(-1 * net_loss)))

    except ValueError as excpt:
        print(excpt)
        print("Could not get all tickets, thus could not calculate total winnings for this round.")

    keep_going = go_again()



# Manual Test Section
print("\nManual Test Section")
winning_ticket = PowerBallTicket(1, 2, 3, 4, 5, 6)

print("\nTest for Jackpot (All matching numbers):")
my_ticket = PowerBallTicket(5, 4, 2, 3, 1, 6)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $1,000,000 (All white numbers the same):")
my_ticket = PowerBallTicket(5, 4, 2, 3, 1, 7)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $50,000 (Four matching white numbers plus the Powerball):")
my_ticket = PowerBallTicket(5, 4, 10, 3, 1, 6)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $100 for four matching white balls:")
my_ticket = PowerBallTicket(5, 4, 10, 3, 1, 7)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $100 for three matching white balls and the Powerball:")
my_ticket = PowerBallTicket(5, 4, 10, 3, 20, 6)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $7 for three matching white balls:")
my_ticket = PowerBallTicket(5, 4, 10, 3, 20, 7)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $7 for two matching white balls and the Powerball:")
my_ticket = PowerBallTicket(5, 4, 10, 25, 20, 6)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $4 for one matching white ball and the Powerball:")
my_ticket = PowerBallTicket(5, 30, 10, 25, 20, 6)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $4 for getting the Powerball only:")
my_ticket = PowerBallTicket(40, 30, 10, 25, 20, 6)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $0 for no matches:")
my_ticket = PowerBallTicket(10, 20, 30, 40, 50, 20)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $0 for two matching white balls only:")
my_ticket = PowerBallTicket(10, 20, 30, 2, 1, 20)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)

print("\nTest for $0 for one matching white ball only:")
my_ticket = PowerBallTicket(10, 20, 30, 40, 1, 20)
winnings = my_ticket.get_winnings(winning_ticket)
print("Winning Ticket:", winning_ticket)
print("My ticket:", my_ticket)
print("Winnings:", winnings)
