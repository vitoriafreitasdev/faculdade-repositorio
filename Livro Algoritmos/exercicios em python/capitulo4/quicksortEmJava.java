public static void quickSort(int[] values, int left, int right) {
	if (left < right) {
		int index_pivot = partition(values, left, right);
		quickSort(values, left, index_pivot - 1);
		quickSort(values, index_pivot + 1, right);	
	}
}

//--- escolha de pivô aleatório 

public static int partition(int[] values, int left, int right) {
        int range = right - left + 1;
        int rand_pivot_index = (int)(Math.random() * range) + left;

        // troca o valor aleatório escolhido com a primeira posição
        swap(values, left, rand_pivot_index);

        int pivot = values[left];
        int i = left;

        for (int j = left + 1; j <= right; j++) {
            if (values[j] <= pivot) {
                i+=1;
                swap(values, i, j);
            }
        }

        // troca pivot (values[left]) com i.
        swap(values, left, i);
        
        return i; 
    }

