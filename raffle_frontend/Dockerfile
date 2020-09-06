# official node.js runtime for Docker
FROM node:12
# Create and set the directory for this container
RUN mkdir -p /app
WORKDIR /app
# Install Application dependencies
<<<<<<< HEAD
COPY package.json /app/frontend/
RUN npm install
# RUN npm install -g react-scripts axios
# RUN yarn global add react-scripts
=======
COPY package.json /app
RUN yarn install
>>>>>>> 485392cbfa7095e870363cee85e8cc1f7832e29a
# Copy over the rest of the project
COPY . /app

# Set the default port for the container
EXPOSE 3000
ENV CI=true

CMD ["npm", "start"]