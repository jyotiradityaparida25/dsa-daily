class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        a=[]
        a.append(float(celsius)+273.15)
        a.append(float(celsius)*1.80+32.00)
        return a