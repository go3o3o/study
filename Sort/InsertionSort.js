function insertionSort(array) {
  for (let i = 0; i < array.length; i++) {
    let cur = array[i];
    let left = i - 1;

    while (left >= 0 && array[left] > cur) {
      array[left + 1] = array[left];
      left--;
    }
    array[left + 1] = cur;
    console.log(`${i} 회전: ${array}`);
  }
  return array;
}

array = [5, 4, 3, 2, 1];
console.log(insertionSort(array));
