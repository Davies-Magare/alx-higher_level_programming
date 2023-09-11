#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: The start of the list
 * @number: The number to insert
 *
 * Return: On success, the address of the new node
 * Otherwise return NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *temp2;
	int descending = 0, index, count;
	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (*head = NULL)
	{
		new_node->next = NULL;
		return (new_node);
	}
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if ((*head)->n > (*head)->next->n)
		descending = 1;
	index = find_index(*head, descending, number);
	if (index == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	if (index != -1)
		index -= 1;
	for (temp = *head, count = 0; temp != NULL; temp = temp->next, count++)
	{
		if (count == index)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			break;
		}
		else if (index == -1)
		{
			temp2 = add_nodeint_end(head, number);
			return (temp2);
		}
	}
	return (new_node);
}
/**
 * find_index - finds the position to insert the new number
 * @head: A pointer to the node at the beginning of the list
 * @descending: A flag to indicate whether a list is sorted in descending
 * or ascending order
 * @number: The number to insert
 * Return: The position to insert the number
 * -1 is returned if the node is to be inserted at the end of the list.
 */
int find_index(listint_t *head, int descending, int number)
{
	listint_t *temp;
	int index;

	for (temp = head, index = 0; temp != NULL; temp = temp->next, index++)
	{
		if (descending)
		{
			if (temp->n < number)
				break;
		}
		else
		{
			if (temp->n > number)
				break;
		}
	}
	if (temp == NULL)
		index = -1;
	return (index);
}
