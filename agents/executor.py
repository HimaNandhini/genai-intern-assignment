# executor.py

def execute_plan(plan):
    """
    Dummy executor function that simulates API calls.
    Replace with real API calls later.
    """
    results = []
    for step in plan.get("steps", []):
        if step["tool"] == "weather":
            results.append({"tool": "weather", "output": f"Weather info for {step['input']}"})
        elif step["tool"] == "github":
            results.append({"tool": "github", "output": f"GitHub repos for {step['input']}"})
    return results
