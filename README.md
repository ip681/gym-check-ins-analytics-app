# Gym check ins Analytics app

<font color="red" size="6">I'M STILL WORKING ON IT</font>

## 🏋🏽‍♀️ Gym Check-ins and User Metadata

### About Dataset

Dataset Summary: Gym Check-ins and User Metadata
This synthetic dataset represents gym check-ins and user metadata, split across four CSV files. It simulates gym activity across 10 different locations, featuring user details, gym attributes, and check-in history. The dataset now also includes information about different subscription plans.

Data Description
Users Data
This file contains detailed information about users who visit the gyms.

user_id: Unique identifier for each user.
first_name: First name of the user.
last_name: Last name of the user.
age: Age of the user.
gender: Gender of the user (Male, Female, Non-binary).
birthdate: Date of birth of the user.
sign_up_date: Date when the user signed up for the gym membership.
user_location: City where the user lives.
subscription_plan: The user's gym subscription plan (Basic, Pro, Student).
Gym Locations Data
This file describes the gyms and their locations.

gym_id: Unique identifier for each gym.
location: Real-world city where the gym is located (e.g., New York, Los Angeles).
gym_type: The type of gym (Premium, Standard, Budget).
facilities: List of facilities available at the gym (e.g., Swimming Pool, Sauna, Yoga Classes).
Check-in/Checkout History
This file tracks user check-ins and check-outs at the gyms.

user_id: ID of the user who checked in.

gym_id: ID of the gym where the check-in occurred.

checkin_time: Timestamp of when the user checked in.

checkout_time: Timestamp of when the user checked out.

workout_type: Type of workout performed during the visit (e.g., Cardio, Weightlifting, Yoga).

calories_burned: Estimated number of calories burned during the workout.

Subscription Plans
This file provides a description of the different subscription plans available to gym members.

subscription_plan: The name of the subscription plan (Basic, Pro, Student).

price_per_month: Price per month in Dollar

Dataset from:
https://www.kaggle.com/datasets/mexwell/gym-check-ins-and-user-metadata/code