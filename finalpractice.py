class ThemeParkPass:
    def __init__(self, guest_name, pass_type, rides_used, ride_limit, is_valid):
        self.guest_name = guest_name
        self.pass_type = pass_type
        self.rides_used = rides_used
        self.ride_limit = ride_limit
        self.is_valid = is_valid

    def can_ride(self, ride_name):
        if not self.is_valid or len(self.rides_used) > self.ride_limit:
            return False
        else:
            self.rides_used.append(ride_name)
            return True


def count_premium_passes(passes):
    count = 0
    for park_pass in passes:
        if park_pass.pass_type == "Premium" and park_pass.is_valid:
            count += 1
    return count



guest1 = ThemeParkPass("Justin", "Basic", ["Baby Coaster, Tall Coaster, Small Loop Coaster"], 1, True)
guest2 = ThemeParkPass("Max", "Premium", [], 1, True)
guest3 = ThemeParkPass("Bart", "Premium", [], 9, True)
guest4 = ThemeParkPass("Mart", "Basic", [], 4, False)
guest5 = ThemeParkPass("Justin", "Basic", [], 0, True)
guest6 = ThemeParkPass("Max", "Premium", [], 3, True)
guest7 = ThemeParkPass("Bart", "Premium", [], 4, True)
guest8 = ThemeParkPass("Mart", "Basic", [], 6, True)

passes = [guest1, guest2, guest3, guest4, guest5, guest6, guest7, guest8]



print(guest1.can_ride("Scary Coaster"))
print(guest1.rides_used)

print(count_premium_passes(passes))
