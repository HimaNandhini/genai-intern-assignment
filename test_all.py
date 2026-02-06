from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_results

# Example prompts
example_prompts = [
    "Get the weather in Hyderabad and find popular Python GitHub repositories",
    "What is the current weather in Bangalore?",
    "Find top GitHub repositories for JavaScript",
    "Tell me the weather in Delhi",
    "Check the weather in Mumbai and search GitHub for machine learning projects"
]

def run_all_tests():
    total = len(example_prompts)
    passed = 0

    for idx, prompt in enumerate(example_prompts, start=1):
        print(f"\n--- Test {idx}: {prompt} ---")
        try:
            plan = plan_task(prompt)
            execution_results = execute_plan(plan)
            verification = verify_results(plan, execution_results)

            # Basic check: verification should confirm all steps executed
            if verification.get("status", "").lower() == "success" or verification.get("success") == True:
                print("✅ Test Passed")
                passed += 1
            else:
                print("❌ Test Failed")
        except Exception as e:
            print("❌ Test Failed due to error:", e)

    print("\n--- Summary ---")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    if passed == total:
        print("🎉 All tests passed! Your workflow is fully functional.")
    else:
        print("⚠️ Some tests failed. Check errors above before submission.")

if __name__ == "__main__":
    run_all_tests()
