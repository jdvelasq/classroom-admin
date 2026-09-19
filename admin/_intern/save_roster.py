def save_roster(roster):
    roster = roster.sort_values("nombre")
    roster.to_csv("roster.csv", header=False, index=False)
