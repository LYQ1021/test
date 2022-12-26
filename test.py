import streamlit as st
from PIL import Image
st.header(" :blue[_音樂播放器_]:coffee:")
year_list={'2022','2021','2020','2019','2018'}
option_year=st.sidebar.selectbox("選擇年度",year_list)

if option_year=='2022':
           type_list={'抒情歌曲':{'嘉賓','千千萬萬','靜悄悄','多想在平庸的世界擁抱你','專屬天使'},
                      '流行歌曲':{'孤勇者','親愛的對象','為你寫下這首情歌','從前說','如果可以'},
                      '饒舌歌曲':{'像他一樣','能火','Too much','NFT','除了說唱我什麼都不會'}}
if option_year=='2021':
           type_list={'抒情歌曲':{'錯位時空','不如','白月光與硃砂痣','熱愛一百零五度的你','TA'},
                      '流行歌曲':{'我不會讓你一個人','光年之外','演員','聽見下雨的聲音','魔鬼中的天使'},
                      '饒舌歌曲':{'畢竟都','赤子','小石頭','嘻哈菩薩','妹妹'}}
if option_year=='2020':
           type_list={'抒情歌曲':{'想見妳','句號','太陽','怎麼了','dance monkey'},
                      '流行歌曲':{'你的答案','少年','失眠飛行','靜悄悄','夏天的風'},
                      '饒舌歌曲':{'CHANGE','差不多姑娘','Whitout you','最後一次','Why you ganna lie'}}
if option_year=='2019':
           type_list={'抒情歌曲':{'小幸運','光年之外','漂向北方','告白氣球','雨蝶'},
                      '流行歌曲':{'那些你很冒險的夢','浪子回頭','浪流連','長途夜車','年少有為'}}
if option_year=='2018':
           type_list={'抒情歌曲':{'那些年','愛你','淋雨一直走','安靜','暖暖'},
                      '流行歌曲':{'告白氣球','是什麼讓我遇見這樣的你','寂寞寂寞就好','還是要幸福','等一個人'}}
                      
option_musiclist=st.sidebar.selectbox("選擇類型",type_list)  
option_music=st.selectbox("選擇音樂",type_list[option_musiclist])

 
       
audio_file = open('音樂'+'/'+option_year+'/'+option_music+'.mp3', "rb")
st.audio(audio_file.read())
st.snow()
