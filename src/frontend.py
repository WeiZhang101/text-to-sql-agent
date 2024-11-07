import streamlit as st
from sql_db_agent import SQLDBAgent
from sql_agent.sql_agent_prompt import SQLAgentPrompt
import traceback

def initialize_agent():
    try:
        agent = SQLDBAgent()
        return agent.create_sql_db_agent()
    except Exception as e:
        st.error(f"初始化AI代理时出错: {str(e)}")
        st.code(traceback.format_exc())
        return None

def main():
    st.set_page_config(
        page_title="SQL查询助手",
        page_icon="🤖",
        layout="wide"
    )

    # 初始化 SQL agent
    if 'sql_agent' not in st.session_state:
        st.session_state.sql_agent = initialize_agent()
        
    if st.session_state.sql_agent is None:
        st.error("系统初始化失败，请检查配置和环境变量。")
        return

    st.title("🤖 SQL智能查询助手")
    
    # 添加说明文字
    st.markdown("""
    ### 使用说明
    1. 在下方输入框中输入您的问题
    2. AI助手会将您的问题转换为SQL查询
    3. 查询结果会以易读的方式展示
    """)

    # 创建两列布局
    col1, col2 = st.columns([2, 1])

    with col1:
        # 文本输入区域
        question = st.text_area(
            "请输入您的问题：",
            height=100,
            placeholder="例如：查询最近10条销售记录..."
        )

        # 查询按钮
        if st.button("开始查询", type="primary"):
            if question:
                with st.spinner('AI正在处理您的问题...'):
                    try:
                        # 获取提示词
                        prompt = SQLAgentPrompt()
                        formatted_question = (
                            prompt.get_agent_prefix() + 
                            question + 
                            prompt.get_format_instructions()
                        )
                        
                        # 调用SQL代理
                        res = st.session_state.sql_agent.invoke(formatted_question)
                        
                        # 显示结果
                        st.success("查询完成！")
                        st.markdown(res["output"])
                        
                        # 添加到历史记录
                        if 'history' not in st.session_state:
                            st.session_state.history = []
                        st.session_state.history.append(question)
                    except Exception as e:
                        st.error(f"查询出错: {str(e)}")
                        st.code(traceback.format_exc())
            else:
                st.warning("请输入查询问题！")

    with col2:
        # 添加使用示例
        st.markdown("""
        ### 示例问题
        - 查询重复的人
        - 统计各部门的员工数量
        - 查找销售额最高的产品
        """)

        # 添加查询历史记录
        if 'history' not in st.session_state:
            st.session_state.history = []

        st.markdown("### 历史查询")
        for item in st.session_state.history[-5:]:  # 只显示最近5条记录
            st.text(item)

if __name__ == "__main__":
    main() 