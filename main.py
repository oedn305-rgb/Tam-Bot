import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# إعداد الصلاحيات
SCOPES = ['https://www.googleapis.com/auth/blogger']
# حط محتوى ملف الـ JSON اللي حملته في الـ Secrets بجيتهاب باسم SERVICE_ACCOUNT_JSON
service_account_info = eval(os.environ.get('SERVICE_ACCOUNT_JSON'))

creds = service_account.Credentials.from_service_account_info(
    service_account_info, scopes=SCOPES)

service = build('blogger', 'v3', credentials=creds)

def create_post(blog_id, title, content):
    body = {
        "kind": "blogger#post",
        "title": title,
        "content": content,
        "labels": ["سيارات", "تم_السعودية"] # تقدر تخليها متغيرة
    }
    try:
        posts = service.posts().insert(blogId=blog_id, body=body).execute()
        print(f"✅ تم النشر بنجاح! الرابط: {posts['url']}")
    except Exception as e:
        print(f"❌ خطأ في فئة Blogger V3: {e}")

# شغل الدالة ببياناتك
create_post('ID_مدونتك', 'إعلان جديد من تم السعودية', '<p>محتوى الإعلان هنا</p>')
