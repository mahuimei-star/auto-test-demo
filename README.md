# Auto Test Demo

> 自动化测试 Demo 项目，集成 CI/CD 流水线，用于展示接口测试和 UI 自动化测试能力。
> A demo project for automated testing with CI/CD pipeline, showcasing API testing and UI automation.

## Project Structure / 项目结构

```
auto-test-demo/
├── .github/workflows/test.yml    # CI/CD pipeline config / CI/CD 流水线配置
├── pages/
│   └── demo_page.py              # POM: page object model / 页面对象封装
├── tests/
│   ├── test_demo.py              # API tests (pytest + requests + Allure) / 接口测试
│   └── test_ui_pom.py            # UI tests (Playwright + POM + DDT + Allure) / UI 测试
├── data/                         # test data files / 测试数据文件
├── requirements.txt              # Python dependencies / Python 依赖
└── README.md                     # project documentation / 项目说明
```

## Test Framework / 测试框架

| Type / 类型 | Tools / 工具 | Description / 说明 |
|------------|------------|------------------|
| API Testing / 接口测试 | pytest + requests | Call GitHub API to verify response / 调用 GitHub API 验证返回 |
| UI Testing / UI 测试 | Playwright + POM | Page Object Model, test the-internet site / 页面对象模式 |
| Data-Driven / 数据驱动 | DDT (pytest.mark.parametrize) | Run same test with multiple data sets / 多组数据运行同一用例 |
| Reporting / 测试报告 | Allure | Structured HTML test report / 结构化测试报告 |

## CI/CD Pipeline / CI/CD 流水线

Using GitHub Actions. Triggered on every `git push`:
> 使用 GitHub Actions，每次 `git push` 自动执行：

1. Checkout code / 拉取代码
2. Setup Python 3.12 / 安装 Python 3.12
3. Install dependencies / 安装依赖 (`pip install -r requirements.txt`)
4. Install Playwright browser / 安装 Playwright 浏览器 (`playwright install chromium`)
5. Run all tests / 运行所有测试 (`pytest --alluredir=allure-results`)
6. Upload Allure report / 上传 Allure 测试报告

## Local Run / 本地运行

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ --verbose --alluredir=allure-results
```