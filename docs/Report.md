Cricket Query AI
Prepared for: UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang Author: Charan Kumar Pathakamuri

GitHub Repo: https://github.com/cnaidu402/UMBC-DATA606-Capstone/
LinkedIn Profile: https://www.linkedin.com/in/charan-kumar/
1. Background
What is it about? 🏏
This project focuses on creating Cricket Query AI, a sophisticated Text-to-SQL and Text-to-Chart conversational agent using a Large Language Model (LLM). This AI will act as an expert sports analyst for the Asia Cup cricket tournament. Users can ask complex questions in plain English, and the system will respond not only with precise data but also with rich, interactive visualizations. For example, a user could ask, "Show me Virat Kohli's run progression over the years," and the agent would generate a line chart to display the trend visually.

Why does it matter? 💡
While Text-to-SQL systems democratize data access, raw numbers in a table don't always tell the full story. The human brain processes visual information far more effectively. By integrating automated visualization generation, this project bridges the final gap between raw data and true insight. It allows non-technical users to not only query the data conversationally but also to see the patterns, trends, and comparisons instantly. This transforms the user experience from simple data retrieval to dynamic, visual data exploration.

What are your research questions? 🤔
How effectively can an LLM generate accurate SQL queries from complex, natural language questions related to the Asia Cup cricket datasets?
What is the most effective contextual training strategy (using schema, documentation, and few-shot examples) for the LLM to master cricket-specific terminology and query patterns?
Can the LLM agent correctly infer the user's intent for visualization and choose the most appropriate chart type (e.g., bar chart for comparison, line chart for time-series, pie chart for composition)?
2. Data
Data Sources
Dataset Link: https://www.kaggle.com/datasets/hasibalmuzdadid/asia-cup-cricket-1984-to-2022 s The knowledge base for the LLM agent will be a relational database (e.g., SQLite) created from the 8 provided CSV files, with each file becoming a table. This structured environment is what the agent will query and visualize.

asiacup.csv
champion.csv
batsman data odi.csv & batsman data t20i.csv
bowler data odi.csv & bowler data t20i.csv
wicketkeeper data odi.csv & wicketkeeper data t20i.csv
3. The LLM System Workflow
The project's core is the LLM's ability to act as a multi-talented "Reasoning Engine" that can translate natural language into both database queries and visualization code.

The workflow is a multi-step process:

Question Understanding: The user asks a question like, "Compare the strike rates of the top 5 run-scorers in the 2022 T20I tournament."

SQL Generation: The LLM, using its contextual training (schema, docs, examples), generates the appropriate SQL query to retrieve the necessary data from the database.

Data Retrieval: The SQL query is executed, and the results are returned as a data structure (e.g., a Pandas DataFrame).

Visualization Intent & Code Generation: The LLM analyzes both the original question and the data results. It recognizes the intent to "compare" and determines that a bar chart is the best visualization. It then generates the required Python code using the Plotly library to create this chart, ensuring correct labels, titles, and data mapping.

Response Delivery: The final output presented to the user includes both the data table and the interactive Plotly visualization.

Technologies Used
Language: Python
LLM Framework: Vanna.AI (or a similar framework like LangChain)
LLM: Google Gemini (or another powerful model)
Database: SQLite / MS SQL Server
Data Manipulation: Pandas
Visualization: Plotly
Web Framework: Flask
