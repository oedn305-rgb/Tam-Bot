name: Tam Bot Engine

on:
  schedule:
    - cron: '*/30 * * * *'  # يعمل كل 30 دقيقة بالضبط
  workflow_dispatch:        # يتيح لك تشغيله يدوياً وقت ما تحب

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install requests

      - name: Run Tam Bot
        env:
          API_KEY: ${{ secrets.API_KEY }}
          BLOG_ID: ${{ secrets.BLOG_ID }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python main.py
