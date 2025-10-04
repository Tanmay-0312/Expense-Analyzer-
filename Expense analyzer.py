from math import ceil

import matplotlib.pyplot as plt

def totalsav(a,b,c,d):
    x= a-(b+c)
    y = [x*month for month in range(1,d+1)]
    return(y)

def dicpri(d):
    print(f"{'Expenses':<20} {'Money':<10}")
    print("-" * 30)

    for e, f in d.items():
        print(f"{e:<20} {f:<10}")
    return d


def diccomp(a,b):
    total_savings = a - b
    if a >0:
        percentage = (total_savings / income) * 100
    else:
        percentage = 0
    if a ==b:
        print("There is no Savings!\n Net savings",total_savings)
        print("A total of",(percentage),"%")

    elif a> b:
        print("You can save a lot!\n Net savings",total_savings)
        print("A total of", (percentage), "%")
    else:
        print("You need to Spend less!\n Net savings",total_savings)
        print("A total of", (percentage), "%")

    labels = ["Income","Expenses"]
    values = [a,b]
    plt.bar(labels,values,color=["green","red"])
    plt.title("Income vs Expenses")
    plt.ylabel("Amount")
    plt.show()
    show_expense_pie(Expenses)


def show_expense_pie(expenses_dict):
    if not expenses_dict:
        print("No expenses to show in pie chart.")
        return

    labels = list(expenses_dict.keys())  # Categories
    sizes = list(expenses_dict.values())  # Amounts

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Expenses Distribution by Category")
    plt.show()




x = input("Enter your monthly income: ")
try:
    income = int(x)
except ValueError:
    print("Invalid!")
    income = 0

Expenses = {}
while True:
    Expenses_Type = input("Ok so How do you spend your salary?(To finish typing expenses write 'Finished' or if you want to see your total expendeture type Total): ").lower().strip()
    if Expenses_Type == "finished":
        print("OK")
        break
    if Expenses_Type == "total":
        dicpri(Expenses)
        continue

    z = input("Please do tell the amount: ")

    try:
        Expenses_Money = int(z)
    except ValueError:
        print("Not a correct value!")
        continue

    Expenses[Expenses_Type] = Expenses_Money

a = sum(Expenses.values())
diccomp(income,a)

max_exp = max(Expenses,key=Expenses.get)
print(f"{max_exp} is the category where you spend most!")

min_exp = min(Expenses,key=Expenses.get)
print(f"{min_exp} is the category where you spend least!")


print(f"Ok so now let me ask you which of the following are your essential expenses? ")
dicpri(Expenses)
Essential_Exp = []
while True:
    b = input("Enter the number of essential expenses: ")
    try:
        no_of_EE = int(b)
        for i in range(no_of_EE):
            Essential_Expendetures = input("Ok so can u start listing them?: ").lower().strip()
            if Essential_Expendetures in Expenses:
                Essential_Exp.append(Essential_Expendetures)
                print("Ok")
            else:
                print("Expense not found")
        break
    except ValueError:
        print("Not a Valid entry")

next_month_essentialexp = sum(Expenses[category] for category in Essential_Exp)
print("So your minimum spending next month is: ", next_month_essentialexp)

next_month_nonessentialexp = sum(
    Expenses[category] for category in Expenses if category not in Essential_Exp
)
print("So your non-essential spending next month is: ", next_month_nonessentialexp)

labels = ["Essential","Non Essential"]
values = [next_month_essentialexp,next_month_nonessentialexp]
plt.bar(labels,values,color=["green","red"])
plt.title("Essential expenses vs non Essential Expenses")
plt.ylabel("Amount")
plt.show()

foresight = input("Now would you like to see how much will you save if you keep spending this way?(y/n): ").lower().strip()
if foresight == "y":
    t = input("For how many months would you like to see the foresight?")
    try:
        no_foresight = int(t)
    except ValueError:
        print("Invalid Value")
else:
    print("Ok")

print(f"You will save {(income-(next_month_essentialexp+next_month_nonessentialexp))*no_foresight} in {no_foresight} months")

line_data = totalsav(income,next_month_essentialexp,next_month_nonessentialexp,no_foresight)
print(line_data)

months = list(range(1, no_foresight+1))
plt.plot(months, line_data, marker='o', color='blue')
plt.title(f"Savings Projection for {no_foresight} Months")
plt.xlabel("Months")
plt.ylabel("Total Savings")
plt.grid(True)
plt.show()

if line_data[-1] <= 0:
    plt.plot(months, line_data, marker='o', color='blue')
    plt.title(f"Overexpense Projection for {no_foresight} Months")
    plt.xlabel("Months")
    plt.ylabel("Total Expendeture")
    plt.grid(True)
    plt.show()

inc_sav = input("Do you want to see of you reduce non essential expenses how much will you save?(y/n)?: ")
if inc_sav == "y":
    p = input("Enter the percentage which you want to see(for eg. if u want to see 20% write 0.2): ")

    try:
        sav_perc = float(p)
        new_savings = next_month_nonessentialexp * (1-sav_perc)
        new_exp_and_savings = totalsav(income,next_month_essentialexp,new_savings,no_foresight)


    except ValueError:
        print("Invalid Value")

plt.plot(months, line_data, marker='o', color='red', label="Current Savings")
plt.plot(months, new_exp_and_savings, marker='o', color='green', label="With New Cut")
plt.title(f"What-If Savings Projection for {no_foresight} Months")
plt.xlabel("Months")
plt.ylabel("Total Savings")
plt.legend()
plt.grid(True)
plt.show()

ques1 = input("Do you have a savings goal?(y/n): ")
if ques1 == "y":
    ques2 = input("Enter your savings goal: ")
    try:
        saving_goal = int(ques2)
        total_proj_savings = (income - (next_month_essentialexp + next_month_nonessentialexp)) * no_foresight
        if total_proj_savings >= saving_goal:
            print(f"Congratulations! Your goal of {saving_goal} is achievable. Projected savings: {total_proj_savings}")
        else:
            diff = saving_goal - total_proj_savings
            print(
                f"You need to save an additional {diff} to reach your goal. Consider reducing non-essential expenses.")

    except:
        print("invalid")

plt.plot(months, line_data, label="Projected Savings")
plt.plot(months, [saving_goal/no_foresight * m for m in months], label="Savings Goal")
plt.legend()
plt.show()

monthly_savings = income - (next_month_essentialexp + next_month_nonessentialexp)
months_needed = ceil(saving_goal / monthly_savings)
print(f"With your current spending, you will reach your savings goal in {months_needed} months.")



















