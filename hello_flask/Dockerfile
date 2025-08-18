FROM python:3.8-slim

WORKDIR /app
COPY . .

# why: mysqlclient needs headers, pkg-config, and a compiler to build
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      gcc \
      pkg-config \
      default-libmysqlclient-dev \
      libmariadb3 \
 && pip install --no-cache-dir flask mysqlclient \
 && apt-get purge -y gcc pkg-config default-libmysqlclient-dev \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 5002
CMD ["python", "app.py"]
