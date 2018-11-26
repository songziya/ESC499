## ESC499
This repository is dedicated to my graduation thesis. It contains all the files that are related to the thesis. 

### About 'RDDL model' folder
This folder contains different versions of navigation.rddl files

v1.3: Added interm variables, 'block behaviour' is demenstrated through a separate state variable 'v5'. 'v5' is updated through a cdf that contains all the interm variables.
 
v1.4: Replaced the entire 'interm variables' system with state-action constraints. TFplan is responsible for converting constraints into a part of the reward function. So the 'block behaviour' now should be regulated by the state-action constraints.  
### About 'TFplan files' folder
Contains all files that are part of the TFplaner(TFplan, tfrddlsim, etc). 
Note that all sections where I modified are indicated by the comment 'Scott:'


###  \*\*Updates & Progress\*\*
**Current task:** 
* Automate the process of converting State-Action Constraints into reward function in TFplanner.


[Oct 07 20:00-21:30] Debugged and ran navigation RDDL model in TFplanner(**Without block behaviour**)

Action constraints only works in 'action-preconditions' section, they DO NOT work in 'state-action-constraints' section.

[Oct 03 17:00-18:00] Modified Navagation_Nonlinear so that block behaviour is in state-action constraint block.

[20:00-21:30] Derived the formula for Backprop.

[Oct 01 20:00-21:30]: Running TFPlaner with the navigation sample on Linux virtual machine.

[Sep 29 13:00-15:00]: Setting up TFPlaner, emailed Thiago for installing instrcutions.

&emsp; Potentially useful link: [pyrddl module](https://pypi.org/project/pyrddl/)

[18:00-21:30]: Writing rddl domain+instance file for navigation problem with 'solid center obstacle'(absolutely no pass) 

[Sep 28 12:00-13:00]: Understanding backpropagation equation, clarified a typo with Wu Ga.

[Sep 27 22:00-23:00]: Trying to understand backpropagation equation, emailed Buser and Wu Ga with questions.

[Sep 16 19:00-24:00]: Setup PROST with VirtualBox, able to establish server. Complete the tutorial.

[Sep 15 11:30-16:00 17:30-19:00]: Learning RDDL Tutorial to section 2.7.1, Ran wildfire_mdp in cmd with visualizer.

&emsp; Useful link: [RDDL language description](https://sites.google.com/site/rddltutorial/rddl-language-discription)

&emsp; Syntax debugging: `./run rddl.parser.parser <PATH/FILENAME>`

&emsp; Simulation running: `./run rddl.sim.Simulator <DOMAINPATH> <rddl-policy> <inst-name> <viz-class-name>`

[Sep 14 16:00-18:00]: Learning git command lines. **Add-Commit-Push**

&emsp; Useful link: [Git command cheetsheet](https://education.github.com/git-cheat-sheet-education.pdf)



### \<Issue Encountered\>
[Sep 16]: \*\*\* No plan.py file in the either of the folder PROST_ROOT or RDDLSIM_ROOT (not able to run client)

\* Error when entering `vagrant up`. (It is unknown if this will affect future exercise yet)

![](https://github.com/songziya/ESC499/blob/master/General%20Documents/Issues/vagrant%20up.png)

[Sep 15]: \* Current wildfire_mdp.rddl file is different from the sample code in Tutorial. (But it's still functional)


