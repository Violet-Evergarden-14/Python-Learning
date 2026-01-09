initial = [0, 0, 0]
final = [0, 0, 0]
sum_up = 0

for i in range(3):
    initial[i] = int(input())

for i in range(3):
    final[i] = int(input())

def judge_year_type(year):
    if year % 400 == 0:
        return 0
    elif year % 100 == 0:
        return 1
    elif year % 4 == 0:
        return 0
    else:
        return 1
    
def first_days_of_a_year(year, month, day):
    result = (month - 1) * 30 + day
    if month == 2:
        result += 1
    else:
        if judge_year_type(year) == 1:
            result -= 1
        match month:
            case 4, 5:
                result += 1
            case 6, 7:
                result += 2
            case 8:
                result += 3
            case 9, 10:
                result += 4
            case 11, 12:
                result += 5
    return result

for i in range(initial[0], final[0]):
    if judge_year_type(i) == 0:
        sum_up += 366
    else:
        sum_up += 365

sum_up = sum_up - first_days_of_a_year(initial[0], initial[1], initial[2]) + first_days_of_a_year(final[0], final[1], final[2])

print(sum_up)
