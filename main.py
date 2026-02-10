import os
import requests
import random

def safe_tam_bot():
    openai_key = os.getenv('OPENAI_API_KEY')
    api_key = os.getenv('API_KEY')
    blog_id = os.getenv('BLOG_ID')

    sectors = ["السيارات المستعملة", "العقارات السكنية", "الجوالات والأجهزة", "الخدمات المنزلية"]
    target = random.choice(sectors)

    prompt = (
        f"اكتب مقالاً حصرياً لمدونة 'تم السعودية' عن {target}. ركز على نصائح البيع والشراء "
        "وأهم العروض في حراج ومستعمل. استخدم تنسيق HTML بفقرات واضحة."
    )

    headers = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        content = response.json()['choices'][0]['message']['content']
        
        url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/?key={api_key}"
        payload = {"kind": "blogger#post", "title": f"دليل تم السعودية: {target}", "content": content.replace("\n", "<br>")}
        
        publish = requests.post(url, json=payload)
        if publish.status_code == 200:
            print(f"✅ نجاح! تم نشر مقال عن {target}")
        else:
            print(f"❌ خطأ بلوجر: {publish.text}")
    except Exception as e:
        print(f"❌ خطأ تقني: {e}")

if __name__ == "__main__":
    safe_tam_bot()
