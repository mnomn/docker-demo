FROM python:2.7-alpine3.8
COPY TODOApp /app

WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV FRIENDER_PORT 80
ENV BENDER_PORT 54321

CMD ["./run_todo.sh"]
