# Dog Chase Simulation

## Overview
This Python script simulates a scenario where a police officer, a thief, and a dog are involved in a chase. The script calculates the total distance traveled by the dog before the thief is caught and breaks down the directional distances the dog covers.

## Problem Statement
Given the speeds of the police officer, thief, and dog, along with the initial distance between the police and the thief, the script determines:
- The total distance traveled by the dog before the thief is caught.
- The time taken for the police officer to catch the thief.
- The breakdown of the dog's movement in forward and backward directions.

## Formulae Used
1. **Time to catch the thief**
   \[ \text{time\_to\_catch} = \frac{\text{distance\_between\_them}}{\text{police\_speed} - \text{thief\_speed}} \]

2. **Total distance traveled by the dog**
   \[ \text{total\_distance\_by\_dog} = \text{dog\_speed} \times \text{time\_to\_catch} \]

3. **Directional Distances**
   - Forward ratio: \( \text{dog\_speed} - \text{police\_speed} \)
   - Backward ratio: \( \text{dog\_speed} + \text{police\_speed} \)
   - Total ratio: \( \text{forward\_ratio} + \text{backward\_ratio} \)
   - One per ratio: \( \frac{\text{total\_distance\_by\_dog}}{\text{total\_ratio}} \)
   - Forward distance: \( \text{one\_per\_ratio} \times \text{backward\_ratio} \)
   - Backward distance: \( \text{one\_per\_ratio} \times \text{forward\_ratio} \)

## Code Explanation
The script consists of two main functions:

### 1. `total_distance(police_speed, thief_speed, dog_speed)`
- Calculates the time required for the police officer to catch the thief.
- Determines the total distance traveled by the dog in that time.

### 2. `dirctional_distance(police_speed, dog_speed, total_distance_by_dog)`
- Computes how much distance the dog covers in forward and backward directions.

## Usage
The script initializes the following parameters:
```python
police_speed = 20  # m/s
thief_speed = 12   # m/s
dog_speed = 30     # m/s
distance_between_them = 5000  # meters
```
Then, it calculates:
```python
total_distance_by_dog, time_to_catch = total_distance(police_speed, thief_speed, dog_speed)
forward_distance, backword_distance = dirctional_distance(police_speed, dog_speed, total_distance_by_dog)
```
Finally, it prints the results:
```python
print(f"Total distance covered by the dog: {total_distance_by_dog} meters, at time: {time_to_catch} sec")
print(f"Forward distance covered by the dog towards the thief: {forward_distance} meters, and backward distance is: {backword_distance} meters")
```

## Example Output
```
Total distance covered by the dog: 18750.0 meters, at time: 625.0 sec
Forward distance covered by the dog towards the thief: 15625.0 meters, and backward distance is: 3125.0 meters
```

## Notes
- The script assumes that the police officer is always faster than the thief.
- The dog continuously runs back and forth between the police officer and the thief.
- Variable names contain minor spelling errors (e.g., `dirctional_distance` should be `directional_distance`, `backword_distance` should be `backward_distance`). Consider renaming them for better readability.

## License
This project is open-source and available for modification and distribution.

---

This README provides a clear and structured explanation of the script, making it professional and easy to understand. 🚀

