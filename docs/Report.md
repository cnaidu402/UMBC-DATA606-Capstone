4. Exploratory Data Analysis (EDA)

This phase was critical for understanding the datasets, identifying quality issues, and preparing the data to serve as a reliable knowledge base for the LLM agent.

4.1. Data Cleansing and Preparation

Data Loading: All 8 CSV files were loaded into separate Pandas DataFrames.

Handling Missing Values (Nulls):

A helper function, checknull(), was defined to systematically count missing values.

def checknull(df):
    return df.isnull().sum()


The asiacup.csv file had several rows with missing data. These rows were dropped using dropna() to ensure all match records are complete.

The champion.csv file had "Not Awarded" text in the 'Player Of The Series' column, which was replaced with None to be handled correctly.

Data Type Correction: Numeric columns used for analysis (e.g., 'Run Rate', 'Avg') were converted to float or int types to ensure calculations are possible.

Player Name Standardization: A key challenge was the inconsistent player names (e.g., "Arjuna Ranatunga" vs. "A Ranatunga"). A fuzzy matching function was created to compare players based on their last name (e.g., "Ranatunga") in a case-insensitive way. This was essential for accurately linking the champion table to the player stats tables.

4.2. Visualizations and Interpretations

Interactive visualizations were generated using Plotly to answer key analytical questions.

Visualization 1: Average Run Rate per Year (ODI)

Question: Has the pace of scoring in ODI matches changed over time?

import plotly.express as px

# Filter for ODIs and group by 'Year'
odi_matches = asia_cup[asia_cup['Format'] == 'ODI']
avg_run_rate_per_year = odi_matches.groupby('Year')['Run Rate'].mean().reset_index()

# Create the interactive bar graph
fig = px.bar(
    avg_run_rate_per_year,
    x='Year',
    y='Run Rate',
    title='Average Run Rate per Year in ODI Matches',
    text='Run Rate'
)
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.show()


Interpretation: The bar chart shows a clear and steady upward trend in average run rates. The scoring rate, which was often below 4.0 runs per over in the 1980s, has consistently climbed to well over 4.5 in recent tournaments. This visually confirms the shift towards more aggressive batting in modern ODI cricket.

Visualization 2: Does Winning the Toss Mean Winning the Match?

Question: How much of an advantage does winning the coin toss provide?

import plotly.graph_objects as go

# Filter for toss winners and check if they also won the match
toss_winners = asia_cup[asia_cup['Toss'].str.lower() == 'win'].copy()
toss_winners['Toss Winner Won Match'] = toss_winners['O/T Result'].str.lower() == 'win'

# Get counts for the chart
outcome_counts = toss_winners['Toss Winner Won Match'].value_counts()
labels = outcome_counts.index.map({True: 'Won the Match', False: 'Lost the Match'})
values = outcome_counts.values

# Create the Donut Chart
fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    hole=.4,
    marker_colors=['deepskyblue', 'indianred'],
    textinfo='percent+label'
)])
fig.update_layout(title_text='Does Winning the Toss Mean Winning the Match?')
fig.show()


Interpretation: The donut chart reveals a near 50/50 split. Teams that win the toss win the match slightly more often than they lose, but the advantage is minimal. This suggests that winning the toss is not a decisive factor in winning the game on its own.

Visualization 3: Source of "Player of The Series" Awards

Question: Does the tournament's best player usually come from the winning team? (This required our fuzzy name matching to link tables).

# --- This code assumes 'champion_filtered' DataFrame is already created ---
# --- with 'Award Category' (Champion Team, Runner Up Team, Other Team) ---
# --- which was generated using the fuzzy name matching logic ---

# category_counts = champion_filtered['Award Category'].value_counts()

# fig = go.Figure(data=[go.Pie(
#     labels=category_counts.index,
#     values=category_counts.values,
#     hole=.4,
#     textinfo='percent+label'
# )])
# fig.update_layout(title_text='Player of The Series Award Distribution')
# fig.show()


Interpretation: The analysis (visualized as a donut chart) showed that the vast majority of "Player of The Series" awards are given to players from the champion (winning) team. A smaller portion goes to the runner-up team, and it is extremely rare for a player from another team to win. This indicates a strong bias towards selecting the best player from one of the top two teams.
