# String concatenation

# 99_bottles.py

for bottles in range(99, 0, -1):
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.")
    
    print()  # Add a newline for better readability

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")