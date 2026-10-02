import requests
LATITUDE = 36.8151
LONGITUDE = 127.1139
url = (
"https://api.open-meteo.com/v1/forecast"
f"?latitude={LATITUDE}"
f"&longitude={LONGITUDE}"
"&current=temperature_2m"
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
print("날씨 코드 등록 완료")