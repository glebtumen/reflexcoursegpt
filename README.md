# ReflexCourseGPT 🎓

_AI-powered academic writing assistant for Russian students_

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.7.0-purple.svg)](https://reflex.dev)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com)
[![Supabase](https://img.shields.io/badge/Supabase-Auth-orange.svg)](https://supabase.com)

## 📖 Описание / Description

**ReflexCourseGPT** — это веб-приложение на базе искусственного интеллекта, которое помогает студентам генерировать академические работы (курсовые, дипломные, рефераты) за считанные минуты. Приложение использует передовые модели ИИ для создания качественного контента с поиском источников в интернете.

**ReflexCourseGPT** is an AI-powered web application that helps students generate academic coursework (term papers, theses, essays) in minutes. The application uses advanced AI models to create quality content with internet source research.

## ✨ Основные возможности / Key Features

- 🤖 **AI-генерация контента** с использованием GPT-4o-mini и Perplexity AI
- 📄 **Экспорт в Word** для удобного редактирования
- 🔍 **Поиск академических источников** через cyberleninka.ru
- ⚙️ **Настройка креативности** и детальности текста
- 📊 **Генерация таблиц** в JSON формате
- 👥 **Система подписок** с еженедельной оплатой
- 🔐 **Полная аутентификация** через Supabase
- 📱 **Адаптивный дизайн** для мобильных и десктопных устройств
- 🚀 **До 100 курсовых в неделю** для премиум-пользователей

## 🛠 Технологический стек / Tech Stack

### Frontend & Backend

- **[Reflex](https://reflex.dev)** - Python-based full-stack framework
- **Python 3.10+** - Core programming language

### AI & APIs

- **OpenAI GPT-4o-mini** - Primary content generation
- **Perplexity AI** - Academic source research
- **OpenRouter** - API routing for multiple models

### Database & Authentication

- **Supabase** - Database and authentication
- **JWT** - Token-based authentication

### Deployment

- **Docker** - Containerization
- **Nginx** - Reverse proxy and static file serving
- **Poetry** - Dependency management

## 📁 Структура проекта / Project Structure

```
reflexcoursegpt/
├── reflex_coursegpt/           # Основной код приложения
│   ├── __init__.py
│   ├── reflex_coursegpt.py     # Главный файл приложения
│   ├── base_state.py           # Базовое состояние
│   ├── auth/                   # Модуль аутентификации
│   │   ├── auth_supabase.py    # Supabase интеграция
│   │   ├── login.py            # Страница входа
│   │   ├── registration.py     # Страница регистрации
│   │   └── reset_password.py   # Сброс пароля
│   ├── landing_page/           # Лендинг страница
│   │   ├── landing_page.py     # Основная лендинг страница
│   │   ├── navbar.py           # Навигационная панель
│   │   ├── main_content.py     # Основной контент
│   │   ├── faq.py              # FAQ секция
│   │   └── footer.py           # Подвал
│   └── main_page/              # Основное приложение
│       ├── dashboard.py        # Панель управления
│       ├── dashboard_state.py  # Состояние дашборда
│       ├── subscription.py     # Страница подписки
│       └── dashboard_components/ # Компоненты дашборда
├── assets/                     # Статические файлы
├── Dockerfile                  # Docker конфигурация
├── docker-compose.yml          # Docker Compose
├── nginx.conf                  # Nginx конфигурация
├── pyproject.toml              # Poetry конфигурация
└── requirements.txt            # Python зависимости
```

## 💡 Использование / Usage

### Основные функции / Main Features

1. **Регистрация и вход** - Создайте аккаунт или войдите в существующий
2. **Выбор подписки** - Оформите подписку для доступа к премиум функциям
3. **Генерация контента** - Используйте различные режимы для создания академических работ
4. **Настройка параметров** - Регулируйте креативность и детальность текста
5. **Экспорт результатов** - Скачивайте готовые работы в формате Word

### API Endpoints

- `/` - Лендинг страница
- `/login` - Страница входа
- `/registration` - Страница регистрации
- `/dashboard` - Основная панель управления
- `/subscription` - Страница подписки

## 🔗 Полезные ссылки / Useful Links

- [Reflex Documentation](https://reflex.dev/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Supabase Documentation](https://supabase.com/docs)
- [Docker Documentation](https://docs.docker.com)

**Сделано с ❤️ для студентов**
