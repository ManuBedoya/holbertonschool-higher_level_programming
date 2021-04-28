#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - Insert a node
 *@head: Header of the list
 *@number: Number
 *Return: Null if fails or the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *aux, *ant;

	if (head == NULL || *head == NULL)
		return (NULL);
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
