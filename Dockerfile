FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#WORKDIR /code
RUN apt -q -y update \
 && apt install -y --assume-yes  \
        python3-dev \
        build-essential \
        python3-pip \
        libgeos-dev \
        libboost-all-dev \
        cmake \
    && apt -q -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# копирование файла зависимостей в рабочую директорию
COPY . /code

# установка рабочей директории в контейнере
WORKDIR /code

RUN python3 -m pip install -r requirements.txt