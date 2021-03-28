
FROM python:3.6-slim
COPY ./server.py /deploy/
COPY ./predictor.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./concrete_strength_trained_model.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "server.py"]