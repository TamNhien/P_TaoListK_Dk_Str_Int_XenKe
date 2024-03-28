L = input("Nhập vào danh sách các chuỗi và số nguyên, cách nhau bởi dấu phẩy: ").split(',')

if all(type(L[i]) != type(L[i + 1]) for i in range(len(L) - 1)):
    K = [str(L[i] * L[i + 1]) for i in range(0, len(L), 2)]
    print("List K mới:", K)
else:
    print("Các phần tử trong danh sách L không xen kẽ nhau.")
