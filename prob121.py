"""
Solve Project Euler Problem 121

Probability of winning a game

"""

import fractions
import itertools

import numpy as np

def generate_probs(N):
    """
    Generate the probability of drawing a colored chip on each turn up to N.
    """
    # Turn 0 -> 1 blue, 1 red
    # Turn 1 -> 1 blue, 2 red
    # etc.
    prob_blue = [fractions.Fraction(1, n+2) for n in range(N)]
    prob_red  = [fractions.Fraction(n+1, n+2) for n in range(N)]
    return prob_blue, prob_red

def outcome_prob(prob_blue, prob_red, blue_turns):
    """Compute the probability of getting a blue chip on the turns given."""
    got_blue = [i in blue_turns for i in range(len(prob_blue))]
    probs    = list(np.where(got_blue, prob_blue, prob_red))
    return reduce(lambda x,y: x*y, probs)

def generate_winning_prob(N):
    p_blue, p_red = generate_probs(N)
    winning_counts = [n for n in range(N+1) if n > (N)/2]
    total_prob = fractions.Fraction(0, 1)
    for count in winning_counts:
        count_prob = fractions.Fraction(0, 1)
        got_blues = itertools.combinations(range(N), count)
        for outcome in got_blues:
            count_prob += outcome_prob(p_blue, p_red, outcome)
        total_prob += count_prob
    return total_prob

def main():
    N = 15
    p_win = generate_winning_prob(N)
    print p_win, p_win.numerator, p_win.denominator
    print p_win.denominator / p_win.numerator
    
if __name__ == "__main__":
    main()
