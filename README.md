# Auto Test Demo

一个集成 CI/CD 的自动化测试演示项目，覆盖 API 接口测试 与 UI 自动化测试，展示了测试框架的核心设计能力。

## 设计亮点

- POM 分层设计：将页面元素与测试逻辑解耦，页面变更只改 Page 层，测试用例不受影响，大幅降低维护成本
- DDT 数据驱动：通过 pytest.mark.parametrize 一份用例多组数据复用，用例编写效率提升，覆盖更全面
- API + UI 双层覆盖：接口层验证数据逻辑，UI 层验证用户交互，形成完整质量防线
- Allure 报告：结构化测试报告，失败用例自动截图与堆栈，便于问题定位
- CI/CD 自动化：GitHub Actions 每次 push 自动执行全部用例并生成报告，测试结果实时可见

## Project Structure

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

## Test Framework

| Type | Tools | Description |
|------|-------|-------------|
| API Testing | pytest + requests | Call GitHub API to verify response |
| UI Testing | Playwright + POM | Page Object Model, test the-internet site |
| Data-Driven | DDT (pytest.mark.parametrize) | Run same test with multiple data sets |
| Reporting | Allure | Structured HTML test report |

## CI/CD Pipeline

Using GitHub Actions. Triggered on every git push:

1. Checkout code
2. Setup Python 3.12
3. Install dependencies (pip install -r requirements.txt)
4. Install Playwright browser (playwright install chromium)
5. Run all tests (pytest --alluredir=allure-results)
6. Upload Allure report

## Local Run

pip install -r requirements.txt
playwright install chromium
pytest tests/ --verbose --alluredir=allure-results

## Contact

如果对我的自动化测试实践经验感兴趣，欢迎交流。
