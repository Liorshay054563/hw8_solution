# start
import statistics

players: list[float] = []
above_2: int = 0
above_avg: int = 0
while True:
    high: float = float(input('Enter Player highest:'))
    if high == -999:
        break
    if not 1.60 <= high <= 3.0:
        print("not in range")
        continue
    players.append(high)
    if high >= 2:
        above_2 += 1

print(f"There are {len(players)} in range")
print(f"The high of the tallest player {max(players)}")
print(f"the high of lowest player {min(players)}")
print(f"the average of the players is {statistics.mean(players)}")
print(f"There are {above_2} players above 2m")
for i in range(1, len(players)):
    if high > statistics.mean(players):
        above_avg += 1 # allways show me zero !!!
print(f"There are {above_avg} players above the average")

#end
