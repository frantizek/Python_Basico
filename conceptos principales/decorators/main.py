def sort_transactions(f):
    def wrapper(transactions):
        copy_of_transactions = transactions.copy()
        indexed = [(i, person, amount) for i, (person, amount) in enumerate(copy_of_transactions)]
        sorted_list = sorted(indexed, key=lambda x: (-x[2], x[0]))
        sorted_transactions = [(person, amount) for i, person, amount in sorted_list]
        return f(sorted_transactions)
    return wrapper

def combine_transactions(f):
    def wrapper(transactions):
        transaction_totals = {}
        for person, amount in transactions:
            if person in transaction_totals:
                transaction_totals[person] += amount
            else:
                transaction_totals[person] = amount
        aggregated_transactions = list(transaction_totals.items())
        return f(aggregated_transactions)
    return wrapper

def filter_transactions(threshold=50):
    def decorator(func):
        def wrapper(transactions):
            filtered_transactions = []
            for transaction in transactions:
                if transaction[1] < 0 or transaction[1] > threshold:
                    filtered_transactions.append(transaction)  
            func(filtered_transactions)
        return wrapper
    return decorator

@filter_transactions(threshold=50)
@combine_transactions
@sort_transactions
def display_total_transactions(transactions):
    for person, total_amount in transactions:
        amount_str = f" $ {total_amount}" if total_amount >= 0 else f"-$ {total_amount * -1}"
        print(f"{person} : {amount_str}")


def main() -> None:

    transactions = [
        ('Robin',50),
        ('Robin',0),
        ('Robin',-1),
        ('Alex', 100),
        ('Chris', 200),
        ('Alex', -25),
        ('Sam', 300), 
        ('Chris', 150),
        ('Alex', 75),
        ('Alex', 51), 
        ('Robin',20), 
        ('Xavier',70), 
        ('Yuri',70), 
        ('Zacek',70), 
    ]

    print(transactions)
    display_total_transactions(transactions)

if __name__ == '__main__':
    main()
