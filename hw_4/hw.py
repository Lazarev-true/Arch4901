class Ticket:
    def __init__(self, ticket_id, departure_zone, arrival_zone, route_number, departure_time, arrival_time, buyer_id, password_hash_code, account_id):
        self.id = ticket_id
        self.departure_zone = departure_zone
        self.arrival_zone = arrival_zone
        self.route_number = route_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.buyer_id = buyer_id
        self.password_hash_code = password_hash_code
        self.account_id = account_id
        self.is_used = False

    def set_is_used(self, is_used):
        self.is_used = is_used

    def get_is_used(self):
        return self.is_used

    def get_departure_zone(self):
        return self.departure_zone

    def get_arrival_zone(self):
        return self.arrival_zone

    def get_route_number(self):
        return self.route_number

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time
    
    
class User:
    def __init__(self, user_id, name, login, is_used, price, place):
        self.id = user_id
        self.name = name
        self.login = login
        self.is_used = is_used
        self.price = price
        self.place = place
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def get_ticket_count(self):
        return len(self.tickets)

    def get_ticket_ids(self):
        return [ticket.id for ticket in self.tickets]
    

class Account:
    def __init__(self, user_account_id, balance):
        self.user_account_id = user_account_id
        self.balance = balance

    def get_user_account(self):
        return self.user_account_id

    def get_balance(self):
        return self.balance