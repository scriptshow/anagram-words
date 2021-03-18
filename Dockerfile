FROM python:3.7

# Environment variable
ENV ANAGRAM_DB_NAME 'DATABASE_NAME_HERE'
ENV ANAGRAM_DB_HOST 'DATABASE_HOST_HERE'
ENV ANAGRAM_DB_PORT 'DATABASE_PORT_HERE'
ENV ANAGRAM_DB_USER 'DATABASE_USERNAME_HERE'
ENV ANAGRAM_DB_PASS 'DATABASE_PASSWORD_HERE'

ENV ANAGRAM_LOG_LEVEL 'LOG_LEVEL'
ENV ANAGRAM_SECRET_KEY 'SECRET_KEY'

# change work directory
RUN mkdir -p /anagram-words
WORKDIR /anagram-words

ADD ./ /anagram-words/
RUN pip install -r requirements.txt

EXPOSE 5000

# Comment this line once tests done
ENTRYPOINT ["./gunicorn_starter.sh"]
