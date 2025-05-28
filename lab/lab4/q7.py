friend1_wishlist = {'book', 'headphones', 'chocolate', 'game'}
friend2_wishlist = {'chocolate', 'game', 'watch', 'backpack'}

# 1. Items both friends want
common_items = friend1_wishlist & friend2_wishlist

# 2. Items only friend1 wants
unique_to_friend1 = friend1_wishlist - friend2_wishlist

# 3. All unique wishlist items
all_items = friend1_wishlist | friend2_wishlist

print("Common items:", common_items)
print("Unique to friend1:", unique_to_friend1)
print("All unique items:", all_items)
