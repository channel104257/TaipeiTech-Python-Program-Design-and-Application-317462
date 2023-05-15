def binary(n):
    if n <= 1:
        return [n]
    else:
        binary_list = binary(n // 2)
        binary_list.append(n % 2)
        return binary_list

result_matrix = []

for i in range(1, 16):
    binary_list = binary(i)
    result_matrix.append(binary_list)

for i, binary_list in enumerate(result_matrix, 1):
    binary_str = ''.join(str(bit) for bit in binary_list)
    print(f"{i:>2} 的二進制為：{binary_str:0>4}")

