FROM python:3.12

RUN apt-get update && \
    apt-get install -y locales git procps
RUN locale-gen ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP
ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo
WORKDIR /python_programming

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python"]