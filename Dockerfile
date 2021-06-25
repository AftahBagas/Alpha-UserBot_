FROM ilhammansiz17/masteruserbot:MasterUserbot

RUN git clone https://github.com/AftahBagas/Alpha-Userbot_ /root/Alpha-Userbot_
WORKDIR /root/Alpha-Userbot_/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
