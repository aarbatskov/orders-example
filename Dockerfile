FROM python:3.12-slim

WORKDIR /opt/app
RUN pip install uv

COPY ./src /opt/app/src

COPY requirements.lock pyproject.toml README.md /opt/app

RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

WORKDIR /opt/app/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
