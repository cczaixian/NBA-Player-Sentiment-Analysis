#Project Topic: NBA Player Sentiment Analysis
####Submitted By: Haotian Huang

#####Overview:

>Basketball is a huge business in sports industry. In United States, winning is every NBA team's culture. General managers, coaches and all other analyst spare no effort to assess and improve their players' performance. Data Mining has proven to be one of the most useful technique to analyze players' performance.
The objective of my project is to utilize both structured and unstructured data to evaluate and predict players' performance.

#####Data Source: 

>Data mainly comes from the following 3 sources: NBA.com, Basketball-Reference.com, Twitter.

#####Data collection techniques:

>1. Connecting to the API of stats.nba.com and pass different parameter values to request all NBA players' basic information and game logs during 2014-15 season.

>2. Scraping players' twitter account and salaries data from basketball-reference.com.

>3. Using Twitter's official API to retrieve NBA players' tweet during 2014-15 season. 

#####Dataset description:

>Game log contains 21 indicators to evaluate players' on-court performance on a game.

  >Typical indicators include Win/Lost, Minutes, Points, Field Goals, Rebounds, Assists, Turnovers and Plus/Minus.
  
  >I gathered more than 100 players' game logs for 82 regular games during the 2014-15 season. More than 10,000 observations are collected.

>Players' basic information includes age, position, ID, team, salary and Twitter Account.

>Tweets or the messages players post on Twitter are collected from 10/28/2014 to 04/15/2015, which covers 2014-15 season.

#####Potential Methodology:

>Multiple Regression, Classification, Sentiment Analysis ( Natural Language Processing)
