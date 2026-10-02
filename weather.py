import requests

LATITUDE = 36.8151
LONGITUDE = 127.1139

WEATHER_CODES = {
0: "맑음",
1: "주로 맑음",
2: "약간 흐림",
3: "흐림"
}

url = (
"https://api.open-meteo.com/v1/forecast"
f"?latitude={LATITUDE}"
f"&longitude={LONGITUDE}"
"&hourly=temperature_2m,weather_code,relative_humidity_2m,"
"precipitation_probability,wind_speed_10m"
"&daily=temperature_2m_max,temperature_2m_min"
"&forecast_days=2"
"&timezone=Asia/Seoul"
)
response = requests.get(url)
data = response.json()
dates = data["daily"]["time"]
print("=" * 40)
print("🌤 천안 날씨 리포트")
print("=" * 40)

for day in range(2):
    if day == 0:
        print("\n📅 천안 오늘 날씨")
    else:
         print("\n📅 천안 내일 날씨")

    date = dates[day]

    for target_time in ["06:00", "15:00"]:
        
        for i, time_str in enumerate(data["hourly"]["time"]):
            
            if date in time_str and target_time in time_str:
                
                weather_code = data["hourly"]["weather_code"][i]
                weather = WEATHER_CODES.get(weather_code, "정보 없음")
                    
                temp = data["hourly"]["temperature_2m"][i]
                humidity = data["hourly"]["relative_humidity_2m"][i]
                rain = data["hourly"]["precipitation_probability"][i]
                wind = data["hourly"]["wind_speed_10m"][i]
                    
                if target_time == "06:00":
                    print("\n🌅 오전 06:00")
                else:
                    print("\n🌇 오후 15:00")
                    
                print(f"날씨 : {weather}")
                print(f"기온 : {temp}℃")
                print(f"강수확률 : {rain}%")
                print(f"습도 : {humidity}%")
                print(f"풍속 : {wind} m/s")
                    
                break
        
    print(
        f"\n🌡 일일 기온 : 최저 {data['daily']['temperature_2m_min'][day]}℃ "
        f"/ 최고 {data['daily']['temperature_2m_max'][day]}℃"
        )

    print("\n프로그램 종료")