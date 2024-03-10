def bitArraySort(arr)
  i, j = 0, arr.length - 1
  while i < j
    while arr[i] == 0
      i += 1
    end
    while arr[j] == 1
      j -= 1
    end
    if i < j
      arr[i], arr[j] = arr[j], arr[i]
    end
  end
  arr
end

pp bitArraySort([1,0,1,1,1,0,0,0,1])
