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

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	aux = *head;
	ant = aux;
	aux = ant->next;
	if (number <= ant->n)
	{
		node->next = ant;
		*head = node;
		return (node);
	}
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
