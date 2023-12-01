# Informatics-final-project

In this project I am trying to figure out a model for NFL sports betting using data from the 1992 season to 2002 season. The idea of the model is from Evan Osbourn. I imporved his model. In Osborne's model, he used OLS regression to estimate the point spread for NFL games. He estimated the game’s outcome using points scored and points allowed by each team as explanatory variables. “M” The estimated equation follows: 
Mit =.6044PPGHit - .4243PPGAHit - .5657PPGVit + .5537PPGAVit

Osborne's model has a win rate of 51.2%. To fit the model better Osborne incorporate a "filter" in his model. There is two kinds of filter 3 and 5. For example, if Osborne’s estimated outcome was M=5 (the home team wins by 5) and the line– 7 (the home team is predicted to lose by at least 7 points). Without the filter, Osborne would bet on the visiting team. With a three or five-point filter, he would not bet on this game at all. This means that the filter will only bet on games that is safe enough to win. With filter 3 Osborne has a win percentage of 0.532 and with filter 5 the win percentage is 0.542. 

I revised Osbourn's model by adding more information into the model. In Osbourn's model he only used data from the current season to predict games in the current year. I implemented stats from the previous season to improve the model. In the new model, the variable points per game (DPPG) was considered which takes the previous year’s points per game and this year’s points per game. This calculation was performed for both the home (H) and visiting (V) teams (DPPGH, DPPGAH, DPPGV, DPPGAV). The net home points were regressed for each game of the season (W) on these four variables.
WUit = 3.897 + 1.263DPPGHit – 0.994DPPGAit – 1.061DPPGVit + 0.741DPPGAVit   

The model that I imporved has a win percentage of 53.7%. With filter 3 mu win percentage is 0.597 and with filter 4 the win percentage is 0.623.

Link of my webapp: https://informatics-final-project-k9uzekqvtcmga9zamduder.streamlit.app/
