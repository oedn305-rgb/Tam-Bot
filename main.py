import os
import requests

def start_engine():
    # 1. جلب البيانات من الخزنة
    api_key = os.getenv('API_KEY')
    blog_id = os.getenv('BLOG_ID')
    
    print(f"--- التحقق من الإعدادات ---")
    if not api_key or not blog_id:
        print("❌ خطأ: المفاتيح ناقصة في Secrets!")
        return

    # 2. محاولة الاتصال بمدونتك
    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}"
    params = {'key': api_key}
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            blog_name = response.json().get('name')
            print(f"✅ نجاح باهر! البوت متصل الآن بمدونة: {blog_name}")
            print("--- البوت يعمل الآن في الخلفية لتحديث الروابط ---")
        else:
            print(f"❌ فشل الاتصال! كود الخطأ: {response.status_code}")
            print(f"السبب: {response.text}")
            
    except Exception as e:
        print(f"❌ خطأ غير متوقع: {e}")

if __name__ == "__main__":
    start_engine()
