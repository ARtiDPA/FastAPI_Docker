FROM python
ADD . .
COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

CMD python main.py