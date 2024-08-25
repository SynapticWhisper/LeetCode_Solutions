import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions: list[str] = []
        
        # Привести все дроби к общему знаменателю
        # вычислить сократить дроби
        # найти НОД числителя и знаменателя 
        # вывести результат

        tmp: str = ""
        for item in expression:
            if item in ("-", "+"):
                if tmp:
                    fractions.append(tmp)
                tmp = '' + item
            else:
                tmp += item
        else:
            fractions.append(tmp)
        
        values: dict[int, int] = {}
        total_denominator = 1

        for fraction in fractions:
            nominator, denominator = fraction.split("/")
            total_nominator: int = values.get(int(denominator), 0)
            if total_nominator == 0:
                total_denominator *= int(denominator)
            total_nominator += int(nominator)
            values[int(denominator)] = total_nominator
        
        result: int = 0
        for denominator, nominator in values.items():
            nominator *= total_denominator // denominator
            result += nominator
        
        g = math.gcd(result, total_denominator)

        return f"{result//g}/{total_denominator//g}"


print(Solution().fractionAddition("-1/2+1/2+1/3"))