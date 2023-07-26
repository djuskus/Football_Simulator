import random

teams = {
  1: "Arizona Cardinals",
  2: "Chicago Bears",
  3: "Detroit Lions",
  4: "Green Bay Packers",
  5: "Minnesota Vikings",
  6: "Atlanta Falcons",
  7: "Carolina Panthers",
  8: "New Orleans Saints",
  9: "Tampa Bay Buccaneers",
  10: "Dallas Cowboys",
  11: "New York Giants",
  12: "Philadelphia Eagles",
  13: "Washington Commanders",
  14: "Los Angeles Rams",
  15: "San Francisco 49ers",
  16: "Seattle Seahawks",
  17: "Baltimore Ravens",
  18: "Cincinnati Bengals",
  19: "Cleveland Browns",
  20: "Pittsburgh Steelers",
  21: "Houston Texans",
  22: "Indiannapolis Colts",
  23: "Jacksonville Jaguars",
  24: "Tennesee Titans",
  25: "Buffalo Bills",
  26: "Miami Dolphins",
  27: "New England Patriots",
  28: "New York Jets",
  29: "Denver Broncos",
  30: "Kansas City Chiefs",
  31: "Las Vegas Raiders",
  32: "Los Angeles Chargers",
  33: "Los Poopulus Farters",

}

goodthings = {
  1: "glorius",
  2: "incredible",
  3: "beautiful"
}

badthings = {
  1: "stinky",
  2: "nasty",
  3: "foul"
}


for i in range(2024,2025):
  Winner = random.randint(1, 32)
  Loser = random.randint(1, 32)
  WinnerAdjective = goodthings[random.randint(1,3)]
  LoserAdjective = badthings[random.randint(1,3)]
  WinnerScore = random.randint(1,100)
  LoserScore = random.randint (1,100)
  if (LoserScore < WinnerScore) and (Winner !=Loser):
    print("Superbowl winner for year",i, "is the",WinnerAdjective,teams[Winner], "who destroyed the",LoserAdjective,teams[Loser], "by a score of", WinnerScore, "to", LoserScore)
  else:
    print ("These refs absolutely blow donky dong and don't know how to count correctly")
  
