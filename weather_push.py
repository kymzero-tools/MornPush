import requests
import os
import sys
from urllib.parse import quote

# 从环境变量读取配置
AMAP_KEY = os.getenv('AMAP_KEY')
PUSHDEER_KEY = os.getenv('PUSHDEER_KEY')
CITY = os.getenv('CITY', 'hangzhou')  # 默认杭州

if not AMAP_KEY or not PUSHDEER_KEY:
    print("❌ 缺少必要的环境变量 AMAP_KEY 或 PUSHDEER_KEY")
    sys.exit(1)

def get_weather():
    """调用高德天气API获取实时天气"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": AMAP_KEY,
        "city": CITY,
        "extensions": "base",  # base=实时天气
        "output": "json"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("status") == "1" and data.get("lives"):
            live = data["lives"][0]
            return {
                "city": live.get("city", "未知"),
                "weather": live.get("weather", "未知"),
                "temperature": live.get("temperature", "未知"),
                "winddirection": live.get("winddirection", "未知"),
                "windpower": live.get("windpower", "未知"),
                "humidity": live.get("humidity", "未知"),
                "reporttime": live.get("reporttime", "未知")
            }
        else:
            print(f"❌ 高德API返回错误: {data.get('info', '未知错误')}")
            return None
    except Exception as e:
        print(f"❌ 请求高德API失败: {e}")
        return None

def push_notification(weather):
    """通过PushDeer推送天气信息"""
    url = "https://api2.pushdeer.com/message/push"

    # 构造推送内容（支持Markdown格式）
    text = f"🌤️ {weather['city']} 今日天气"
    desp = f"""
### {weather['city']} · {weather['reporttime']}

- **天气**：{weather['weather']}
- **温度**：{weather['temperature']}°C
- **风向**：{weather['winddirection']} {weather['windpower']}
- **湿度**：{weather['humidity']}%

> 祝你有美好的一天！☀️
"""

    params = {
        "pushkey": PUSHDEER_KEY,
        "text": text,
        "desp": desp,
        "type": "markdown"
    }

    try:
        response = requests.post(url, data=params, timeout=10)
        result = response.json()
        if result.get("code") == 0:
            print("✅ 推送成功！")
        else:
            print(f"❌ 推送失败: {result}")
    except Exception as e:
        print(f"❌ 推送请求失败: {e}")

if __name__ == "__main__":
    print("🔄 开始获取天气信息...")
    weather = get_weather()

    if weather:
        print(f"📊 获取到天气: {weather}")
        print("📤 开始推送...")
        push_notification(weather)
    else:
        print("❌ 获取天气失败，终止推送")
        sys.exit(1)