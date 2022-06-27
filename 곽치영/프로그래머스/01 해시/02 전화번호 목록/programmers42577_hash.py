def solution(phone_book):
    phone_numbers = set()
    prefix_numbers = set()
    
    for phone_number in phone_book:
        if phone_number in prefix_numbers:
            return False

        for i in range(1, len(phone_number)+1):
            prefix_number = phone_number[:i]
            
            if prefix_number in phone_numbers:
                return False

            prefix_numbers.add(prefix_number)

        phone_numbers.add(phone_number)
    
    return True
