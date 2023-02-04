
# trebu-blacklist

This project contains the source code and instructions for my solution to the Trebu technical test.

Trebu-blacklist is a Python and Fast API application that implements a micro-service API with just two endpoints:

```curl
curl -X POST -H "Content-Type: application/json" -d '{"email": "someemail@somesite.com", "reason": "Rude", "game_id": 435345}'  http://127.0.0.1:8000/blacklist/
```
```curl
curl /blacklist/check/someemail@somesite.com
```

The trebu-blacklist micro-API is currently deployed and ready to use at this URL: 

## AWS deployement and architecture

I'll describe here several details about the technical implementation:

- it uses a PostgresSQL database on RDS (Relational Database Service). While the database was exposed to the public provided a login and password during development, 
it now isn't, and only accepts connections through the VPC.

<p align="center">
<img src="https://user-images.githubusercontent.com/13710571/216707594-8d48c5fa-7e5c-42d4-8db6-0adc8e549afb.png" width="700" >
</p>

- this micro-API is a FastAPI over Python 3.9 application, and was published on the web as an AWS Lambda Function.
- on AWS, it uses a Secrets Manager to keep the RDS connection string secure on the cloud.

<p align="center">
<img src="https://user-images.githubusercontent.com/13710571/216703102-1d29a5d3-ced3-4814-a9d9-95fbc8e4a69a.png" width="700">
</p>

## Documentation and API unit tests:

OpenAPI and Swagger documentation are provided as an easy way to test the API endpoints.

<p align="center">
<img src="https://user-images.githubusercontent.com/13710571/216731168-c6b371a3-70fd-4d05-8abf-0413afbb4e70.png"  width="700">
</p>

- Swagger docs: (https://q1xl8mgi54.execute-api.us-east-1.amazonaws.com/redoc/)
- Open API docs: (https://q1xl8mgi54.execute-api.us-east-1.amazonaws.com/docs/)

## Network configuration

<p align="center">
<img src="https://user-images.githubusercontent.com/13710571/216705239-fc0f79ac-be82-47e7-a65f-c557f93b40bd.png"  width="500">
</p>

VPC rules were configured for a safe and segmented communication between the Lambda Function and its database on RDS.

<p align="center">
<img src="https://user-images.githubusercontent.com/13710571/216713041-ff705aba-c549-417a-8fb1-e4a6613abcba.png"  width="500">
</p>

However, the micro-service itself is exposed through AWS API Gateway.

## Local execution configuration

On Linux, Mac OS or WSL terminal, you may install the micro-service dependencies by running:

```sh
pyenv virtualenv blacklist       # Creates a 
pip install -r requirements.txt  # Install the depencies
```

And then run the service through the command:

```bash
export BLACKLIST_DATABASE_URL=postgresql+psycopg2://postgres:password@localhost/excluye  # Defines a local database connection URL.
uvicorn main:app --reload
```

You can then query the local service 
