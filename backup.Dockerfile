FROM python:3.12-slim

WORKDIR /code

COPY . . 

RUN pip install --upgrade pip
RUN pip install poetry poetry-plugin-export
RUN poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install "uvicorn[standard]"
RUN cat ./requirements.txt
RUN chmod +x entrypoint.sh

# Expose the port that FastAPI will run on
EXPOSE 8000


ENTRYPOINT ["./entrypoint.sh"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]