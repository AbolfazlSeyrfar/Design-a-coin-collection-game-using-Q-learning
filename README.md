# Reinforcement Learning/ Design a coin collection game from scratch using standard Q-learning

Consider an n*n environment with locations (i; j). A miner begins at location (1; 1) and can travel UP, LEFT, DOWN, or RIGHT. 

There is a gold mine at location (n; 1) and miner's home is at location (1; n). The miner begins with 0 coins in his backpack. Each time he visits the mine, he can get one gold. The maximum amount of gold that he can carry is given by some constant integer G > 0. The miner and the gold mine cannot be on the same location (n; 1); instead he visits the gold mine by first traveling to a location that is adjacent to the gold mine (either(n-1; 1) or (n; 2)) and then taking an action that would place himself on the mine. This results in the miner acquiring one more gold provided that he is not carrying G golds already, and meanwhile, the miner's location remains the same. He can visit her home whenever he wants, similarly by first traveling to a location that is adjacent to his home, and taking an action that would place himself on top of his home. This results in him unloading all the gold he carries to his home. He receives the amount of gold he carries as the reward. Similarly, his location remains the same in this process.

![image](https://user-images.githubusercontent.com/97136976/148145782-cdb8c5ea-b190-48bd-af9d-9860b7901566.png)





By assuming n = 5 and G = 3, the cumulative reward in each step is calculated using standard Q-learning to find the optimal policy. 


