#include "lists.h"
/**
 * check_cycle - checks a linked list for cycles
 * @list: The start of the list
 *
 * Return: 1 if a cycle is found
 * Otherwise return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;
	int found;

	found = 0;
	for (hare = list, tortoise = list; hare != NULL;
		hare = hare->next, tortoise = tortoise->next)
		if (hare == tortoise)
			found = 1;
	if (found)
		return (1);
	return (0);
}

