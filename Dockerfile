
FROM mongo:latest

# Set environment variables 
# ENV MONGO_INITDB_ROOT_USERNAME=mongo
# ENV MONGO_INITDB_ROOT_PASSWORD=2020go

# Expose the default MongoDB port
EXPOSE 27017

# Command to run MongoDB
CMD ["mongod", "--quiet"]
