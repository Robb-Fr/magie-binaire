"""Creates the cards in their initial state"""
NB_BITS_1 = 5  # the number of bits for representing the values minus 1
NB_COL = 8
NB_ROWS = 4


class Card:
    """Represents one of the 6 cards"""

    def __init__(self, bit_index: int) -> None:
        if bit_index > 5 or bit_index < 0:
            raise IndexError("Index must be between 0 and 5")
        self.numbers = [0 for _ in range(NB_ROWS * NB_COL)]
        for number in range(NB_ROWS * NB_COL):
            bin_nb = bin(number)[2:]
            bin_nb = "0" * (NB_BITS_1 - len(bin_nb)) + bin_nb
            new_bin = bin_nb[:bit_index] + "1" + bin_nb[bit_index:]
            # print(bin_val, new_bin, int(new_bin, 2))
            self.numbers[number] = int(new_bin, 2)

    def display(self, binary: bool) -> str:
        """Displays the Card"""
        repr_str = ""
        for i in range(NB_ROWS):
            repr_str += "\n"
            for j in range(NB_COL):
                num = self.numbers[i * NB_COL + j]
                bin_num = bin(num)[2:]
                repr_str += (
                    "0" * (NB_BITS_1 + 1 - len(bin_num)) + bin_num + " "
                    if binary
                    else str(num) + (2 - len(str(num))) * " "
                )
                repr_str += " "
            repr_str += "\n"
        return repr_str

# caches the creation of all the cards in the python module        
all_cards: list[Card] = [Card(i) for i in range(6)]