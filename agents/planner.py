def plan_task(user_input):
    """
    Converts user input into a structured execution plan
    """

    steps = []

    if "weather" in user_input.lower():
        steps.append({
            "tool": "weather",
            "input": "Hyderabad"
        })

    if "github" in user_input.lower():
        steps.append({
            "tool": "github",
            "input": "python"
        })

    return {
        "steps": steps
    }
