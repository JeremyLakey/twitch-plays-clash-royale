import sys
import random

# Challenge win rate approximator

NUM_OF_CHALLENGES = 10000000
RATE = .7

def approx_win_rate(rate=RATE, num_games=NUM_OF_CHALLENGES):
    w = 0
    l = 0
    n = num_games
    while n > 0:
        w2 = 0
        l2 = 0
        n -= 1

        while w2 < 12 and l2 < 3:
            if random.random() < rate:
                w2 += 1
            else:
                l2 += 1

        if w2 >= 12:
            w += 1
        else:
            l += 1

    print("Wins: " + str(w))
    print("Loses: " + str(l))
    print("Rate: " + str((w / num_games) * 100) + "%")




if __name__ == "__main__":
    if len(sys.argv) == 1:
        approx_win_rate()