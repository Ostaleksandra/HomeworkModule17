per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Ведите сумму вклада "))
deposit = []
for key in per_cent:
    deposit.append(round(per_cent[key] * money / 100))
max_deposit = round(max(deposit))
print(deposit)
print("Максимальная сумма, которую вы можете заработать - " + str(max_deposit))