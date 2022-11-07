int main(void)
{
  float *pointer; 
  int i, size, number, option, increment;
  size = 22;
  pointer = (float *) malloc(size * sizeof(float));
  
  for (i = 0; i < size; i++)
  {
    printf("\nInsira um valor para a posição: ", i+1);
    scanf("%f",&pointer[i]);
  }
  
  printf("\nDeseja incrementar algum número?: ");
  printf("\n1 - Sim");
  printf("\n2 - Não\n");
  scanf("%d", &option);

  if (option == 1)
  {
    printf("Quantos números você deseja incrementar?: ");
    scanf("%d", &number);
    
    increment = number + size;

    pointer = (float *) realloc(pointer, increment * sizeof (float));
    for (i = i; i < increment; i++)
  {
    printf("\nInsira um valor para a posição: ", i+1);
    scanf("%f",&pointer[i]);
  }

  }
  else
  {
    increment = size;
  }

  for (i = 0;i < increment; i++)
  {
    printf("%.2f\n",pointer[i]);
  }
  
  free(pointer);
  getch();
  return 0;
}
