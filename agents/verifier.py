# verifier.py

def verify_results(plan, results):
    """
    Dummy verifier function that checks if all steps have results
    """
    if len(plan.get("steps", [])) == len(results):
        return {"status": "success", "success": True}
    else:
        return {"status": "failed", "success": False}
