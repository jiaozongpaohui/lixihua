import numpy as np
import streamlit as st
import pandas as pd
import time
st.set_page_config(page_title='🥔南宁美食地图🥔')
st.header("🍲南宁美食地图🍲")
restaurants = pd.DataFrame({
"餐厅": ["星艺会塔斯汀", "麦当劳(华成都市店)", "好友缘(西大店)", "小放肆烤肉(西南商都店)", "李嬢拌粉(金花茶公园店)"],
"类型": ["西餐", "西餐", "自助餐", "自助餐", "自助餐"],
"评分": [4.2, 4.5, 4.0, 4.7, 4.3],
"人均消费(元)": [20, 30, 80, 50, 15],
"位置X": [22.853973,22.843103,22.834317,22.814946,22.821271],
"位置Y": [108.222505,108.267250,108.284567,108.321104,108.357652]
})
df=pd.DataFrame(restaurants)
df.index.name='编号'
st.dataframe(df[0:5])
st.map(pd.DataFrame({
"latitude":[22.853973,22.843103,22.834317,22.814946,22.821271],
"longitude":[108.222505,108.267250,108.284567,108.321104,108.357652]}))
st.header("💰不同类型餐厅价格")
data = {
'时间':['9','10','11','12','13','14','15','16','17','18','19','20'],
'月份':['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
'星艺荟塔斯汀':[50, 50, 80,20,45,60,20,44,32,11,47,32],
'麦当劳':[20, 60, 23,60,22,30,20,33,52,62,28,66],
'好友缘':[180, 150, 160,144,122,163,188,192,150,145,165,133],
'小放肆烤肉':[150,140,133,188,192,150,145,122,144,172,152,123],
'李嬢拌粉':[10,13,12,10,40,13,18,12,15,15,12,16]
}
df = pd.DataFrame(data)
index = pd.Series([0,1,2,3,4,5,6,7,8,9,10,11], name='序号')
df.index = index
st.line_chart(df,x='月份')


df= pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='序号')
df.index = index
st.header("🕣用餐高峰时段")
df.set_index('时间', inplace=True)
st.area_chart(df,y=["星艺荟塔斯汀", "麦当劳", "好友缘","小放肆烤肉", "李嬢拌粉"])

st.header("⭐餐厅评分")
st.bar_chart(restaurants,x='餐厅',y='评分')
st.header("🍽餐厅详情")
st.subheader('选择餐厅查看详情')
def my_format_func(option):
    return f'{option}店'
food = st.selectbox('选择餐厅：', ['星艺会塔斯汀', '麦当劳(华成都市店)', '好友缘(西大店)', '小放肆烤肉(西南商都店)', '李嬢拌粉(金花茶公园店)'], format_func=my_format_func, index=2)
if food == '星艺会塔斯汀':
    c1, c2 = st.columns(2)
    c1=st.subheader('星艺会塔斯汀')
    c2=st.markdown('''- 特色套餐
    - 香辣炸鸡
    - 薯条配可乐''')
    st.metric(label="评分", value="4.2/5.0")
    st.metric(label="人均消费", value="25元")
    st.subheader('当前拥挤程度')
    st.progress(value=40,text='40%拥挤')

elif food == '麦当劳(华成都市店)':
    st.subheader('麦当劳(华成都市店)')
    st.metric(label="评分", value="4.6/5.0")
    st.metric(label="人均消费", value="47元")
    st.subheader('当前拥挤程度')
    st.progress(value=55,text='55%拥挤')   

 
elif food == '好友缘(西大店)':
    st.subheader('好友缘(西大店)')
    st.metric(label="评分", value="4.6/5.0")
    st.metric(label="人均消费", value="80元")
    st.subheader('当前拥挤程度')
    st.progress(value=68,text='68%拥挤')  

 
elif food == '小放肆烤肉(西南商都店)':
    st.subheader('小放肆烤肉(西南商都店)')
    st.metric(label="评分", value="4.0/5.0")
    st.metric(label="人均消费", value="50元")
    st.subheader('当前拥挤程度')
    st.progress(value=60,text='60%拥挤') 
     
 
else:
    st.subheader('李嬢拌粉(金花茶公园店)')
    st.metric(label="评分", value="4.0/5.0")
    st.metric(label="人均消费", value="15元")
    st.subheader('当前拥挤程度')
    st.progress(value=32,text='32%拥挤')       



st.header("🎲今日午餐推荐")
if st.button('帮我选午餐'):
    lunch=st.selectbox(
               '你中午想吃什么？',
               ['今日推荐：星艺荟塔斯汀'],
               label_visibility='hidden')
    st.image('https://image.so.com/ai/large/view?end=60&id=18fa4e1e6093ae510835c4481e70427e&q=%E5%A1%94%E6%96%AF%E6%B1%80%E5%9B%BE%E7%89%87&tab=all&srcg=imglist_img')


