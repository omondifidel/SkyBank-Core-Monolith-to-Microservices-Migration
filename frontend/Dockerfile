FROM nginx:alpine

# 1. Copy config to the Nginx settings folder
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 2. Only copy the specific UI files to the web folder
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

EXPOSE 80