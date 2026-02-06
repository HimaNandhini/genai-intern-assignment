from fastapi import FastAPI
from agents.planner import plan_task
from agents.executor import execute
from agents.verifier import verify

app = FastAPI()

@app.get("/")
def run_agent(task: str = "Get weather for Hyderabad and find Python GitHub repos"):
    plan = plan_task(task)
    results = execute(plan)
    verification = verify(results)

    return {
        "plan": plan,
        "results": results,
        "verification": verification
    }

if __name__ == "__main__":
    # CLI execution still supported
    task = "Get weather for Hyderabad and find Python GitHub repos"
    plan = plan_task(task)
    print("PLAN:", plan)

    results = execute(plan)
    print("RESULTS:", results)

    verification = verify(results)
    print("VERIFICATION:", verification)
