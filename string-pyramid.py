"""String Pyramid challange : http://www.codewars.com/kata/string-pyramid/train/python."""


def watch_pyramid_from_the_side(characters):
    """Create visual of side of pyramid."""
    reversed_characters = characters[::-1]
    output_string = ''
    last_index = len(characters) - 1

    for current_index, ch in enumerate(reversed_characters):
        padding = last_index - current_index
        char_repeats = (2 * (current_index + 1)) - 1
        output_string += ' ' * padding + ch * char_repeats + ' ' * padding + '\n'

    return output_string[:-1]


def count_visible_characters_of_the_pyramid(characters):
    """Count visible letters from top view."""
    return ((len(characters) * 2 - 1)**2)


def count_all_characters_of_the_pyramid(characters):
    """Count all tiles required to create pyramid."""
    reversed_characters = characters[::-1]
    output_list = []

    for current_index, ch in enumerate(reversed_characters):
        char_repeats = (2 * (current_index + 1)) - 1
        output_list.append(ch * char_repeats)
    count = 0
    for i in output_list:
        count += len(i)**2
    return count


def watch_pyramid_from_above(characters):
    """Create a top down view of pyramid."""
    reversed_characters = characters[::-1]
    output_list = []

    for current_index, ch in enumerate(reversed_characters):
        char_repeats = (2 * (current_index + 1)) - 1
        output_list.append(ch * char_repeats)
    output_list = output_list[::-1]
    temp_first = output_list[0]
    length = 1
    for string_idx in range(1, len(output_list)):
        temp = temp_first[0:length]
        temp += output_list[string_idx]
        temp += temp_first[-(length):]
        output_list[string_idx] = temp
        temp_first = temp
        length += 1
    output_list.extend(output_list[-2::-1])
    output_string = output_list[0]
    for string_idx in range(1, len(output_list)):
        output_string += '\n' + output_list[string_idx]
    return output_string

    if __name__ == '__main__':
        print(watch_pyramid_from_the_side('abcde'))
        print(count_visible_characters_of_the_pyramid('abcde'))
        print(count_all_characters_of_the_pyramid('abcde'))
        print(watch_pyramid_from_above('abcde'))
        print(watch_pyramid_from_the_side('abc'))
        print(count_visible_characters_of_the_pyramid('abc'))
        print(count_all_characters_of_the_pyramid('abc'))
        print(watch_pyramid_from_above('abc'))
