# Используем официальный образ Node.js
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и устанавливаем зависимости
COPY package.json .
RUN npm install

# Копируем весь остальной код фронтенда
COPY . .

# Открываем порт и запускаем приложение
EXPOSE 3000
CMD ["npm", "start"]
