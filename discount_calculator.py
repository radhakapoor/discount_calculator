import sys


def discount_amount(total_amount, discount, discount_type):
    if discount_type == "percentage":
        discount_amount = total_amount * discount
        print discount_amount
    
    if discount_type == "dollar":
        discount_amount = total_amount - discount         
        print discount_amount 
 
    
def main():
    total_amount = float(sys.argv[1])
    discount = float(sys.argv[2])
    discount_type = sys.argv[3]
    discount_amount(total_amount, discount, discount_type)
    
    
if __name__ == '__main__':
    main()