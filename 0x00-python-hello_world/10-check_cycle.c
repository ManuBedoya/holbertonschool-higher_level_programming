#include "lists.h"
#include <string.h>
#include <stdio.h>
int check_cycle(listint_t *list)
{
	listint_t *aux= list;
	list = list->next;
	while (list != NULL)
	{
		if (list == aux)
			return (1);
		list = list->next;
	}
	return (0);
}