#include "lists.h"
#include <string.h>
#include <stdio.h>
/**
 *check_cycle - Check a circule list
 *@list: header of the list
 *Return: 1 or 0 if is or isn't a cicrcule list
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;

	list = list->next;
	while (list != NULL)
	{
		if (list == aux)
			return (1);
		list = list->next;
	}
	return (0);
}
