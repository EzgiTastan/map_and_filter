#Question: You work on a payroll program.
#Question: Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
#Question: Output the resulting list.
# salaries = [2000, 1800, 3100, 4400, 1500]
#bonus = int(input())

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

new_salaries = list(map(lambda x: x + bonus, salaries))
print(new_salaries)