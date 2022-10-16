
# Bowling Score

The calculation of the bowling score is executed by the module bowlingGame, which has two separate moduls to calculate explicitly 
the game results as well as the total game scores as specified [hier ](https://www.liveabout.com/bowling-scoring-420895)

the bowlingThrows modul is responsable to generate randomly the number of pins which remained staying. This result would be pass to BowlingGame modul to calculate the result

the ScoreTable modul shows graphically the results of every frame and the reached total scores till the current frame
the throws should be done by clicking on the button on the GUI.

## dependencies
In order to run the bowling game, the pytq5 library should be installed. The easy way is directly to install this bibliotec using pip
        python3.? -m pip install Pytq5
or, just install the requirements on the file requirements.txt
        python3.? -m pip install -r .requirements.txt
it is also possible to install the bowlingScore modul as a library using the toml file 
        python3.? -m pip install -e .
using the last way will enable to test or run the bowlingScore modul using the already written test files in the 
BowlingScore/src/tests directory 

## set up

after the dependencies have been installed, it could be possible to run the file testBowlingGame.py which runs the bowlingScore modul and test the calculation of the results and scores of the game.
the file test_bowlingScoreTable.py runs the GUI Score Table to start gaming!

