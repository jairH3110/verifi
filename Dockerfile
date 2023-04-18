FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /halo
WORKDIR /halo
COPY requirements.txt /halo/
RUN pip install -r requirements.txt
COPY . /halo/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8000
