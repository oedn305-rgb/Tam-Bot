import os
import requests
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. إعدادات الوصول (سحب البيانات من Secrets)
SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = os.environ.get('BLOG_ID')
SERVICE_ACCOUNT_STR = os.environ.get('SERVICE_ACCOUNT_JSON')

def start_bot():
    try:
        # تحويل النص السري إلى قاموس JSON
        info = json.loads(SERVICE_ACCOUNT_STR)
        creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
        service = build('blogger', 'v3', credentials=creds)

        # محتوى تجريبي (يمكنك ربطه بـ OpenAI لاحقاً)
        title = "فرصة عقارية مميزة في الرياض - تم السعودية"
        content = "<h2>تفاصيل العرض</h2><p>فيلا فاخرة للبيع بمساحة 400 متر...</p>"

        body = {
            "kind": "blogger#post",
            "title": title,
            "content": content,
            "labels": ["عقارات", "الرياض"]
        }

        # النشر الفعلي
        post = service.posts().insert(blogId=BLOG_ID, body=body).execute()
        print(f"✅ تم النشر! الرابط: {post['url']}")

    except Exception as e:
        print(f"❌ فشل البوت بسبب: {e}")

if __name__ == "__main__":
    start_bot()
