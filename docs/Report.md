# 🏏 Cricket Query AI

**Prepared for:** UMBC Data Science Master’s Degree Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  
**Author:** Charan Kumar Pathakamuri  

🔗 **GitHub Repository:**  https://github.com/cnaidu402/UMBC-DATA606-Capstone/

🔗 **LinkedIn:**  https://www.linkedin.com/in/charan-kumar/

🔗 **Video Link:** https://drive.google.com/file/d/1qiTNywDyGIaZi2DanD0LVTCyU08tF1eU/view?usp=sharing

🔗 **PPT Link:** https://docs.google.com/presentation/d/1gZn5iQdmS9uqDmjZ_k4eIMOmBIOIJgDB/edit?usp=sharing&ouid=101843104812874478278&rtpof=true&sd=true 

---

## 1. Background

### What is it about?
Cricket Query AI is a sophisticated **Text-to-SQL** and **Text-to-Chart conversational agent** powered by a **Large Language Model (LLM)**.  
The system acts as an **expert sports analyst** for the **Asia Cup cricket tournament**, allowing users to ask complex questions in plain English and receive accurate data responses with **rich, interactive visualizations**.

**Example query:**  
> *"Show me Virat Kohli's run progression over the years."*  

The agent responds by generating a **line chart** to visually display the trend.

### Why does it matter?
While Text-to-SQL systems provide data access, **raw tables often fail to convey insights effectively**.  
This project bridges the gap between **data retrieval and insight generation** by integrating **automated visualization**, leveraging the fact that humans process visual information more efficiently.

Cricket Query AI transforms analytics from simple querying into **dynamic visual data exploration**, making it accessible to **non-technical users**.

### Research Questions
- **SQL Generation:** How effectively can an LLM generate accurate SQL queries from complex natural language questions about Asia Cup datasets?
- **Training Strategy:** What contextual training strategy (schema, documentation, few-shot examples) best helps the model understand cricket terminology and query patterns?
- **Visualization Inference:** Can the agent correctly infer user intent and select the appropriate chart type (e.g., bar vs. line charts)?

---

## 2. Data

### Data Sources & Structure
- **Source:** Kaggle – *Asia Cup Cricket (1984–2022)*
- **Structure:** Relational database built in **Microsoft SQL Server**
- **Tables:** 8 CSV files, each treated as a separate table
- **Size & Period:** ~150 KB, covering years **1984–2022**

### Data Dictionary & Schema

| Table Name | Description | Key Columns |
|-----------|------------|-------------|
| `asiacup` | Match-level details for all Asia Cup games | Team, Opponent, Year, Runs_Scored, Wickets_Taken, Result |
| `champion` | Tournament history | Year, Host, Champion, Runner_Up, Player_Of_The_Series |
| `batsman_data_odiCareer` | ODI batting statistics | Player_Name, Runs, Strike_Rate, Centuries, Batting_Average |
| `bowler_data_odiCareer` | ODI bowling statistics | Player_Name, Wickets, Economy_Rate, Five_Wickets |
| `wicketkeeper_data_odiCareer` | ODI wicketkeeping statistics | Player_Name, Dismissals, Catches, Stumpings |
| *(T20I Tables)* | Equivalent T20 International statistics | Same structure as ODI tables |

### Features & Target
- **Target:** No traditional target variable; the system supports **dynamic query-based retrieval**
- **Features:** User’s natural language questions, mapped by the LLM to the SQL schema

---

## 3. Exploratory Data Analysis (EDA)

EDA was performed using **Jupyter Notebooks** to assess data structure and quality.

### Data Cleansing
- **Missing Values:** Rows with NULL values in *Runs Scored* or *Wickets Taken* (abandoned matches) were removed
- **Schema Verification:** Data types were validated to ensure correct SQL execution

### Key Visualizations & Insights
- **Batting Aggression:** Average run rate per year shows a clear upward trend, indicating modern batting aggression
- **Bowling Effectiveness:** Bowlers maintain strong wicket-taking ability despite higher scoring rates
- **Impact of Toss:** Winning the toss provides approximately a **7.1% advantage**
- **Star Power:** *Player of the Series* is typically from the championship-winning team

---

## 4. Model Training (RAG Implementation)

This project uses **Retrieval Augmented Generation (RAG)** rather than traditional model fine-tuning.  
Training involves indexing structured knowledge into a **Vector Database**.

### Training Process
Using the **Vanna.AI framework**, the model was trained on:

1. **DDL (Schema) Training**  
   - Indexed `CREATE TABLE` statements to teach schema, keys, and data types
2. **Documentation Training**  
   - Indexed plain-English explanations of cricket logic and metrics
3. **Few-Shot Learning**  
   - SQL–question pairs (“Golden Questions”) to teach correct T-SQL syntax and logic

### Development Environment
- **LLM:** Anthropic Claude 3 Haiku (optimized for speed and cost)
- **Vector Store:** ChromaDB (local)
- **Database:** Microsoft SQL Server (via ODBC)
- **IDE:** Visual Studio Code (Jupyter Notebooks)

---

## 5. Application of the Trained Model

The agent was deployed as a **Flask-based web application** (`Main_file.ipynb`).

### Interface
- Chat-based interface for English-language queries

### Functionality
- **Text-to-SQL:** Converts questions into executable SQL
- **Visualization:** Automatically selects and renders the best chart type using Plotly
- **Debugging Mode:** Displays generated SQL and raw query results for advanced users

---

## 6. Conclusion

### Summary
Cricket Query AI demonstrates how **RAG-powered LLMs** can democratize data analytics.  
By combining a low-latency LLM with a structured relational database, users can answer complex cricket questions and generate professional visualizations **without writing code**.

### Limitations
- **Ambiguity:** Subjective terms (e.g., *“best player”*) require explicit definitions
- **Schema Dependency:** The model is tightly coupled to the Asia Cup schema

### Future Directions
- **Multi-Agent System:** Manager agent to decompose complex tasks
- **Voice Interface:** Speech-to-Text support for verbal queries
- **Real-Time Data:** Integration with live cricket APIs

---

## 7. References

- **Vanna AI Documentation:** https://vanna.ai/docs/  
- **Anthropic API:** https://docs.anthropic.com/  
- **Plotly Python Graphing Library:** https://plotly.com/python/

---
