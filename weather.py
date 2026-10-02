import requests
LATITUDE = 36.8151
LONGITUDE = 127.1139
url = (
"https://api.open-meteo.com/v1/forecast"
f"?latitude={LATITUDE}"
f"&longitude={LONGITUDE}"
"&current=temperature_2m,weather_code"
"&daily=weather_code,temperature_2m_max,temperature_2m_min"
"&forecast_days=2"
"&timezone=Asia/Seoul"
)
response = requests.get(url)
data = response.json()
print("천안 현재 기온")
print(f"{data['current']['temperature_2m']}℃")
WEATHER_CODES = {
0: "맑음",
1: "대체로 맑음",
2: "약간 흐림",
3: "흐림"
}
weather_code = data["current"]["weather_code"]
weather = WEATHER_CODES.get(
weather_code,
"정보 없음"
)
print("=" * 40)
print("🌤 천안 날씨 리포트")
print("=" * 40)
print("\n📅 오늘")
print(f"날씨 : {weather}")
print(f"기온 : {data['current']['temperature_2m']}℃")
tomorrow_code = data["daily"]["weather_code"][1]
tomorrow_weather = WEATHER_CODES.get(
tomorrow_code,
"정보 없음"
)
print("\n📅 내일")
print(f"날씨 : {tomorrow_weather}")
print(f"최저 기온 : {data['daily']['temperature_2m_min'][1]}℃")
print(f"최고 기온 : {data['daily']['temperature_2m_max'][1]}℃")
print("\n프로그램 종료")
