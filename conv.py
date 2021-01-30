import streamlit as st
import time
import re
#ターミナル　streamlit run main.py

st.title('変換アプリケーション')


# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i + 1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)


# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右のカラム')
# if button:
#     right_column.write('ここはカラム')
add_selectbox = st.sidebar.selectbox(
    "選択してください",
    ("カット", "溶接")
)

sentence_from = st.text_area("文字を入力してください", height=300)

def text_input_1(fro):
    texts = re.sub(r'[ ]+', '', fro )
    result = re.findall(r'[A-Z]=-?[0-9]{1,5}\.[0-9]{2}|LWPOLYLINE|面積|長さ',texts)
    'G90'
    'F2.5'
    'V36'
    'G11 L29;'
    'M08'
    'M24'
    'G00 X'+result[0][2:]+'0 Y'+result[1][2:]+'0 Z'+result[2][2:]+'0;'
    'M22'
    'G04 T100;'
    'M07'

    result_list = list(result)


    for i in range(int(len(result_list)/3)):
        if result_list[i*3]=='LWPOLYLINE':
            z = re.sub('=', '',result_list[i*3+3])
            y = re.sub('=', '',result_list[i*3+4])
            x = re.sub('=', '',result_list[i*3+5])
            'M08'
            'M24'
            'G00 ' + [z][0] +' '+ [y][0] +' '+ [x][0] + ';'
            'M22'
            'G04 T100;'
            'M07'
        else:
            q = re.sub('=', '',result_list[i*3])
            w = re.sub('=', '',result_list[i*3+1])
            e = re.sub('=', '',result_list[i*3+2])
            'G01 '+ [q][0] +' '+ [w][0] +' '+ [e][0] + ';'

    'M08'
    'M24'
    'G00 X 0.000 Y 0.000 Z 0.000;'
    'G00 X 0.000 Y 0.000 Z 0.000;'
    'M02'


def text_input_2(fro):
    texts = re.sub(r'[ ]+', '', fro )
    result = re.findall(r'[A-Z]=-?[0-9]{1,5}\.[0-9]{2}|LWPOLYLINE|面積|長さ',texts)
    'G90'
    'F11.5'
    'M05'
    'G11 L2;'
    'G00 X'+result[0][2:]+'0 Y'+result[1][2:]+'0 Z'+result[2][2:]+'0;'
    'M22'
    'G04 T100;'
    'M07'
    'G04 T300;'
    'M60'

    result_list = list(result)


    for i in range(int(len(result_list)/3)):
        if result_list[i*3]=='LWPOLYLINE':
            z = re.sub('=', '',result_list[i*3+3])
            y = re.sub('=', '',result_list[i*3+4])
            x = re.sub('=', '',result_list[i*3+5])
            'M08'
            'M24'
            'G00 ' + [z][0] +' '+ [y][0] +' '+ [x][0] + ';'
            'M22'
            'G04 T100;'
            'M07'
        else:
            q = re.sub('=', '',result_list[i*3])
            w = re.sub('=', '',result_list[i*3+1])
            e = re.sub('=', '',result_list[i*3+2])
            'G01 '+ [q][0] +' '+ [w][0] +' '+ [e][0] + ';'
    'M64'
    'M08'
    'G04 T100;'
    'M24'
    'G00 X 0.000 Y 0.000 Z 0.000;'
    'G00 X 0.000 Y 0.000 Z 0.000;'
    'M02'

    

button = st.button('変換')

if add_selectbox == "溶接":
    if button:
        writeer = text_input_1(sentence_from)
        try:
            writeer
        except IndexError:
            st.write("違う")
            
elif add_selectbox == "カット":
    if button:
        writeer = text_input_2(sentence_from)
        try:
            writeer
        except IndexError:
            st.write("違う")





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
# texts = re.sub(r'[ ]+', '', text )
# 'あなたの趣味:', texts, 'です。'
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

