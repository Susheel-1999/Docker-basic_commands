FROM python

RUN mkdir -p /home/app

COPY . /home/app.

# set default dir so that next commands executes in /home/app dir
WORKDIR /home/app

# Install the dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "ui.py"]