def even_index_or_value(list):
    result = []
    for index, value in enumerate(list):
      
        if index % 2 == 0 or value % 2 == 0:
            result.append(value)
    return result 