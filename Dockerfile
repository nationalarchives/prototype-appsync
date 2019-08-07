FROM python:2.7-alpine
WORKDIR graphql
COPY ./ .
RUN apk update && apk add zip build-base bash yarn openjdk8-jre && yarn 
CMD yarn offline
