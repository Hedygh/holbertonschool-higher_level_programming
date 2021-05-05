#include "lists.h"
#include <stdio.h>
/**
 * listint_len - count length of list
 * @h: list
 * Return: length of list
 */
size_t listint_len(const listint_t *h)
{
	int i = 0;

	while (h != NULL)
	{
		h = h->next;
		i++;
	}
	return (i);
}
/**
 * is_palindrome - check if linked list is palindrome
 * @head: linked list
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int length = listint_len(tmp);
	int i = 0;
	int j = 0;
	int tab[2048];

	if (!*head)
		return (1);
	if (length == 1)
		return (1);
	while (tmp != NULL)
	{
		tab[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	i = 0;
	j = length - 1;
	while (j >= length / 2)
	{
		if (tab[i] != tab[j])
			return (0);
		i++;
		j--;
	}
	return (1);
}
