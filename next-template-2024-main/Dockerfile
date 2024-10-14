# Use the Node.js image for development
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy only package.json and lock files to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Expose port 3000 for the Next.js server
EXPOSE 3000

# Start the Next.js app in development mode
CMD ["npm", "run", "dev"]
