class TimeAngle:
    @staticmethod
    def calculator(hours, minutes):
        if 24 >= hours > 13:
            hours /= 2
        elif hours == 12:
            hours == 0
        h_angle = 30*hours + minutes/2
        m_angle = minutes*6
        return (abs(h_angle - m_angle))

hours = int(input("Введите часы (от 0 до 24): "))
minutes = int(input("Введите минуты (от 0 до 59): "))
angle = TimeAngle().calculator(hours, minutes)

print(f"Угол равен {angle}")
