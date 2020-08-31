# official node.js runtime for Docker
FROM node:12
# Create and set the directory for this container
RUN mkdir -p /app/frontend/
WORKDIR /app/frontend/
# Install Application dependencies
COPY package.json /app/frontend/
RUN yarn install
# Copy over the rest of the project
COPY . /app/frontend/

# Set the default port for the container
EXPOSE 3000

CMD yarn start