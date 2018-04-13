def merge(a, b):
  if not a or not b:
    return b or a
  
  result = []
  i, j = 0, 0
  while len(result) < len(a) + len(b):
    if a[i] < b[j]:
      result.append(a[i])
      i += 1
    else:
      result.append(b[j])
      j += 1
      
    if i == len(a) or j == len(b):
      result.extend(a[i:] or b[j:])
      break
    
  return result

def merge_sort(L):
  if len(L) < 2:
    return L[:]
  else:
    mid = len(L)//2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)

num_list = [1, 5, 19, 10, 2, 15, 8, 4, 3]
print(merge_sort(num_list))