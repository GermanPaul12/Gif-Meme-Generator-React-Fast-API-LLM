# Dockerfile for React frontend using Vite
FROM node:18-slim

# Set environment variable for production
ENV NODE_ENV=production

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5167

# Start the Vite development server
CMD ["npm", "run", "dev"]
