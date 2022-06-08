#include "lists.h"

/**
* reverse - reverses the second half of the list
* @hr: head of second_half
* Return: nothing
*/

void reverse(listint_t **hr)
{
	listint_t *prv;
	listint_t *curr;
	listint_t *nxt;
	prv = NULL;
	curr = *hr;
	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prv;
		prv = curr;
		curr = nxt;
	}
	*hr = prv;
}
/**
* compare - compares each int of the list
* @h1: head of the first half
* @h2: head of the second half
* Return: 1 if are equals, 0 if not
*/
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;
	tmp1 = h1;
	tmp2 = h2;
	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
			return (0);
	}
	if (tmp1 == NULL && tmp2 == NULL)
		return (1);
	return (0);
}
/**
* is_palindrome - checks if a singly linked list
* is a palindrome or not
* @head: pointer that point to the head of list
* Return: 0 if it is not a palindrome,1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scan_half, *middle;
	int i;
	slow = fast = prev_slow = *head;
	middle = NULL;
	i = 1;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}
		scan_half = slow;
		prev_slow->next = NULL;
		reverse(&scan_half);
		i = compare(*head, scan_half);
		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scan_half;
		}
		else
			prev_slow->next = scan_half;
	}
	return (i);
}
