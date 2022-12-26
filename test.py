import streamlit as st
from PIL import Image
st.header(" :blue[_音樂播放器_]:coffee:")
year_list={'2022','2021','2020','2019','2018'}
option_year=st.sidebar.selectbox("選擇年度",year_list)

if option_year=='2022':
           type_list={'抒情歌曲':{'交換餘生'},
                      '流行歌曲':{'如果可以','過客','天黑黑'},
                      '搖滾歌曲':{'一直走','癢癢'},
                      '饒舌歌曲':{'mei mei','Married To The Game','I Wish I Was There'},
                      '民謠歌曲':{'parent love songs','可不可以放進去一下下就好','黃輔軍魂','大安高工校歌','歌'}}
if option_year=='2021':
           type_list={'抒情歌曲':{'慢冷','在這座城市遺失了你'},
                      '流行歌曲':{'我很好騙','唯一想了解的人'},
                      '搖滾歌曲':{'媽遙控器在哪','抱一抱一下','祖克柏是蜥蜴人'},
                      '饒舌歌曲':{'伯父'},
                      '民謠歌曲':{'國歌','我有一支槍'}}
if option_year=='2020':
           type_list={'抒情歌曲':{'最後一堂課','告白氣球','想見你想見你想見你'},
                      '流行歌曲':{'眼淚記得你','外人'},
                      '搖滾歌曲':{'規則就是用來打破的','派對動物'},
                      '饒舌歌曲':{'WAIT','她沒在看我','dont worry about me'}}
if option_year=='2019':
           type_list={'抒情歌曲':{'你的婚禮','你的婚禮'},
                      '流行歌曲':{'我們好好的','可不可以放進去一下下就好'},
                      '搖滾歌曲':{'致青春'},
                      '饒舌歌曲':{'something i dont need '},
                      '民謠歌曲':{'健康操'}}
if option_year=='2018':
           type_list={'抒情歌曲':{'天外之物','披星戴月的想你'},
                      '流行歌曲':{'親愛的對象'},
                      '搖滾歌曲':{'你要不要吃哈密瓜','馬子狗'},
                      '饒舌歌曲':{'少年董','辣台妹'},
                      '民謠歌曲':{'黃埔軍校'}}           

option_musiclist=st.sidebar.selectbox("選擇類型",type_list)  
option_music=st.selectbox("選擇音樂",type_list[option_musiclist])

 
       
audio_file = open('音樂'+'/'+option_year+'/'+option_music+'.mp3', "rb")
st.audio(audio_file.read())
st.snow()
