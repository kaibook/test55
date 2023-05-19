import streamlit as st

st.title("飲酒ペースメーカー")
st.write("ウィドマーク法を使用し、飲酒のペースを「ゆっくり」「ほろ酔い」「少し早い」「早い」「警告」「危険」の6つに分類しました。")
st.write("※これはあくまで目安です。体質や健康状態により個人差が生じます。")

x1 = st.number_input("ビール小ジョッキ(杯)",0,100,0)
y1 = st.number_input("ビール中ジョッキ(杯)",0,100,0)
z1 = st.number_input("ビール大ジョッキ(杯)",0,100,0)

x2 = st.number_input("ハイボール小ジョッキ(杯)",0,100,0)
y2 = st.number_input("ハイボール中ジョッキ(杯)",0,100,0)
z2 = st.number_input("ハイボール大ジョッキ(杯)",0,100,0)

x3 = st.number_input("サワー小ジョッキ(杯)",0,100,0)
y3 = st.number_input("サワー中ジョッキ(杯)",0,100,0)
z3 = st.number_input("サワー大ジョッキ(杯)",0,100,0)

x4 = st.number_input("日本酒(合)",0,100,0)

x5 = st.number_input("焼酎(杯)",0,100,0)

time = st.number_input("経過時間",0,100,0)
weight = st.number_input("体重(kg)",0,100,60)

al1 = x1*200+y1*350+z1*700
al2 = x2*200+y2*350+z2*700
al3 = x3*200+y3*350+z3*700
al = 0.792*(al1*0.05+al2*0.07+al3*0.03+x4*27+x5*18.75)

alc = al/(weight*0.96)
nalc = alc-(0.19*time)

result = ""
if nalc <= 0.04:
    result = "ゆっくり"
elif (0.04 < nalc <= 0.10):
    result = "ほろ酔い"
elif (0.10 < nalc <= 0.15):
    result = "少し早い"
elif (0.15 < nalc <= 0.30):
    result = "早い！"
elif (0.30 < nalc <= 0.40):
    result = "警告!!"
elif  0.40 < nalc:
    result = "危険!!!"

st.write("血中アルコール濃度:", nalc)
st.write("判定：", result)

