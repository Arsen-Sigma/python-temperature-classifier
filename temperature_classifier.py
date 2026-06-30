temperature = int(input("Введите температуру: "))
print(f"🌡 Температура: {temperature}°C")

if temperature < 0:
    print("❄️ Мороз ")
    print("🧣 Оденьтесь теплее!")
elif 0 <= temperature <= 15:
    print("🧥 Холодно")
    print("🧣 Оденьтесь теплее!")
elif 16 <= temperature <= 25:
    print("🌤️ Тепло")
    print("💧 Совет: возьмите воду.")
elif  26 <= temperature <= 35: 
    print("☀️ На улице жарко.")
    print("💧 Совет: возьмите воду.")
else:
    print("🔥 Очень жарко")
    print("💧 Совет: не выходите без необходимости и пейте больше воды.")
