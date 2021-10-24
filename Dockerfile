FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/TheOksigen/neonuserbot /root/neonuserbot
WORKDIR /root/neonuserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
