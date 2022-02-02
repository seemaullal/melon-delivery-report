def print_line_info(line_text):
    content = line.rstrip()
    words = content.split('|')

    melon, count, amount = words

    print(f"Delivered {count} {melon}s for total of ${amount}")

print("Day 1")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    print_line_info(line)
the_file.close()


print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    print_line_info(line)
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    print_line_info(line)
the_file.close()
