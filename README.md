# SISMO-Py
Slime Mold Simulation (adapted for Energy Networks)
# WHAT IS IT?`
Enhanced SISMO (SImulation of Slime MOlds) through Python optimizations, accelerating its simulation of Physarum polycephalum foraging behavior
# HOW IT WORKS?
The plasmodium, along with the desired number of pseudopods and food sources, are distributed in specific coordinates on a map. The pseudopods then spread out to look for food sources. If a food source is found and the nutrients are used up, new pseudopodia may be attached with a certain probability. As long as there are still food sources available, the slime mold will keep searching for them. The thicker yellow tubes in the map represent the shortest paths between the food sources and the plasmodium. In nature, the slime mold uses distinct veins to transport food. The A* algorithm is used to determine the shortest path.

# HOW TO USE IT
Click the SETUP button to set up the pseudopodium (the yellow blob), the foodsources and the selected number of initial pseudopodia. Click the GO button to start the simulation. The movements of the pseudopoida are represented by yellow lines. The AMOUNT-PSEUDOPODIA slider sets the number of initial pseudopodia. The slider AMOUNT-FOODSOURCES sets the number of food sources. This slider is not needed, when the the number and coordinates of the food sources is given in the "Code" section. The SHOW-NUTRIENT-VALUE switch determines whether the number of nutrients from the food sources should be displayed or not. The switch SHOW-NETWORK determines whether the created network (blue dots), which is needed for the A* algorithm, should be displayed or not. The switch SHOW-INTERSECTION-POINTS determines whether the calculated intersection points (red crosses at the intersections of the pseudopodia) should be displayed or not.

# THINGS TO TRY

Change the number of pseudopodia and food sources. Display Nutrient values to see how quickly the pseudopodia consume them. Furthermore, the network points can be displayed. If this is the case, then one can see how the network is constructed for the A* algorithm. Furthermore the found intersection points can be displayed.

# EXTENDING THE MODEL

Since the simulation takes quite a long time, one could consider improving the performance. Also, the calculations of the intersections could be outsourced to Python, for example, and the calculations could be run in parallel there. Furthermore, one could let the pseudopodia disappear over the time. Since slime molds also do this in nature. Only the important thick veins remain the longest.

# CREDITS AND REFERENCES

Developed at Universität Klagenfurt (2022) via collaborative theses:

"Simulation and Mobility Planning with Slime Molds" (Emir Sinanovic)

"SISMO: A Slime Mold Algorithm for Traffic Management" (Kristina Wogatai)

# REQUIREMENTS
Please refer to the requirements.txt file for prerequisites to run the simulation.

# COPYRIGHT AND LICENSE
Copyright 2025 Karisch Michael.

CC BY-NC-SA 3.0

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.

This model was developed by Michael Karisch at Klagenfurt University for his bachelor's thesis, Performance Improvement of Self-Organizing Applications in Energy Networks
