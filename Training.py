Documentation = """ I want to create a chatbot that answers the questions raised by users. The data base is going to contain cricket data. Data base name: Cricket 
Table Names: 
asiacup: it is going to contain match records of asia cup which has happened several times 
batsman data odi: this table has batsmen records in odi format 
batsman data t20i: this table has batsmen records in t20i format
bowler data odi: This table contains bowlers records in odi format  
bowler data t20i: This table contains bowlers records in t20i format 
wicketkeeper data odi: This table has wicketkeeper data in odi format
wicketkeeper data t20i: This table has wicketkeeper data in t20i format
champions: This table has champion team, runner up team and other  details of that edition 
Columns description tables wise:
asiacup
•	Team : One team of the match
•	Opponent : Other team of the match
•	Format : Format of the tournament
•	Ground : Match venue
•	Year : Tournament Year
•	Toss : Win/Lose the toss
•	Selection : Selection After winning/losing toss
•	Run Scored : Total runs scored
•	Wicket Lost : Total wicket lost
•	Fours : Total scored fours
•	Sixes : Total scored sixes
•	Extras : Total extras given by opponent team
•	Run Rate : Batting Innings run rate
•	Avg Bat Strike Rate : Average batting strike rate
•	Highest Score : Highest individual run scored
•	Wicket Taken : Opponent teams total wickets taken
•	Given Extras : Extras given to opponent team
•	Highest Individual Wicket : Highest individual wickets taken of opponent team
•	Player Of The Match : Player of the match for good performance
•	Result : Winning/Losing the match
batsman data odi and batsman data  t20i
•	Player Name : Name of the batsman
•	Country : Country of the batsman
•	Time Period : Playing time period of the batsman
•	Matches : Total matches the batsman played
•	Played : Total matches the batsman batted
•	Not Outs : Total no of being not out
•	Runs : Total runs scored
•	Highest Score : Highest score of the batsman
•	Batting Average : Batting average of the batsman
•	Balls Faced : Total balls the batsman faced
•	Strike Rate : Strike rate of the batsman
•	Centuries : Total centuries the batsman scored
•	Fifties : Total fifties the batsman scored
•	Ducks : Total no of ducks batsman got
•	Fours : Total no of fours batsman scored
•	Sixes : Total no of sixes batsman scored
bowler data odi and bowler data  t20i
•	Player Name : Name of the bowler
•	Country : Country of the bowler
•	Time Period : Playing time period of the bowler
•	Matches : Total matches the bowler played
•	Played : Total matches the bowler bowled
•	Overs : Total no of overs the bowler bowled
•	Maiden Overs : Total no of maiden overs the bowler bowled
•	Runs : Total runs given by the bowler
•	Wickets : Total no of wickets taken by the bowler
•	Best Figure : Best bowling figure of the bowler
•	Bowling Average : Bowling average of the bowler
•	Economy Rate : Economy rate of the bowler
•	Strike Rate : Bowling strike rate of the bowler
•	Four Wickets : Total no of times the bowler taken four wickets in an innings
•	Five Wickets : Total no of times the bowler taken five wickets in an innings
Champion 
•	Year : Year of the tournament
•	Host : Host country of the tournament
•	No Of Team : Total no of teams participated in the tournament
•	Champion : Champion team of the tournament
•	Runner Up : Runner up team of the tournament
•	Player Of The Series : Best player of the tournament
•	Highest Run Scorer : Highest run scorer of the tournament
•	Highest Wicket Taker : Highest wicket taker of the tournament
wicketkeeper data odi and wicketkeeper t20i 
•	Player Name : Name of the wicketkeeper
•	Country : Country of the wicketkeeper
•	Time Period : Playing time period of the wicketkeeper
•	Matches : Total matches the wicketkeeper played
•	Played : Total matches the wicketkeeper played as wicketkeeper
•	Dismissals : Total no of dismissals done by the wicketkeeper
•	Catches : Total no of catches taken by the wicketkeeper
•	Stumpings : Total no of stumpings done by the wicketkeeper
•	Maximum Dismissals : Highest no of dismissals done by the wicketkeeper in an innings. 
Some KPIs: 
Conversion Rate = (Centuries/ (Centuries + Fifties) )*100
Innings per Century = Played/Centuries
Boundary= (((Fours*4) + (Sixes*6))/Runs)*100
Wickets per Match = Wickets/Matches
Win % = (COUNT(Matches where Result = 'Won’)/COUNT(Total Matches Played))*100
Dismissals per Innings  = Dismissals/Played 
"""
schema_text = """
CREATE TABLE [dbo].[asiacup](
	[Team] [nvarchar](50) NOT NULL,
	[Opponent] [nvarchar](50) NOT NULL,
	[Format] [nvarchar](50) NOT NULL,
	[Ground] [nvarchar](50) NOT NULL,
	[Year] [smallint] NOT NULL,
	[Toss] [nvarchar](50) NOT NULL,
	[Selection] [nvarchar](50) NOT NULL,
	[Run_Scored] [smallint] NULL,
	[Wicket_Lost] [tinyint] NULL,
	[Fours] [tinyint] NULL,
	[Sixes] [tinyint] NULL,
	[Extras] [tinyint] NULL,
	[Run_Rate] [float] NULL,
	[Avg_Bat_Strike_Rate] [float] NULL,
	[Highest_Score] [tinyint] NULL,
	[Wicket_Taken] [tinyint] NULL,
	[Given_Extras] [tinyint] NULL,
	[Highest_Individual_wicket] [tinyint] NULL,
	[Player_Of_The_Match] [nvarchar](50) NULL,
	[Result] [nvarchar](50) NOT NULL
) ON [PRIMARY]

CREATE TABLE [dbo].[champion](
	[Year] [smallint] NOT NULL,
	[Host] [nvarchar](50) NOT NULL,
	[No_Of_Team] [tinyint] NOT NULL,
	[Champion] [nvarchar](50) NOT NULL,
	[Runner_Up] [nvarchar](50) NOT NULL,
	[Player_Of_The_Series] [nvarchar](50) NOT NULL,
	[Highest_Run_Scorer] [nvarchar](50) NOT NULL,
	[Highest_Wicket_Taker] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_champion] PRIMARY KEY CLUSTERED 
(
	[Year] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[batsman data odi](
	[Player_Name] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Time_Period] [nvarchar](50) NOT NULL,
	[Matches] [tinyint] NOT NULL,
	[Played] [tinyint] NOT NULL,
	[Not_Outs] [tinyint] NOT NULL,
	[Runs] [smallint] NOT NULL,
	[Highest_Score] [tinyint] NOT NULL,
	[Batting_Average] [float] NOT NULL,
	[Balls_Faced] [smallint] NOT NULL,
	[Strike_Rate] [float] NOT NULL,
	[Centuries] [tinyint] NOT NULL,
	[Fifties] [tinyint] NOT NULL,
	[Ducks] [tinyint] NOT NULL,
	[Fours] [tinyint] NOT NULL,
	[Sixes] [tinyint] NOT NULL,
 CONSTRAINT [PK_batsman data odi] PRIMARY KEY CLUSTERED 
(
	[Player_Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[batsman data t20i](
	[Player_Name] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Time_Period] [nvarchar](50) NOT NULL,
	[Matches] [tinyint] NOT NULL,
	[Played] [tinyint] NOT NULL,
	[Not_Outs] [tinyint] NOT NULL,
	[Runs] [smallint] NOT NULL,
	[Highest_Score] [tinyint] NOT NULL,
	[Batting_Average] [float] NULL,
	[Balls_Faced] [smallint] NOT NULL,
	[Strike_Rate] [float] NOT NULL,
	[Centuries] [bit] NOT NULL,
	[Fifties] [tinyint] NOT NULL,
	[Ducks] [tinyint] NOT NULL,
	[Fours] [tinyint] NOT NULL,
	[Sixes] [tinyint] NOT NULL,
 CONSTRAINT [PK_batsman data t20i] PRIMARY KEY CLUSTERED 
(
	[Player_Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SE
QUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[bowler data odi](
	[Player_Name] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Time_Period] [nvarchar](50) NOT NULL,
	[Matches] [tinyint] NOT NULL,
	[Played] [tinyint] NOT NULL,
	[Overs] [float] NOT NULL,
	[Maiden_Overs] [tinyint] NOT NULL,
	[Runs] [smallint] NOT NULL,
	[Wickets] [tinyint] NOT NULL,
	[Best_Figure] [time](7) NOT NULL,
	[Bowling_Average] [float] NOT NULL,
	[Economy_Rate] [float] NOT NULL,
	[Strike_Rate] [float] NOT NULL,
	[Four_Wickets] [tinyint] NOT NULL,
	[Five_Wickets] [tinyint] NOT NULL,
 CONSTRAINT [PK_bowler data odi] PRIMARY KEY CLUSTERED 
(
	[Player_Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[bowler data t20i](
	[Player_Name] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Time_Period] [nvarchar](50) NOT NULL,
	[Matches] [tinyint] NOT NULL,
	[Played] [tinyint] NOT NULL,
	[Overs] [float] NOT NULL,
	[Maiden_Overs] [tinyint] NOT NULL,
	[Runs] [tinyint] NOT NULL,
	[Wickets] [tinyint] NOT NULL,
	[Best_Figure] [time](7) NOT NULL,
	[Bowling_Average] [float] NOT NULL,
	[Economy_Rate] [float] NOT NULL,
	[Strike_Rate] [float] NOT NULL,
	[Four_Wickets] [bit] NOT NULL,
	[Five_Wickets] [bit] NOT NULL,
 CONSTRAINT [PK_bowler data t20i] PRIMARY KEY CLUSTERED 
(
	[Player_Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[wicketkeeper data odi](
	[Player_Name] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Time_Period] [nvarchar](50) NOT NULL,
	[Matches] [tinyint] NOT NULL,
	[Played] [tinyint] NOT NULL,
	[Dismissals] [tinyint] NOT NULL,
	[Catches] [tinyint] NOT NULL,
	[Stumpings] [tinyint] NOT NULL,
	[Maximum_Dismissals] [tinyint] NOT NULL
) ON [PRIMARY]

CREATE TABLE [dbo].[wicketkeeper data t20i](
	[Player_Name] [nvarchar](50) NOT NULL,
	[Country] [nvarchar](50) NOT NULL,
	[Time_Period] [nvarchar](50) NOT NULL,
	[Matches] [tinyint] NOT NULL,
	[Played] [tinyint] NOT NULL,
	[Dismissals] [tinyint] NOT NULL,
	[Catches] [tinyint] NOT NULL,
	[Stumpings] [tinyint] NOT NULL,
    
	[Maximum_Dismissals] [tinyint] NOT NULL,
 CONSTRAINT [PK_wicketkeeper data t20i] PRIMARY KEY CLUSTERED 
(
	[Player_Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
"""

training_queries = [
    {
        "question": "Who won the Asia Cup in 2018 ?",
        "sql": """
USE Cricket;
SELECT Champion
FROM dbo.champion
WHERE Year = 2018;
"""
    },
    {
        "question": "How many career ODI runs does Virat Kohli have?",
        "sql": """
USE Cricket;
SELECT Runs
FROM dbo.[batsman data odi]
WHERE Player_Name = 'V Kohli';
"""
    },
    {
        "question": "What is the best bowling figure for J Bumrah in T20s?",
        "sql": """
USE Cricket;
SELECT Best_Figure
FROM dbo.[bowler data t20i]
WHERE Player_Name = 'J Bumrah';
"""
    },
    {
        "question": "List all wicketkeepers from Australia in the T20i table.",
        "sql": """
USE Cricket;
SELECT Player_Name
FROM dbo.[wicketkeeper data t20i]
WHERE Country = 'Australia';
"""
    },
    {
        "question": "Who are the top 5 all-time run-scorers in ODIs?",
        "sql": """
USE Cricket;
SELECT TOP 5 Player_Name, Runs
FROM dbo.[batsman data odi]
ORDER BY Runs DESC;
"""
    },
    {
        "question": "What is the head-to-head win-loss record between India and Pakistan in the Asia Cup?",
        "sql": """
USE Cricket;
SELECT 
    Team, 
    COUNT(Result) AS Wins
FROM 
    dbo.asiacup
WHERE 
    Result = 'Won'
    AND (
        (Team = 'India' AND Opponent = 'Pakistan')
        OR 
        (Team = 'Pakistan' AND Opponent = 'India')
    )
GROUP BY 
    Team;
"""
    },
    {
        "question": "Which bowler has the best economy rate in ODIs (minimum 3 matches played)?",
        "sql": """
USE Cricket;
SELECT TOP 1 Player_Name, Economy_Rate
FROM dbo.[bowler data odi]
WHERE Matches >= 3
ORDER BY Economy_Rate ASC;
"""
    },
    {
        "question": "What is the average number of dismissals for T20i wicketkeepers?",
        "sql": """
USE Cricket;
SELECT AVG(Dismissals) AS Average_Dismissals
FROM dbo.[wicketkeeper data t20i];
"""
    },
    {
        "question": "Which batsman has the best 50-to-100 conversion rate in ODIs?",
        "sql": """
USE Cricket;
SELECT 
    TOP 1 Player_Name,
    (CAST(Centuries AS float) / (Centuries + Fifties)) * 100 AS Conversion_Rate_Percent
FROM 
    dbo.[batsman data odi]
WHERE 
    (Centuries + Fifties) > 0  
ORDER BY 
    Conversion_Rate_Percent DESC;
"""
    },
    {
        "question": "What is the overall win percentage for India in the Asia Cup?",
        "sql": """
USE Cricket;
SELECT 
    (CAST(COUNT(CASE WHEN Result = 'Won' THEN 1 END) AS float) / COUNT(*)) * 100 AS India_Win_Percentage
FROM 
    dbo.asiacup
WHERE 
    Team = 'India';
"""
    },
    {
        "question": "Who was the Player of the Series in the 2022 Asia Cup?",
        "sql": """
USE Cricket;
SELECT Player_Of_The_Series
FROM dbo.champion
WHERE Year = 2022;
"""
    },
    {
        "question": "How many ducks does R Sharma have in ODIs?",
        "sql": """
USE Cricket;
SELECT Ducks
FROM dbo.[batsman data odi]
WHERE Player_Name = 'R Sharma';
"""
    },
    {
        "question": "How many 5-wicket hauls does M Muralitharan have in ODIs?",
        "sql": """
USE Cricket;
SELECT Five_Wickets
FROM dbo.[bowler data odi]
WHERE Player_Name = 'M Muralitharan';
"""
    },
    {
        "question": "Rank the top 3 ODI wicketkeepers by their total number of catches.",
        "sql": """
USE Cricket;
SELECT TOP 3 Player_Name, Catches
FROM dbo.[wicketkeeper data odi]
ORDER BY Catches DESC;
"""
    },
    {
        "question": "Which ground has hosted the most Asia Cup matches?",
        "sql": """
USE Cricket;
SELECT TOP 1 Ground, COUNT(*) AS Match_Count
FROM dbo.asiacup
GROUP BY Ground
ORDER BY Match_Count DESC;
"""
    },
    {
        "question": "Calculate the wickets per match for every bowler in the T20i table and show the top 5.",
        "sql": """
USE Cricket;
SELECT 
    TOP 5 Player_Name,
    (CAST(Wickets AS float) / Matches) AS Wickets_Per_Match
FROM 
    dbo.[bowler data t20i]
WHERE 
    Matches > 0
ORDER BY 
    Wickets_Per_Match DESC;
"""
    },
    {
        "question": "Find the top 3 most aggressive batsmen in T20s, based on the percentage of their runs from boundaries.",
        "sql": """
USE Cricket;
SELECT 
    TOP 3 Player_Name,
    (((Fours * 4) + (Sixes * 6)) / CAST(Runs AS float)) * 100 AS Boundary_Percent
FROM 
    dbo.[batsman data t20i]
WHERE 
    Runs > 0
ORDER BY 
    Boundary_Percent DESC;
"""
    },
    {
        "question": "Who has the most stumpings in ODI cricket?",
        "sql": """
USE Cricket;
SELECT TOP 1 Player_Name, Stumpings
FROM dbo.[wicketkeeper data odi]
ORDER BY Stumpings DESC;
"""
    },
    {
        "question": "How many times has Sri Lanka been the runner-up in the Asia Cup?",
        "sql": """
USE Cricket;
SELECT COUNT(*) AS Runner_Up_Count
FROM dbo.champion
WHERE Runner_Up = 'Sri Lanka';
"""
    },
    {
        "question": "What is the average number of centuries scored by players in the ODI batsman table?",
        "sql": """
USE Cricket;
SELECT AVG(Centuries) AS Average_Centuries
FROM dbo.[batsman data odi];
"""
    },
    {
        "question": "Does winning the toss and batting first lead to more wins in the Asia Cup? Show the win percentage.",
        "sql": """
USE Cricket;
SELECT 
    (CAST(COUNT(CASE WHEN Result = 'Won' THEN 1 END) AS float) / COUNT(*)) * 100 AS Win_Percent_Bat_First
FROM 
    dbo.asiacup
WHERE 
    Toss = 'Won' AND Selection = 'Bat';
"""
    },
    {
        "question": "What is the average dismissals per innings for MS Dhoni as a wicketkeeper in ODIs?",
        "sql": """
USE Cricket;
SELECT 
    (CAST(Dismissals AS float) / Played) AS Dismissals_Per_Innings
FROM 
    dbo.[wicketkeeper data odi]
WHERE 
    Player_Name = 'MS Dhoni' AND Played > 0;
"""
    },
    {
        "question": "List all players who appear in both the bowler data odi table and the batsman data odi table.",
        "sql": """
USE Cricket;
SELECT b.Player_Name
FROM dbo.[batsman data odi] AS b
INTERSECT
SELECT bo.Player_Name
FROM dbo.[bowler data odi] AS bo;

-- Alternative using JOIN:
-- SELECT b.Player_Name
-- FROM dbo.[batsman data odi] AS b
-- JOIN dbo.[bowler data odi] AS bo ON b.Player_Name = bo.Player_Name;
"""
    },
    {
        "question": "Who was the highest run-scorer in the 2016 Asia Cup?",
        "sql": """
USE Cricket;
SELECT Highest_Run_Scorer
FROM dbo.champion
WHERE Year = 2016;
"""
    },
    {
        "question": "Find the top 3 most dominant ODI bowlers, defined by the lowest number of innings played per five-wicket haul.",
        "sql": """
USE Cricket;
SELECT 
    TOP 3 Player_Name,
    (CAST(Played AS float) / Five_Wickets) AS Innings_Per_5_Wicket_Haul
FROM 
    dbo.[bowler data odi]
WHERE 
    Five_Wickets > 0
ORDER BY 
    Innings_Per_5_Wicket_Haul ASC;
"""
    }
]