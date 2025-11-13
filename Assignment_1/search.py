def linear_search (account_list,target_id):
	for i, acc_id in enumerate(account_list):
		if acc_id == target_id:
			return i # Return index if found
	return -1 # Not Found
	
def binary_search(account_list, target_id):
	low = 0
	high = len(account_list) -1
	
	while low <= high:
		mid = (low + high) // 2
		if account_list[mid] == target_id:
			return mid
		elif account_list[mid] < target_id:
			low = mid + 1
		else:
			high = mid - 1
	return -1
	
# Sample list of customer account IDs
account_ids = [105, 203, 307, 411, 509, 601, 712, 814]

# Input target ID

target = int(input("Enter the customer account ID to search: "))

# Linear Search
index_linear = linear_search(account_ids, target)
if index_linear != -1:
	print(f"Linear Search: Account ID {target} found at index {index_linear}.")
else:
	print("Linear Search: Account ID not found.")

#Binary Search (requires sorted list)
sorted_ids = sorted(account_ids) # endsure list is sorted
index_binary = binary_search(sorted_ids, target)
if index_binary != -1:
	print(f"Binary Search: Account ID {target} fount at index {index_binary} (sorted list).")
else:
	print("Binary Search: Account ID not found.")
