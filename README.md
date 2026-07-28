# Auto Test Demo

A demo project for automated testing with CI/CD pipeline, showcasing API testing and UI automation.

自动化测试 Demo 项目，集成 CI/CD 流水线，用于展示接口测试和 UI 自动化测试能力。

---

## Project Structure

```
auto-test-demo/
├── .github/workflows/test.yml    # CI/CD pipeline config
├── pages/
│   └── demo_page.py              # POM: page object model
├── tests/
│   ├── test_demo.py              # API tests (pytest + requests + Allure)
│   └── test_ui_pom.py            # UI tests (Playwright + POM + DDT + Allure)
├── data/                         # test data files
├── requirements.txt              # Python dependencies
└── README.md                     # project documentation
```

## Test Framework

| Type | Tools | Description |
|------|-------|-------------|
| API Testing | pytest + requests | Call GitHub API to verify response |
| UI Testing | Playwright + POM | Page Object Model, test the-internet site |
| Data-Driven | DDT (pytest.mark.parametrize) | Run same test with multiple data sets |
| Reporting | Allure | Structured HTML test report |

## CI/CD Pipeline

Using GitHub Actions. Triggered on every `git push`:

1. Checkout code
2. Setup Python 3.12
3. Install dependencies (`pip install -r requirements.txt`)
4. Install Playwright browser (`playwright install chromium`)
5. Run all tests (`pytest --alluredir=allure-results`)
6. Upload Allure report

## Local Run

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ --verbose --alluredir=allure-results
```
