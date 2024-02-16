# NFL Player Rushing Yards Prediction 🏈

## Introduction 🚀

### Problem Description 🎯
In this project, I predict the number of rushing yards by individual players in the National Football League (NFL). The goal is to develop a model capable of predicting player performance based on various factors such as the number of attempts, average yards per game, and other statistics. This could aid coaches, players, and analysts in better understanding the key performance factors in the game and in making decisions regarding player selection.

### Data Description 📊
The data used in this project was obtained from the website [Football DB](https://www.footballdb.com/statistics/nfl/player-stats/rushing/2022/regular-season) for educational purposes only, as part of a school project. It includes various statistics of NFL players for the 2022 season, including:

- Player Name
- Team: The team for which the player plays.
- Gms (Games): Number of games played.
- Att (Attempts): Number of rushing attempts.
- Yds (Yards): Total number of rushing yards (target variable for prediction).
- Avg (Average): Average yards per attempt.
- YPG (Yards Per Game): Average yards per game.
- Lg (Longest Run): Longest rush of the season.
- TD (Touchdowns): Number of touchdowns scored.
- FD (First Downs): Number of first downs achieved.

## Analysis 📈

### Decision Tree Regression:
Despite achieving a high R² (0.96), indicating a good fit of the model, the high MSE and MAE suggest potential for improvement in prediction accuracy.

### Algorithm Comparison:
'Random Forest' and 'Extra Trees' emerged as the most accurate algorithms. SVR was the least performing algorithm.

### Grid Search:
Improvement with 'Random Forest', demonstrated by a high R² (0.983), indicates a strong correlation between the selected parameters and the model's performance.

### Contribution:
This analysis confirms that for predicting sports statistics such as football yards, 'Random Forest' and 'Extra Trees' algorithms are more effective. Additionally, parameter optimization with Grid Search can significantly enhance prediction accuracy, which is crucial for developing reliable predictive models in sports analytics.
