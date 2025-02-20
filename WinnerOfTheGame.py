"""
Steve and Harvey are playing a game against each other. In the game they are given with N keys,
where N-1 keys are silver coated and one is gold-plated. P is the position of the gold plated
key which is the correct key. While playing the game, Steve and Harvey have to take turns and in
each turn they have to choose consecutive M keys which should include the gold key and reverse their order.
To win the game, one has to put the gold-plated key in the position of X. Steve starts the game


Determine the winner of the game. The game may end in draw. Assume steve and harvey play optimally.


Note: Indexing is 1-based.


Input
The first line contains an integer N representing the number of keys.
The second line contains an integer P representing the position of gold-plated keys.
The third line contains an integer M, representing number of consecutive keys that needs to be reversed.
The fourth line contains an integer X, representing the winning position.


Output


Print the name of the player who wins "Steve" or "Harvey" or "Draw".


Constraints


1 <= N,P,M,X <= 10 power 5


Example:
Input: 4,1,2,4 (N,P,M,X respectively)
Output: Draw


INput: 3,1,2,2 (N,P,M,X respectively)
Output: Steve


Explanation: There are three keys in total. The first one is a gold-plated key.
On each turn, players must choose two consecutive keys and reverse their order .
The winning position is two. Steve starts playing the game, so he can just choose the first two keys and reverse
their order. In this turn, he will be able to put a gold key on the winning position. The answer is steve

"""
