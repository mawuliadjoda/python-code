name = ('Paulo', 'James')
name[0] = 'Mawuli'  # This will raise an error because tuples are immutable
for name in name:
    print(f"Hello there {name} this is Goood!")