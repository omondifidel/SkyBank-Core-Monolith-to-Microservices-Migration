FROM nginx:alpine

# Copy custom configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Set the working directory to where Nginx serves files
WORKDIR /usr/share/nginx/html

# Copy ALL frontend files (index, script, style) into the image
COPY . .

EXPOSE 80