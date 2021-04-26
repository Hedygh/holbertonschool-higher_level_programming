#include "lists.h"
/**
 * check_cycle - check for infinite loop or cycle
 * @list: list to check
 * Return: 0 for infinite loop else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *tmpcheck = list;

	if (list == NULL)
		return (0);

	while (temp != NULL && temp->next)
	{
		tmpcheck = tmpcheck->next;
		temp = temp->next->next;
		if (tmpcheck == temp)
			return (1);
	}
	return (0);
}
