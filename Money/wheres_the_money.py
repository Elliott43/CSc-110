def main():
    title()
    financial_report = FinancialReport()
    
    # the __call__ function makes it so that your objects are callable (object(*args) is the same as object.__call__(*args))
    financial_report()
    

def title():
    print("""-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------""")

# I know this isn't necessary, but it was the neatest way to do this (in the main function)
class FinancialReport:
    def __init__(self):
        # Considered grouping assignment and input validation, but I think this is more readable
        salary = input("What is your annual salary?\n")
        self.salary = FinancialReport._input_validation(salary, "salary")

        monthly_housing_expences = input("How much is your monthly mortgage or rent?\n")
        self.monthly_housing_expenses = FinancialReport._input_validation(monthly_housing_expences, "mortgage or rent")
        self.monthly_housing_expenses *= 12 # nolonger monthly...

        monthly_bills = input("What do you spend on bills monthly?\n")
        self.monthly_bills = FinancialReport._input_validation(monthly_bills, "bills")
        self.monthly_bills *= 12 # nolonger monthly...

        weekly_grocery_expences = input("What are your weekly grocery/food expenses?\n")
        self.weekly_grocery_expences = FinancialReport._input_validation(weekly_grocery_expences, "food")
        self.weekly_grocery_expences *= 52 # nolonger weekly...

        travel_expences = input("How much do you spend on travel annually?\n")
        self.travel_expences = FinancialReport._input_validation(travel_expences, "travel")

        tax_percentage = self.get_tax_percentage()
        self.income_tax = self.salary * ( tax_percentage / 100.0)
        self.income_tax = self.income_tax if self.income_tax <= 75000 else 75000

        print()


    # I think using __call__ instead of something like __str__ or print_financial_reoprt is bad style
    # I am doing this mostly just to learn how __call__ works
    def __call__(self):
        header = "See the financial breakdown below, based on a salary of $" + str(self.salary)
        lengths = [len(header)]

        names = [FinancialReport._format_name(name) 
                for name in ("mortgage/rent", "bills", "food", "travel", "tax", "extra")]
        
        amounts = [
            self.monthly_housing_expenses, 
            self.monthly_bills, self.weekly_grocery_expences, 
            self.travel_expences, 
            self.income_tax]
        
        extra = self.salary - sum(amounts)
        amounts.append(extra)

        report = ""
        for name, amount in zip(names, amounts):
            # I chose to enforce keyword arguments, because if you mix these up, it breaks
            # It's a lot easier to fix the bug this way, if you do mix them up
            # I really only did this because I spent a lot of time trying to figure out why this didn't work
            # When all that really went wrong was that I switched the parameters
            # a syntax error will now show up if you don't use keyword arguments
            segment = self.get_report_segment(amount=amount, name=name)
            lengths.append(len(segment))

            report += segment
            report += "\n"
        
        # The assignment seperates the header and the report with a barrier made of '-'
        # The characters should extend as far as the longest part of the report
        barrier = "-" * max(lengths)

        print(barrier)
        print(header)
        print(barrier)
        print(report, end="")
        print(barrier)
        print(">>> WARNING: DEFICIT <<<") if extra < 0 else "do nothing"
        print(">>> TAX LIMIT REACHED <<<") if self.income_tax == 75000 else "do nothing"

    # self not used because input validation is only used inside the function, but not directly related
    # private meathod (theoretically)
    def _input_validation(user_input: str, category: str):
        if not user_input.isnumeric():
            print(f"Must enter positive integer for", category + ".")
            exit()

        return int(user_input)

    def _format_name(name):
        return f"{' ' * (14-len(name))}{name} "

    # segment of the full report (does the formatting here)
    def get_report_segment(self, *, amount, name):
        # := is an operater that assigns variables within expressions. it is sometimes called the walrus operator 🥺
        return f"|{name}| ${format(amount, '11,.2f')} | {format( round(percent := ((amount/self.salary) * 100), 1), '5')}% | {'#'*(int(percent))}"
        
    
    # Based on values given in assignment
    def get_tax_percentage(self):
        if self.salary <= 15000:
            return 10

        elif self.salary <= 75000:
            return 20

        elif self.salary < 200000:
            return 25

        else:
            return 30

# main contains the code that is run
main()