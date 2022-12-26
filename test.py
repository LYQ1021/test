import streamlit as st
from PIL import Image
st.header(" :blue[_音樂播放器_]:coffee:")
year_list={'2022','2021','2020','2019','2018'}
option_year=st.sidebar.selectbox("選擇年度",year_list)

#if option_year=='2022':
#           type_list={'抒情歌曲':{'2018流行1告白氣球'},
#                      '流行歌曲':{}}
#if option_year=='2021':
#           type_list={'抒情歌曲':,
#                      '流行歌曲':}
#if option_year=='2020':
#           type_list={'抒情歌曲':,
#                      '流行歌曲':}
if option_year=='2019':
           type_list={'抒情歌曲':{'小幸運','光年之外','漂向北方','告白氣球','雨蝶'},
                      '流行歌曲':{}
if option_year=='2018':
           type_list={'抒情歌曲':{'那些年','愛你','淋雨一直走','安靜','暖暖'},
                      '流行歌曲':{'告白氣球','是什麼讓我遇見這樣的你','寂寞寂寞就好','還是要幸福','等一個人'}
option_musiclist=st.sidebar.selectbox("選擇類型",type_list)  
option_music=st.selectbox("選擇音樂",type_list[option_musiclist])

 
       
audio_file = open('音樂'+'/'+option_year+'/'+option_music+'.mp3', "rb")
st.audio(audio_file.read())
st.snow()
