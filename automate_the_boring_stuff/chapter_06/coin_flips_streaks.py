"""

Coin Flip Streaks

For this exercise, we’ll try doing an experiment.
If you flip a coin 100 times and write down an H for each heads and a T for each tails,
you’ll create a list that looks like T T T T H H H H T T.

If you ask a human to make up 100 random coin flips,
you’ll probably end up with alternating heads-tails results like H T H T H H T H T T—which looks random (to humans),
but isn’t mathematically random.

A human will almost never write down a streak of six heads or six tails in a row,
even though it is highly likely to happen in truly random coin flips.

Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up
in a randomly generated list of 100 heads and tails.

Your program should break up the experiment into two parts:
the first part generates a list of 100 randomly selected 'H' and 'T' values,
and the second part checks if there is a streak in it.

Put all of this code in a loop that repeats the experiment 10,000 times
so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row.

As a hint, the function call random.randint(0, 1) will return
a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

You can start with the following template:

import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values

    # Code that checks if there is a streak of 6 heads or tails in a row

print('Chance of streak: %s%%' % (number_of_streaks / 100))

Of course, this is only an estimate, but 10,000 is a decent sample size.

Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program,
but programmers are notoriously bad at math.

To create a list, use a for loop that appends a randomly selected 'H' or 'T' to a list 100 times.
To determine if there is a streak of six heads or six tails, create a slice like some_list[i:i + 6]
(which contains the six items starting at index i)
and then compare it to the list values ['H', 'H', 'H', 'H', 'H', 'H'] and ['T', 'T', 'T', 'T', 'T', 'T'].

"""
import random


def main() -> None:
    number_of_streaks = 0
    for experiment_number in range(10_000):  # Run 100,000 experiments total.

        # Code that creates a list of 100 'heads' or 'tails' values
        current_coin_flips = []
        for _ in range(100):
            flip_result = "H" if random.randint(0, 1) == 0 else "T"
            current_coin_flips.append(flip_result)

        # Code that checks if there is a streak of 6 heads or tails in a row
        for index in range(95):
            temp_slice = current_coin_flips[index : index+6]
            if temp_slice == ['H', 'H', 'H', 'H', 'H', 'H'] or temp_slice == ['T', 'T', 'T', 'T', 'T', 'T']:
                number_of_streaks += 1
                break

    print(f'Chance of streak: {number_of_streaks / 100:.2f}%')


if __name__ == "__main__":
    main()