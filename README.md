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

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
## Windows
venv\Scripts\activate
## macOS/Linux
source venv/bin/activate

# 安装依赖
pip3 install -r requirements.txt

# 如果遇到依赖安装问题，可以尝试更新 pip
pip3 install --upgrade pip
```

### 2. 配置环境变量
创建 `.env` 文件并添加以下内容：
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. 准备数据
1. 将您的CSV数据文件放在 `./data` 目录下
2. 默认支持的数据文件名为：`xxx_xxx.csv`
3. 运行数据库初始化脚本：
```bash
python3 src/db_init.py
```

### 4. 启动应用
```bash
streamlit run src/frontend.py
```

### 5. 使用示例
1. 访问 http://localhost:8501
2. 在输入框中输入自然语言查询，例如：
   - "查询所有员工的数量"
   - "显示部门分布情况"
3. 点击 "开始查询" 按钮
4. 系统会返回：
   - SQL 查询语句
   - 查询结果
   - 结果说明

## 项目结构

```
text-to-sql-agent/
├── src/
│   ├── frontend.py        # 前端界面
│   ├── sql_db_agent.py    # 后端逻辑
│   └── db_init.py         # 数据库初始化脚本
├── data/                  # 数据文件目录
├── db/                    # SQLite 数据库文件
├── venv/                  # Python虚拟环境
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

## 常见问题

1. 虚拟环境相关
   - 如果 `venv` 命令不可用，请先安装：`pip3 install virtualenv`
   - 要退出虚拟环境，使用命令：`deactivate`
   - 删除虚拟环境：删除 `venv` 目录即可

2. 依赖安装问题
   - 如果安装依赖时出错，可以尝试：`pip3 install -r requirements.txt --upgrade`
   - 对于 M1/M2 Mac 用户，某些包可能需要特殊处理，请参考具体包的文档

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。