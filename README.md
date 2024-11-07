# Text-to-SQL Agent

一个基于 LangChain 和 Gemini 的智能 SQL 查询助手，可以将自然语言转换为 SQL 查询语句并执行。

## 功能特点

- 自然语言转 SQL 查询
- 基于 Gemini-1.5-pro 大语言模型
- 支持 SQLite 数据库
- Web UI 界面（基于 Streamlit）
- 智能查询限制和结果优化
- 详细的查询解释

## 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone https://github.com/yourusername/text-to-sql-agent.git
cd text-to-sql-agent

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量
创建 `.env` 文件并添加以下内容：
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. 准备数据
1. 将您的CSV数据文件放在 `./data` 目录下
2. 默认支持的数据文件名为：`GITS_Delivery_Hub_resource_management-Resource_management.csv`
3. 运行数据库初始化脚本：
```bash
python src/db_init.py
```

### 4. 启动应用
```bash
streamlit run src/sql_db_agent.py
```

### 5. 使用示例
1. 访问 http://localhost:8501
2. 在输入框中输入自然语言查询，例如：
   - "查询所有员工的数量"
   - "显示部门分布情况"
3. 点击 "Run Query" 按钮
4. 系统会返回：
   - SQL 查询语句
   - 查询结果
   - 结果说明

## 项目结构

```
text-to-sql-agent/
├── src/
│   ├── sql_db_agent.py    # 主应用程序
│   └── db_init.py         # 数据库初始化脚本
├── data/                  # 数据文件目录
├── db/                    # SQLite 数据库文件
└── requirements.txt       # 项目依赖
```

## 技术栈

- Python 3.7+
- LangChain
- Google Gemini 1.5 Pro
- Streamlit
- SQLite
- Pandas
- SQLAlchemy

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。