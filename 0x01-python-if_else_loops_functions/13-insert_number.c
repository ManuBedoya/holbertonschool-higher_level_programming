#include "lists.h"
/**
 *insert_node - Insert a node with the number in the correct position
 *@head: Pointer with the head of the list
 *@number: Number
 *Return: Null if fails or the address directtion
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (head == NULL || *head == NULL)
		return (NULL);
	listint_t *node, *aux, *ant;

	aux = *head;
	ant = aux;
	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;
	while (aux != NULL)
	{
		if (number <= aux->n)
		{
			node->next = aux;
			ant->next = node;
			return (node);
		}
		ant = aux;
		aux = aux->next;
	}
	ant->next = node;
	return (node);
}
