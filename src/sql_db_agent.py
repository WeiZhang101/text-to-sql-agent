from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from sql_agent.sql_agent_config import SQLAgentConfig
from sql_agent.sql_agent_prompt import SQLAgentPrompt

class SQLDBAgent:
    def __init__(self):
        self.config = SQLAgentConfig()
        self.prompt = SQLAgentPrompt()

    def create_sql_db_agent(self):
        try:
            database_file_path = "./db/test_1.db"
            db = SQLDatabase.from_uri(f"sqlite:///{database_file_path}")
            model = self.config.create_model()
            toolkit = SQLDatabaseToolkit(db=db, llm=model)

            return create_sql_agent(
                llm=model,
                toolkit=toolkit,
                top_k=30,
                verbose=True,
                prefix=self.prompt.get_agent_prefix(),
                format_instructions=self.prompt.get_format_instructions()
            )
        except Exception as e:
            print(f"创建SQL代理时出错: {str(e)}")
            raise e
