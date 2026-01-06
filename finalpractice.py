class ThemeParkPass:
    def __init__(self, guest_name, pass_type, rides_used, ride_limit, is_valid):
        self.guest_name = guest_name
        self.pass_type = pass_type
        self.rides_used = rides_used
        self.ride_limit = ride_limit
        self.is_valid = is_valid

    def can_ride(self, ride_name):
        if not self.is_valid or len(self.rides_used) >= self.ride_limit:
            return False
        else:
            self.rides_used.append(ride_name)
            return True


guest = ThemeParkPass("Bartholemew", "Premium", [], 5, True)


print(guest.can_ride("Scary_Coaster"))
print(guest.rides_used)
