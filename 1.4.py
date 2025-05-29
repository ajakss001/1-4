from collections import Counter

def count_it(sequence):
    filtered_sequence = [int(item) for item in sequence if item.isdigit()]
    num_frequency = Counter(filtered_sequence)
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
    return dict(sorted_num_frequency[-3:])

print(count_it('222222222333'))
print(count_it('98765432109876543219987654321998765432199876543210'))
print(count_it('5555555555666777888999000'))    