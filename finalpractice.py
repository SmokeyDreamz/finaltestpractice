class ThemeParkPass:
    def __init__(self, guest_name, pass_type, rides_used, ride_limit, is_valid):
        self.guest_name = guest_name
        self.pass_type = pass_type
        self.rides_used = rides_used
        self.ride_limit = ride_limit
        self.is_valid = is_valid


    def can_ride(ride_name, self):
        if self.is_valid is "Not Valid" or self.rides_used >= self.ride_limit:
            return False
        else:
            self.rides_used.append(ride_name)
            return True
    can_ride("Scary_Coaster", "Bartholemew")
        
guest = ThemeParkPass("Bartholemew", "Premium", [1], 5, "Not Valid")
