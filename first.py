import streamlit as st
import pandas as pd
st.title('🕶学生-李华-数字档案')
st.header('🔑 基础信息')
st.markdown('***学生ID：***:green[23051170248]')
st.markdown('***注册时间：***:green[2023-09-01 08:30:17] ***| 精神状态：✅正常***')
st.markdown('***当前教室：***:green[实训楼301] ***| 安全等级：***:green[绝密 ]')
     
st.header('📊  技能矩阵')

c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="95%", delta="2%")
c2.metric(label="Python", value="87%", delta="-1%")
c3.metric(label="Java", value="68%", delta="-10%")
st.header('Streamlit课程进度')
st.progress(value=30,text='Streamlit课程进度')

data = {
'日期':['2023-10-1','2023-10-5','2023-10-12'],
'任务':['学生数字档案','课程管理系统', '数据图表展示'],
'状态':['✅完成','🕒 进行中','❌未完成'],
'难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆']}

index = pd.Series(['0','1','2'], name='')
df = pd.DataFrame(data, index=index)

st.subheader('📝 任务日志')

st.dataframe(df)

st.subheader('🔐 最新代码成果')
st.code('''
public class Hello {
    public static void main(String[] args) {
        System.out.println("你好！ Streamlit!");
    }
}
''')

st.markdown(':green[>>SYSTEM MESSAGE:]***下一个任务目标已解锁...***')
st.markdown(':green[>>TARGET:]***课程管理系统***')
st.markdown(':green[>>COUNTDOWN:]***2025-06-03 15:24:58***')
st.markdown('系统状态：在线  连接状态：已加密')