import streamlit as st
import time

#ターミナル　streamlit run main.py

st.title('Streamlit 超入門')

st.write('ブログレスパーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右のカラム')
if button:
    right_column.write('ここはカラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# option = st.sidebar.selectbox(
#     'あなたが好きな数字を教えてください,',
#     list(range(1, 11))
# )
# condistionn = st.sidebar.slider('あなたの今の調子は？', 0, 10, 5)

# 'あなたの趣味:', text, 'です。'
# 'あなたの好きな数字は、', option, 'です。'
# 'コンディション：', condistionn
# if st.checkbox('Asakura Image'):
#     img = Image.open('IMG_6453.jpg')
#     st.image(img, caption='Asakura Ryouya', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

#write()は表の細かい設定はできない
#dataframe()は表の縦横の長さを指定できる width=100, height=100
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))

#shift + @ = ```
# """
# # 章
# ## 節
# ### 項

# ``` python  
# import streamlit as st
# import numpy as nu
# import pandas as pd

# ```

# """

