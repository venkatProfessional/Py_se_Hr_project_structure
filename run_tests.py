import pytest

if __name__ == "__main__":
    pytest.main([
        "tests",                                      # 1. Run all test cases in `tests/` folder
        "-n", "1",                                    # 2. Run tests in 4 parallel workers (pytest-xdist)
        "--alluredir=reports/allure-results",         # 3. Allure results directory for reporting
        "--html=reports/report.html",                 # 4. Generate a human-readable HTML report
        "--self-contained-html",                      # 5. Embed CSS/JS in the HTML report
        "--capture=tee-sys",                          # 6. Show print/logging output in console and report
        "--tb=short",                                 # 7. Show short tracebacks on failure
        "--maxfail=5",                                # 8. Stop test run after 5 failures
        "-v",                                         # 9. Verbose output (see each test status)
    ])
