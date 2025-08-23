# Stage 1: Builder and AS builder just means are naming the stage so we can call it later

FROM python:3.8-slim AS builder

# Make working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install packages into /install
RUN pip install --prefix=/install -r requirements.txt




# stage 2 
FROM python:3.8-slim

# Copy installed packages from builder
COPY --from=builder /install /install

# Tell Python where to find the installed packages
ENV PYTHONPATH=/install/lib/python3.8/site-packages

# Copy app code into image's working directory
COPY app.py .

#run app
CMD ["python", "app.py"]