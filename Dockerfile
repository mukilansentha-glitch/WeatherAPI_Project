FROM python:latest
WORKDIR app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
Expose 5000
CMD ["python","main.py"] 
