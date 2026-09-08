class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        fuel_used = 0
        while mainTank >= 5:
            mainTank -= 5
            fuel_used += 5
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        fuel_used += mainTank  
        return fuel_used * 10
