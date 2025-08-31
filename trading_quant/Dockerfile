FROM python:3.11-slim

WORKDIR /app

# 시스템 패키지 업데이트
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY app/ .

# 포트 노출
EXPOSE 8001

# 앱 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
