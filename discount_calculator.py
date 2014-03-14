class DiscountCalculator(object):
    
    def calculate(self, total, discount_amount, discount_type):
        if discount_type == 'percent':
            if discount_amount > 100:
                raise ValueError("Discount amount has to be less than 100 percent")
            percentage_discount = float(discount_amount) / 100
            discount = float(total) * percentage_discount            
        elif discount_type == 'dollar':
            if discount_amount > total:
                raise ValueError("Discount amount has to be larger than the price of the item")
            discount = discount_amount   
        else:
            raise ValueError("Invalid discount type")           
        return discount
        
    
        
    