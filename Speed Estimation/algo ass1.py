def total_distance(police_speed,thief_speed,dog_speed):
    
    relative_speed = police_speed - thief_speed  #8 m/s


    time_to_catch = distance_between_them / relative_speed  #625 seconds

    
    total_distance_by_dog = dog_speed * time_to_catch  #18750 meters

    return total_distance_by_dog,time_to_catch

def dirctional_distance(police_speed,dog_speed,total_distance_by_dog):
   
    forward_ratio= dog_speed - police_speed # 10 
    backword_ratio= dog_speed + police_speed # 50
    total_ratio = forward_ratio + backword_ratio # 60
    one_per_ratio = total_distance_by_dog / total_ratio # 312.5
    forward_distance = one_per_ratio * backword_ratio  # 15625 meter
    backword_distance = one_per_ratio * forward_ratio  # 3125 meter

    return forward_distance,backword_distance

  

police_speed = 20  # m/s
thief_speed = 12   # m/s
dog_speed = 30     # m/s
distance_between_them = 5000  # meters

total_distance_by_dog,time_to_catch = total_distance(police_speed,thief_speed,dog_speed)
forward_distance,backword_distance = dirctional_distance(police_speed,dog_speed,total_distance_by_dog)

print(f"Total distance covered by the dog: {total_distance_by_dog} meters, at time: {time_to_catch} sec")
print(f"forward distance covered by the dog towards the thife is: {forward_distance} meters,and backword distance is: {backword_distance} meters")

