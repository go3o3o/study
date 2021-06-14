function bubbleSort(array) {
  for (let i = 0; i < array.length; i++) {
    let swap;
    for (let j = 0; j < array.length - 1 - i; j++) {
      if (array[j] > array[j + 1]) {
        swap = array[j];
        array[j] = array[j + 1];
        array[j + 1] = swap;
      }
    }
    console.log(`${i} 회전: ${array}`);
    if (!swap) break;
  }
  return array;
}

array = [5, 4, 3, 2, 1];
console.log(bubbleSort(array));
