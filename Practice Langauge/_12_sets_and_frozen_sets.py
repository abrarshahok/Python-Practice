# basket = {'orange','apple','mango','apple','mango'}
# print(basket)

# dup  = [1,2,3,4,5,6,1,2]
# s = set(dup)
# # Allow s.add()
# s.add(7)
# print(s)

# # Does not allow fs.add()
# fs = frozenset(dup)
# print(fs)

nums1 = {1,2,3,4,5,6}
nums2 = {4,5,6}

union = nums1 | nums2
intersection = nums1 & nums2
difference = nums1 - nums2

is_num1_subset_of_nums2 = nums1 < nums2
is_num2_subset_of_nums1 = nums2 < nums1

print(union)
print(intersection)
print(difference)
print(is_num1_subset_of_nums2)
print(is_num2_subset_of_nums1)