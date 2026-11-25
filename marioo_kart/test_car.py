# Kart-Engine v2.3

from model.car import Car

car = Car(7, 1)

# Test 1 : application du boost
car.speed = 6.0
car.apply_boost()

assert car.speed == 9.0
print("Test 1 : Boost valide")

# Test 2 : acceleration apres un boost
car.accelerate()

assert car.speed == 9.0
print("Test 2 : Conservation du boost validee")

# Test 3 : boost en marche arriere
car.speed = -2.0
car.apply_boost()

assert car.speed == -2.0
print("Test 3 : Marche arriere validee")

# Test 4 : reinitialisation
car.speed = 5.0
car.vx = 3.0
car.vy = 4.0

car.reset_position(200, 300, 90)

assert car.x == 200
assert car.y == 300
assert car.angle == 90
assert car.speed == 0.0
assert car.vx == 0.0
assert car.vy == 0.0

print("Test 4 : Reinitialisation validee")

print("Tous les tests sont valides !")