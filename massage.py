# استيراد الوحدات المطلوبة
import requests 
import json

# تحديد المتغيرات اللازمة
url = "https://www.fast2sms.com/dev/bulk"
my_data = { 
	# معرف المرسل الافتراضي الخاص بك 
	'sender_id': 'FSTSMS', 
	
	# ضع رسالتك هنا! 
	'message': 'هذه رسالة اختبار', 
	
	'language': 'english', 
	'route': 'p', 
	
	# يمكنك إرسال رسائل قصيرة إلى أرقام متعددة 
	# مفصولة بفاصلة. 
	'numbers': '9999999999, 7777777777, 6666666666'	
} 

# إنشاء الرأس
headers = { 
	'authorization': 'YOUR API KEY HERE', 
	'Content-Type': "application/x-www-form-urlencoded", 
	'Cache-Control': "no-cache"
}

# إرسال الطلب
response = requests.request("POST", 
							url, 
							data = my_data, 
							headers = headers) 

# تحليل الرد
returned_msg = json.loads(response.text) 

# طباعة الرسالة المرسلة
print(returned_msg['message'])