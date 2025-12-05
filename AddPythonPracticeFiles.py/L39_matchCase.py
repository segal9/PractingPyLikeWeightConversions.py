# also known as a switch - An alternative to using many elif statements
# execute some code if a value matches a 'case'
# benefits: cleaner and synatax is more readable.
'''
def dayOfWeek(day):
    match day:

        case 1:
            return "It is Sunday!"
        case 2:
            return "It is Monday!"
        case 3:
            return "Its is Tuesday!"
        case 4:
            return "It is Wednesday!"
        case 5:
            return "It is Thursday!"
        case 6:
            return "It is Friday!"
        case 7:
            return "It is Saturday!"
        case _:
            return "Not a valid day!"
        
print(dayOfWeek("pizza"))
'''
# example 1 displayed how it is simplier than using else - if statements
def isWeekend(day):
    match day:

        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(isWeekend("Pizza"))