immutable_var = 1, 2, "a", "b"
print(immutable_var)
#immutable_var[0] = 8 # Выдает ошибку. Так как кортеж не изменяется и служит для храниляща данных именно таких которые мы не хотим менять.
                    # И еще кортеж занимает меньше памяти, нежали списки
mutable_list = [1, 2, "a", "b", "car", "dog"]
print(mutable_list[0])
mutable_list[4]='mouse'
print(mutable_list)
mutable_list.append('Modified')
print(mutable_list)
