

def first_bet():
    total = float(input("What is the total amount of money you are betting (in dollars)?"))

    odds_one_initial = float(input("What are the odds of team 1? (X to 1, replace X)?"))

    odds_two_initial = float(input("What are the odds of team 2? (X to 1, replace X)"))

    initial_bet = float(input("How much money did you bet (in dollars?)"))

    initial_team_bet = int(input("Which team did you bet on? (1 for team 1, 2 for team 2)"))

    remaining = total - initial_bet


    if initial_team_bet == 1:
        initial_win_profit = (odds_one_initial - 1) * initial_bet

    if initial_team_bet == 2:
        initial_win_profit = (odds_two_initial - 1) * initial_bet

    values = (initial_bet, initial_team_bet, remaining, initial_win_profit)

    return values



def later_bets(values):

    if values[1] == 1:
        odds_two_final = float(input("What are the odds of team 2? (X to 1, replace X)"))
        bet_value = round(values[0]/(odds_two_final - 1), 2)
        profit_one = values[3] - bet_value
        profit_two = bet_value * odds_two_final - (values[0] + bet_value)

    if values[1] == 2:
        odds_one_final = float(input("What are the odds of team 1? (X to 1, replace X)?"))
        bet_value = round(values[0]/(odds_one_final - 1), 2)
        profit_two = values[3] - bet_value
        profit_one = bet_value * odds_one_final - (values[0] + bet_value)

    information = (bet_value, profit_one, profit_two)

    if bet_value < values[2]:     
        return "Bet value: " + str(information[0]) + "\nTeam One Win: " + str(information[1]) + "\nTeam Two Win: " + str(information[2])

    return "Optimal bet exceeds total."


bet_vals = first_bet()
print (later_bets(bet_vals))



# Test1:  Bet initially on team 1, even odds, they are later in a winning position
# Odds 1 Initial 1.95
# Odds 2 Initial 1.8

# Bet 100 on team 1
# Odds 2 change to 3.6 (they are losing)
# Bet value: 38.46
# Team One Win: 56.54
# Team Two Win: -0.003999999999990678

# Test2: Bet initially on team 1, team with better odds, they are later in a losing position
# Odds 1 Initial 1.4
# Odds 2 Initial 2.6

# Bet 100 on team 1
# Odds 2 change to 1.2
# Bet value: 500.0
# Team One Win: -460.0
# Team Two Win: 0.0

# Test3: Bet initially on team 1, team with worse odds, they are later in a losing position.
# Odds 1 Initial 2.6
# odds 2 Initial 1.4

# Bet 100 on team 1
# Odds 2 1.1

# Bet value: 1000.0
# Team One Win: -840.0
# Team Two Win: 0.0

