# AI Ops Assistant – Multi-Agent GenAI System


This project is a multi-agent AI Operations Assistant that accepts a natural language task, plans execution steps, calls real third-party APIs, and returns a structured response.


---

## Architecture Overview


The system follows a **Planner → Executor → Verifier** architecture:

### 1. Planner Agent
- Accepts a user task
- Uses LLM-based or rule-based logic
- Generates a structured JSON plan with steps and tools

### 2. Executor Agent
- Iterates over the plan steps
- Calls real third-party APIs (Weather, GitHub)
- Collects results

### 3. Verifier Agent
- Ensures all planned steps are executed
- Confirms output completeness
- Returns final structured response


## Integrated APIs

1. **Weather API**
   - Source: Open-Meteo
   - Used to fetch current weather details by city

2. **GitHub API**
   - Source: GitHub REST API
   - Used to search popular repositories by keyword


## Project Structure

ai_ops_assistant/
├── agents/
│ ├── planner.py
│ ├── executor.py
│ └── verifier.py
├── tools/
│ ├── weather_tool.py
│ └── github_tool.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md

## Setup Instructions (Run Locally)

### 1. Clone the repository
```bash
git clone <your-github-repo-link>
cd ai_ops_assistant
2. Install dependencies
pip install -r requirements.txt
3. Run the project
uvicorn main:app
4. Open in browser
http://127.0.0.1:8000

Environment Variables
Create a .env file (example below):

GITHUB_API_URL=https://api.github.com/search/repositories
WEATHER_API_URL=https://api.open-meteo.com/v1/forecast

---

## Example Prompts to Test the System

- Get the weather in Hyderabad and find popular Python GitHub repositories
- What is the current weather in Bangalore?
- Find top GitHub repositories for JavaScript
- Tell me the weather in Delhi
- Check the weather in Mumbai and search GitHub for machine learning projects

## Known Limitations / Trade-offs

- Rule-based planning instead of full LLM due to local constraints
- No caching of API responses
- Sequential execution (no parallel calls)

## Improvements With More Time

- Add LLM-based planner using local models
- Cache API responses
- Parallel tool execution
- Cost and performance tracking

