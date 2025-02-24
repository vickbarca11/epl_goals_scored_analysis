# demo
 Initial repository testing Github Desktop

#### Based on all findings so far, the main question is when is the best moment to watch soccer and see the most goals:

##### Data to support this question:
* Focusing only on key plays, which removes of null values. 
* Main outliers are found in home_team_score and away_team_score, which we will be avoiding on this question.
* High positive correlation between: 
    * hour and key_play_id
    * year and key_play_id
    * goal_scored and fieldpositionX
    * goal_scored and fieldpositionY
* High negative correlation between:
    * goal_scored and seconds
    * month and key_play_id


#### This findings should help us answer:
* What part of the season shows that a player is more likely to score a goal?
* What month shows that a player is more likely to score a goal?
* What hour of the day shows that a player is more likely to score a goal?
* What minute of the match shows that a player is more likely to score a goal? 
* What player position shows that a player is more likely to score a goal?