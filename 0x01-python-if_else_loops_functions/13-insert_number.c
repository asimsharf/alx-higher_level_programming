#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 *
 * Return: pointer to the new node, or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current;

    if (!head)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    new->n = number;

    if (!*head || (*head)->n >= number)
    {
        new->next = *head;
        *head = new;
        return (new);
    }

    current = *head;
    while (current->next && current->next->n < number)
        current = current->next;

    new->next = current->next;
    current->next = new;

    return (new);
}
