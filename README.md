# Off-The-Book-twitterBot
This serverless python twitter application reports the best odds per game in a list from the most popular sports books to use. The different files can be 
used to display the entire league as a whole or just a specific team. The odds come from a centralized JSON object provided by the-odds-api.com

This serverless application is run from Lambda in AWS. 

Algorithms used:

The odds are sorted for ML and spreads based on the HOME team. Some areas grey'd out.

Tweets out the highest paying parlay that any sportsbook can offer daily.

Project still in development

Sports leagues used: MLB, NFL

Twitter: @bookiebot_

AWS Resources Used:
- Lambda
- CloudWatch
- EventBridge
- SNS

Author: Daniel Higgins
