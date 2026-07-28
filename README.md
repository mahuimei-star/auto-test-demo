# Auto Test Demo

自动化测试 Demo 项目，集成 CI/CD 流水线，用于展示接口测试和 UI 自动化测试能力。

## 项目结构

```
auto-test-demo/
├── .github/workflows/test.yml    # CI/CD 流水线配置
├── pages/
│   └── demo_page.py              # POM：页面对象封装
├── tests/
│   ├── test_demo.py               # 接口测试（pytest + requests + Allure）
│   └── test_ui_pom.py             # UI测试（Playwright + POM + DDT + Allure）
├── data/                          # 测试数据文件
├── requirements.txt               # Python 依赖
└── README.md                      # 项目说明
```

## 测试框架

| 测试类型 | 工具 | 说明 |
|---------|------|------|
| 接口测试 | pytest + requests | 调用 GitHub API 验证返回 |
| UI测试 | Playwright + POM | 页面对象模式，测试 the-internet 页面 |
| 数据驱动 | DDT (pytest.mark.parametrize) | 多组数据运行同一用例 |
| 测试报告 | Allure | 结构化 HTML 测试报告 |

## CI/CD 流水线

使用 GitHub Actions，每次 `git push` 自动执行：

1. 拉取代码
2. 安装 Python 3.12
3. 安装依赖（pip install -r requirements.txt）
4. 安装 Playwright 浏览器（playwright install chromium）
5. 运行所有测试（pytest --alluredir=allure-results）
6. 上传 Allure 测试报告

## 本地运行

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ --verbose --alluredir=allure-results
```