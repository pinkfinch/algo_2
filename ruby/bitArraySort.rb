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

def find_num_in_arr(arr, num)
  for i in arr
    diff = num - i
    return true if arr.index(diff) != nil
  end
  false
end


def find_num_in_arr2(arr, num)
  i,j = 0, arr.length-1
  while i < j
    if arr[i] + arr[j] == num
      return true
    elsif arr[i] + arr[j] < num
      i += 1
    else
      j -= 1
    end
  end
  false
end

pp(find_num_in_arr2([12, 13, 15, 32, 37, 50, 57, 66, 79, 80], 82))
pp(find_num_in_arr2([12, 13, 15, 32, 37, 50, 57, 67, 79, 80], 81))

#find index of num in sorted array
def binary_search(arr, num)
  start, finish = 0, arr.length-1
  while start <= finish
    mid = (start+finish)/2
    if arr[mid] == num
      return mid
    elsif arr[mid] < num
      start = mid+1
    else
      finish = mid-1
    end
  end
  -1
end
pp(binary_search([1, 22, 33, 45, 56, 59, 71, 74, 77, 82], 77))
pp(binary_search([1, 22, 33, 45, 56, 59, 71, 74, 77, 82], 98))
pp(binary_search([1, 22, 33, 45, 56, 59, 71, 74, 77, 82], 60))

#find prime factor with euclid's algorithm
def euclid(a,b)
  a,b = b,a if b > a
  while b != 0
    tmp = b
    b = a%b
    if b != 0
      a = b
    end
  end
  a
end

pp(euclid(78, 52))
