One way to solve this problem is by using dynamic programming approach. We can create a table to store the minimum number of coins required to make each value from 0 to the given total amount.

Here's the algorithm:

Create a table min_coins with size total + 1 and initialize all elements to infinity except for the element at index 0, which is set to 0.
For each coin in the list of coins, iterate over the table starting from the coin's value up to the total amount, and for each index i, update the value at min_coins[i] to be the minimum of its current value and min_coins[i - coin] + 1.
After iterating over all the coins, return the value at index total of the min_coins table.
