#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *is_palindrome - Verify if the list is a palindrome
 *@head: header of the list
 *Return: 0 if not or 1 if is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int count = 0, *temp, i = 0;
	listint_t *aux = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (aux != NULL)
	{
		count++;
		aux = aux->next;
	}
	count--;
	aux = *head;
	temp = malloc(sizeof(int) * count);
	while (aux != NULL)
	{
		temp[i++] = aux->n;
		aux = aux->next;
	}
	for (i = 0; i + 1 != count && i != count; i++, count--)
	{
		if (temp[i] != temp[count])
		{
			free(temp);
			return (0);
		}

	}
	free(temp);
	return (1);
}
