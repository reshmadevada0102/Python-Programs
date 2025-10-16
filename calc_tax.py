'''WAP to calculate the tax'''
def calc_tax():
    tax = 0
    salary = int(input("Enter the salary:"))
    if salary > 0 and salary <= 10000:
        tax = tax + (salary * 0.1)
    elif salary <= 20000:
        tax = tax + 1000 + ((salary - 10000) * 0.2)
    else: 
        tax = tax + 3000 + ((salary -20000) * 0.3)
    print(f"Salary: ${salary}, Tax: ${tax}")
if __name__ == "__main__":
    calc_tax()