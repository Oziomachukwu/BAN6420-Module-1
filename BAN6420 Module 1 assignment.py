#BAN6420 Mosdule 1 assignment
import random

# Generating a list of workers dynamically
num_workers = 451
workers = []
for i in range(num_workers):
    worker = {
        'name': f'Staff_102{i+1}',
        'salary': random.randint(5000, 35000),  # Generating random salary between $5000 and $35000
        'gender': random.choice(['Male', 'Female'])
    }
    workers.append(worker)

# Function to generate payment slips
def generate_payment_slips(workers):
    payment_slips = []
    for worker in workers:
        try:
            slip = {
                'name': worker['name'],
                'salary': worker['salary'],
                'gender': worker['gender'],
                'employee_level': ''
            }
            if 10000 < worker['salary'] < 20000:
                slip['employee_level'] = 'A1'
            if 7500 < worker['salary'] < 30000 and worker['gender'] == 'Female':
                slip['employee_level'] = 'A5-F'
            payment_slips.append(slip)
        except KeyError as e:
            print(f"Missing key: {e}")
        except Exception as e:
            print(f"Error: {e}")
    return payment_slips

# Generate payment slips for all workers
payment_slips = generate_payment_slips(workers)
print(f"Generating Payslips...{len(payment_slips)} payment slips\n")
print("Done!\n")
# Print a few example payment slips
numpaymentslips = None
while type(numpaymentslips) != int or  numpaymentslips <= 0 or numpaymentslips > len(payment_slips) :
    try:
        numpaymentslips = int(input("How many payment slips do you want? "))  # Ask user how many payment slips they want
        if numpaymentslips > len(payment_slips) or numpaymentslips <= 0:
            raise Exception
    except Exception as e:
            print(f"Please enter a number between 0 and {len(payment_slips)}")
    except ValueError:
        print("Please enter a valid number.")
    else:
        for slip in payment_slips[:numpaymentslips]:
            print(slip)
