# ENGLISH PREMIER LEAGUE (EPL) SEASON 2024-2025, ANALYSIS OF GOALS SCORED

## 1. Project Overview
A usual EPL season last from August to May of the next year. This analysis is looking at the current EPL 2024-25 season from August 2024 up to February 2025, which can provide statistical answers for the remaining of the season. 

### Current EPL Standings on February 20th, 2025
![alt text](img/20_feb_pltable.png) 

Figure 1. EPL standings posted on February 20th. The current top 5 teams are Liverpool, Arsenal, Nottingham Forest, Manchester City, and AFC Bournemouth.
## 2. Research question
The general question to be answered is when should one predict a player to score. 
This will be looked at through multiple steps:
1. What other numerical features in the data correlate to goal scoring?
2. At what time in the game have most goals happened?
3. Where in the field do most players score from?

### Questions to Keep in mind:
1. Analysis of home vs away team scores
2. How do top teams or players compare to overall statistics?
3. What other events in the match are relevant?
4. Corners that end in goal?
5. Markers for shots vs goals scored


## 3. Describe source of data
The data used for this project was downloaded from Kaggle: 
https://www.kaggle.com/datasets/excel4soccer/espn-soccer-data
This dataset contains detailed soccer match data in 2024-2025 season, compiled from ESPN soccer data API into csv files containing:
30,000+ Match fixtures information, including: Match lineups, Play-by-play information, Key events, Commentary, Team statistics, Player statistics, and more.

Narrowing down the focus of this research, different csv files were compiled into a single file that looks at all the EPL matches played on the 2024-25 season from 2024-08-16 to 2025-02-21

### The columns include: 
* match_id = a specific 5 digit id that identifies the match played
* game_date = year, month, day, and hour the match started [British Summer Time (BST)]
* team_name = Name identified to one of the 20 current EPL teams
* team_abb = 3 digit abbreviation for each team
* team_id = ID identified to one of the 20 current EPL teams
* home_team_id = ID identified to the team that is playing at home
* away_team_id = ID identified to the team that is playing away from home
* home_team_won = Shows True if the home team won the game or False if they lost or tied
* home_team_score = Number of goals scored by the home team
* away_team_score = Number of goals scored by the away team
* period = 1 for first-half or 2 for second-half
* clock = Minute marker of the match
* seconds = Second marker of the match
* player = Name of player
* play_id = ID identified to a specific type of play that was performed (ex: pass, shot, tackle, goal, save...)
* key_play_id = ID identified to a specific type of key play that was performed (ex:goal, shot, goal attempt...)
* playtype_id = A shorted ID identified to a specific type of play (ex: pass, shot, tackle, goal, save...)
* events = Short description from commentary on what just happened
* goal_scored = Value of 1 if a goal was scored or 0 if it is another type of key play that is not a goal. Null values indicate that it is neither
* fieldpositionX = X-coordinate position on the field that the player is at 
* fieldPositionY = Y-coordinate position on the field that the player is at
* fieldPosition2x and fieldPosition2y = Unsure of the meaning of these values

## 4. Describe how you cleaned and transformed data
### Searching through the Databse
![alt text](img/dB_diagram.png)

Figure 2. Image of how the database would look like for all the files gathered from Kaggle's ESPN soccer data.
##### Highlighted in yellow are the tables that were extracted using SQLite3 Editor on VSC. Highlighted in red are the primary keys that were used to JOIN the desired tables along with their respective columns (green dots). Query utilized is saved in the references folder as match_player_plays_sqlite3-query.

### Parsing game_date column and creating additional columns
#### It was necessary to change the game_date column to the datetime data type to further create the columns:
* year
* month
* day
* hour

### Removing null values from the clock and player columns with their respective rows
* Null values were removed from the clock column, especially because it a single row

### Fill in all null values for the goal_scored column
* Having 1 meaning goal scored and zero meaning no goal scored, it makes correlations easier to analyze

### Changing the clock data type and creating bins
* The clock data type was initially set as an object that includes extra time added to the 45 and 90 minute marks. 
* The column was transformed to the integer type so that the x-values can be used to track goal scoring over time and be able to include over time as separate intervals. The data was also added to 9' interval bins for further analysis.

### Install mpl soccer and adjust the x and y positions to fit the coordinates of a standard 105 by 68 meter pitch
* EPL pitch sizes will be used later for the analysis so it would be best to fit our data now on two new columns: xtimes105 and ytimes68 for the respective fieldpositionX and fieldPositionY features.

### Identify play_types and create new columns of the type of plays that involve goal scoring
##### The new columns created, identified by their playtype_id are:
* 70 is a goal, regular shot in freeplay, not own goal
* 137 is a goal with a header
* 98 is a goal from a penalty
* 173 is a goal from a volley
* 97 is an own goal
* 138 is a goal from a free kick

## 5. Key insights

### Features Affecting Goal Scoring
![alt text](img/scoring_heatmap.png)

Figure 3. The most relevant correlation values found in the data
#### There does not seem to be any relevant correlations between match time and goal_scoring. High correlations do appear for field positions, play types, and goals scored which will the focus of the analysis. 

### Most Likely Minute to Score
![alt text](img/goal_dist_perc.png)

Figure 4. Goal Percentage Distribution per minute match among EPL matches during the 2024-25 season
#### Looking at Figure 4, the graph experiences a fairlly normal distribution without much skewness. There does not seem to be any extreme irregularities to show a more predictable minute to score. The KDE line does show the probability of values across the match, where the highest peaks represents the modes of the data or highest probabilities of scoring.


### Most Likely Position to Score
![alt text](img/scatter_shots_vs_goals.png)

Figure 5. Scatterplot of shots and goals scored, where goals scored are shown as red crosses and shots as green dots
#### Looking at the figure 5, some notable fidnings are that shot distribution seems very similar thoroughout the whole match. Frequency of shots and goals are much lower on extra time because of less minutes being played. From visual inspection, it seems that the 63-72m interval experiences the most spread out goals along the y-axis and pass the 40 meter mark. That is a time to increase pressure on those high wings. Looking at a kdeplot will provide a better understanding of where goals are concentrated. 


![alt text](img/kde_goals_concentration.png)

Figure 6. KDE plot showing the density of goals scored
#### The KDE plot confirms our inference on goals scored in the 63-72min of the match. High goal scoring concentrations are mostly high between the penalty box and the 30meter mark. Overtime does seem to show a smaller range, high concentration aroud the penalty shot mark up to the 25 meter mark. The assumption would be that defending teams are defending tight by the goalkeeper, and attacking teams are not taking as many risks shooting from far. Also, noting that goal concentration seems to be opening up around the start of the second half up until the 63min interval where it begins to narrow again, likewise at the 27-36min interval. 

 

### Identifying the Types of Plays to Determine Which Plays are Correlated with Opportunities
![alt text](img/scatter_goals_byplay.png)

Figure 7. Scatterplot showing the different types of plays and the goals that were scored during all matches
#### Across all time intervls, we can see that pure shots are the most frequent way that goals are scored. However, looking at other play types, we see that header goals are overtaking the 18m mark in the 27-36min, 54-63min, and overtime. It looks like volleys sort of make an appearance mostly within the 18m mark; they are the least relevant closer to the end of each half. Own goals are as expected within the penalty box, and penalties have a fixed position, so it is difficult to calculate their frequency since they overlap. 

##

![alt text](img/heatmap_shots_vs_goals.png)

Figure 8. Heatmap comparing shots that were not converted into goals (shots off target and shots on target) along with headers that were converted into goals against goals scored.
#### Both shots off target and shots on target signal to the highest percentage being in the middle (20-40m on the x-axis), meaning that most shots coming from this position did not end up in goals. Goals scored show that most goals have been scored right inside the middle of the penalty box (0-20m from the x-axis) as it is the easiest place on the field to tap the ball and score. An interesting finding is that while most headers were scored in the middle of the penalty box, 33% of headers were scored near the first post on the right side of the attacking team; likewise the fewest number of shots that were not converted into goals were taken from the same position. Looking at the goals scored, we see that 21% of goals are scored in that same position, not a small number and should not go unnoticed. Taking more shots closer to the near post on the right side of the attacking team has prospects to open up a lot of goal scoring opportunities. 



## Future Recommendation/Areas of Study
* Perform the same analysis on other leagues to see if patterns differ from this one. The ESPN databse has access to all other leagues and the SQL query can be modified to get their data imported isntead of EPL.
* It might be possible to adjust the query to gather play by play data of players in the same team. This could help analyze passing and position patterns of each team. 
