@echo off
cd /d D:\weather_report
call .venv\Scripts\activate
python manage.py fetch_weather
python manage.py send_daily_reports
