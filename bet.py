

class Bet:



    # total: Total amount of starting dollars excluding what was first bet.
    # teamOneBet: The value bet on team one.
    # teamTwoBet: The value bet on team two.
    # teamOneOdds: The odds of team one at that specific bet time.
    # teamTwoOdds: The odds of team two at that specific bet time.
    # teamOneWinProfit: The profit that the user would gain from team one winning.
    # teamTwoWinProfit: The profit that the user would gain from team two winning.
    # team: The team that the user last bet on (1 or 2).
    def __init__(self, total = 0, teamOneBet = 0, teamTwoBet = 0, teamOneOdds = 1, teamTwoOdds = 1, team = 0):
        self.total = total
        self.teamOneBet = teamOneBet
        self.teamTwoBet = teamTwoBet
        self.teamOneOdds = teamOneOdds
        self.teamTwoOdds = teamTwoOdds
        self.teamOneWinProfit = (teamOneOdds - 1) * teamOneBet
        self.teamTwoWinProfit = (teamTwoOdds - 1) * teamTwoBet
        self.team = team


    def sameTeamBet(self):
        laterOdds = float(input("What are the odds of the team you are betting for? (X to 1, replace X)"))
        laterBet = float(input("How much are you betting for this team?"))
        if self.team == 1:
            totalProfit = round(self.teamOneWinProfit + laterBet * (laterOdds - 1), 2)
            print("Bet value: " + str(self.teamOneBet + laterBet) + "\nTeam One Win: " + str(totalProfit) + "\nTeam Two Win: " + str(-1*(self.teamOneBet + laterBet)))
            return Bet(self.total - laterBet, self.teamOneBet + laterBet, self.teamTwoBet, laterOdds, self.teamTwoOdds, 1)

        if self.team == 2:
            totalProfit = round(self.teamTwoWinProfit + laterBet * (laterOdds - 1), 2)
            print("Bet value: " + str(self.teamTwoBet + laterBet) + "\nTeam One Win: " + str(-1*(self.teamTwoBet + laterBet)) + "\n Team Two Win: " +  str(totalProfit))
            return Bet(self.total - laterBet, self.teamOneBet, self.teamTwoBet + laterBet, self.teamOneOdds, laterOdds, 2)

        return "Not a valid team chosen"


    def differentTeamBet(self):

        laterOdds = float(input("What are the odds of the team you are betting for? (X to 1, replace X)"))
        if self.team == 1:
            betValue = round(self.teamOneBet/(laterOdds - 1), 2)
            profitInitial = round(self.teamOneWinProfit - betValue, 2)
            profitLater = round(betValue * (laterOdds - 1) - (self.teamOneBet + betValue), 2)
            information =  (betValue, profitInitial, profitLater)
            if betValue <= self.total:
                print("Bet value: " + str(information[0]) + "\nInitial Team Win: " + str(information[1]) + "\nChanged Team Win: " + str(information[2]))
                return Bet(self.total - betValue, self.teamOneBet, betValue, 0, laterOdds, 2)

        if self.team == 2:
            betValue = round(self.teamTwoBet/(laterOdds - 1), 2)
            profitInitial = round(self.teamTwoWinProfit - betValue, 2)
            profitLater = round(betValue * (laterOdds - 1) - (self.teamTwoBet + betValue), 2)
            information =  (betValue, profitInitial, profitLater)
            if betValue <= self.total:
                print("Bet value: " + str(information[0]) + "\nInitial Team Win: " + str(information[1]) + "\nChanged Team Win: " + str(information[2]))
                return Bet(self.total - betValue, betValue, self.teamTwoBet, laterOdds, 0, 1)

        return "betValue is greater than total amount."



def main():

# 90 = Total
# 10 = Initial Bet
# 0 = The odds 1st team
# 3 = The odds 2nd team
# 1/2 = Team
    test = Bet(90, 10, 0, 3, 0, 1)

    while (True):

        betType = input("1 for betting on same team, 2 for betting on other team")

        if betType == '1':
            test = test.sameTeamBet()
        
        if betType == '2':
            test = test.differentTeamBet()
if __name__ == "__main__":
    main()

    

# bet_vals = first_bet()
# print (later_bets(bet_vals))



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


