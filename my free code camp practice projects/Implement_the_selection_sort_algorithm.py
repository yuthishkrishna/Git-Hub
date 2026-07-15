def selection_sort(items):
    # Loop through each position in the list
    for i in range(len(items)):
        # Assume the current position holds the smallest value
        min_index = i

        # Find the smallest value in the remaining unsorted portion
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        # Swap only if a smaller value was found
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]

    return items
