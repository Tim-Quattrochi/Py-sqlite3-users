from advanced_user_operations import *
import uuid

test_uuid = uuid.uuid4()


# Initialize AdvancedUserOperations instance
advanced_user_ops = create_user_with_profile
# Test creating a new user with profile information

print("Creating a new user...")

result_create = advanced_user_ops(test_uuid,
                                  'joker', 'joker@joker.com', 'test123', 60, 'Male', '123 Owl St')

print("User creation result:", result_create)


# Test retrieving users based on specified criteria
print("\nRetrieving users...")
users = retrieve_users_by_criteria(
    min_age=25, max_age=40, gender='Male')
print("Retrieved users:", users)


# Test updating user profile information
print("\nUpdating user profile...")
result_update = update_user_profile(
    'john.doe@example.com', age=35, address='456 Oak St')
print("User profile update result:", result_update)

# Test deleting users based on specified criteria
print("\nDeleting users...")

result_delete = delete_users_by_criteria('Female')

print("User deletion result:", result_delete)
