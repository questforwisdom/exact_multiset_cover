#include "quad_linked_list.h"

/*--------------------------------------------------------------------
 * These are the only pieces that need to be changed if the payload
 * data changes:
 */

data_type create_data(int internal_data, int multiplicity, struct node *list_data) {
    data_type new_data = malloc(sizeof *new_data);
    new_data->counter = internal_data;
    new_data->multiplicity = multiplicity;
    new_data->list_data = list_data;
    return new_data;
}

void delete_data(data_type data_obj) {
    free(data_obj);
}

/*------------------------------------------------------------------*/

list create_empty_list(void) {
    return NULL;
}

node_ptr create_node(data_type data) {
    node_ptr new_node_ptr = malloc(sizeof *new_node_ptr);
    if (new_node_ptr != NULL) {
        new_node_ptr->data  = data;
        new_node_ptr->left  = new_node_ptr;
        new_node_ptr->right = new_node_ptr;
        new_node_ptr->up    = new_node_ptr;
        new_node_ptr->down  = new_node_ptr;
    }
    return new_node_ptr;
}

bool is_empty(list l) {
    return l == NULL;
}

bool not_empty(list l) {
    return !(is_empty(l));
}

void set_data(node_ptr N, data_type data) {
    N->data = data;
}

void set_left(node_ptr N, node_ptr left) {
    N->left = left;
}

void set_right(node_ptr N, node_ptr right) {
    N->right = right;
}

void set_up(node_ptr N, node_ptr up) {
    N->up = up;
}

void set_down(node_ptr N, node_ptr down) {
    N->down = down;
}

void set_dangling_next(node_ptr N, node_ptr dangling_next) {
    N->dangling_next = dangling_next;
}

void set_dangling_previous(node_ptr N, node_ptr dangling_previous) {
    N->dangling_previous = dangling_previous;
}

data_type get_data(node_ptr N) {
    return N->data;
}

struct node *get_left(node_ptr N) {
    return N->left;
}

struct node *get_right(node_ptr N) {
    return N->right;
}

struct node *get_up(node_ptr N) {
    return N->up;
}

struct node *get_down(node_ptr N) {
    return N->down;
}

struct node *get_dangling_next(node_ptr N) {
    return N->dangling_next;
}

struct node *get_dangling_previous(node_ptr N) {
    return N->dangling_previous;
}

// Inserts at current cursor.
// Returns pointer to new node.
// Does not affect vertical pointers.
list insert_horizontally(list orig_list, node_ptr new_node_ptr) {
    if (not_empty(new_node_ptr) && not_empty(orig_list)) {
        new_node_ptr->right     = orig_list;
        new_node_ptr->left      = orig_list->left;
        orig_list->left->right  = new_node_ptr;
        orig_list->left         = new_node_ptr;
    }

    return new_node_ptr;
}

// Inserts after node pointed to by current cursor.
// Returns pointer to new node.
// Does not affect vertical pointers.
list insert_horizontally_after (list orig_list, node_ptr new_node_ptr) {
    if (not_empty(orig_list))
        orig_list = get_right(orig_list);

    return insert_horizontally(orig_list, new_node_ptr);
}

// Inserts at current cursor.
// Returns pointer to new node.
// Does not affect horizontal pointers.
list insert_vertically(list orig_list, node_ptr new_node_ptr) {
    if (not_empty(new_node_ptr) && not_empty(orig_list)) {
        new_node_ptr->down  = orig_list;
        new_node_ptr->up    = orig_list->up;
        orig_list->up->down = new_node_ptr;
        orig_list->up       = new_node_ptr;
    }

    return new_node_ptr;
}

// Inserts after node pointed to by current cursor.
// Returns pointer to new node.
// Does not affect horizontal pointers.
list insert_vertically_after (list orig_list, node_ptr new_node_ptr) {
    if (not_empty(orig_list))
        orig_list = get_down(orig_list);

    return insert_vertically(orig_list, new_node_ptr);
}

list insert_dangling_after(list orig_list, node_ptr new_node_ptr) {
    if (not_empty(new_node_ptr) && not_empty(orig_list)) {
        orig_list = get_dangling_next(orig_list);
        new_node_ptr->dangling_next                 = orig_list;
        new_node_ptr->dangling_previous             = orig_list->dangling_previous;
        orig_list->dangling_previous->dangling_next = new_node_ptr;
        orig_list->dangling_previous                = new_node_ptr;
    }

    return new_node_ptr;
}

list new_dangling_stack(node_ptr new_node_ptr) {
    if (not_empty(new_node_ptr)) {
        new_node_ptr->dangling_next     = new_node_ptr;
        new_node_ptr->dangling_previous = new_node_ptr;
    }

    return new_node_ptr;
}

//
// Returns pointer to right node, or NULL if there's only one node.
// General usage would be: saved_N = N; L = cover(N);
node_ptr cover_horizontally(node_ptr N) {
    if (not_empty(N) && (N->right != N)) {
        N->right->left = N->left;
        N->left->right = N->right;
        return N->right;
    } else
        return NULL;
}

// Returns pointer to down node, or NULL if there's only one node.
// General usage would be: saved_N = N; L = cover(N);
node_ptr cover_vertically(node_ptr N) {
    if (not_empty(N) && (N->down != N)) {
        N->down->up = N->up;
        N->up->down = N->down;
        return N->down;
    } else
        return NULL;
}

void cover_row(list row) {
    list next, other_col;
    for (next = row; (next = get_right(next)) != row; ) {
        other_col = get_data(next)->list_data;
        cover_vertically(next);
        get_data(other_col)->counter -= 1;
    }
}

void uncover_row(list row) {
    list next, other_col;
    for (next = row; (next = get_left(next)) != row; ) {
        other_col = get_data(next)->list_data;
        get_data(other_col)->counter += 1;
        uncover_vertically(next);
    }
}

void cover_column(list col, list selected_row) {
    list row, stack;
    get_data(col)->multiplicity -= get_data(selected_row)->multiplicity;
    if (get_data(col)->multiplicity == 0) {
        cover_horizontally(col);
        for (row = col; (row = get_down(row)) != col; ) {
            if (row != selected_row) { // selected row is removed through cover_column calls for the other columns
                cover_row(row);
            }
        }
    }
    else {
        cover_vertically(selected_row);
        get_data(col)->counter -= 1;
        stack = new_dangling_stack(selected_row);
        // TODO: currently, duplicate solutions may be found: the current column can e.g. be covered by one row with m=2 and one with m=3, then all_solutions will pick e.g. m=2 first and then m=3 and during a later iteration (i.e. sibling level in the search tree?) m=3 first and then m=2
        for (row = col; (row = get_down(row)) != col; ) {
            if (get_data(row)->multiplicity > get_data(col)->multiplicity && row != selected_row) {
                cover_vertically(row);
                cover_row(row);
                get_data(col)->counter -= 1;
                stack = insert_dangling_after(stack, row);
            }
        }
    }
    return;
}

void uncover_column(list col, list selected_row) {
    list row;
    if (get_data(col)->multiplicity == 0) {
        for (row = col; (row = get_up(row)) != col; ) {
            if (row != selected_row) {
                uncover_row(row);
            }
        }
        uncover_horizontally(col);
    }
    else {
        for (row = selected_row; (row = get_dangling_previous(row)) != selected_row; ) {
            uncover_row(row);
            uncover_vertically(row);
            get_data(col)->counter += 1;
        }
        get_data(col)->counter += 1;
        uncover_vertically(selected_row);
    }
    get_data(col)->multiplicity += get_data(selected_row)->multiplicity;
    return;
}


// General usage would be: uncover(N); L = N;
// This should work even if L was NULL before N is uncovered.
void uncover_horizontally(node_ptr N) {
    N->right->left = N;
    N->left->right = N;
}

// General usage would be: uncover(N); L = N;
// This should work even if L was NULL before N is uncovered.
void uncover_vertically(node_ptr N) {
    N->down->up = N;
    N->up->down = N;
}

// Returns pointer to right node, or NULL if there's only one node.
node_ptr delete_return_right(node_ptr N) {
    node_ptr next = cover_horizontally(N);
    cover_vertically(N);
    free(N->data);
    free(N);
    return next;
}

// Returns pointer to down node, or NULL if there's only one node.
node_ptr delete_return_down(node_ptr N) {
    node_ptr next = cover_vertically(N);
    cover_horizontally(N);
    free(N->data);
    free(N);
    return next;
}

// These two are almost identical, but abstracting out the similarities
// creates confusing code and adds no benefit.  They're also similar
// to delete, but slightly faster.
void destroy_column_unsafely (list column) {
    // Frees the column data, but DOES NOT fix the left and right
    // neighbors of deleted nodes.
    list rest, orig_column = column;
    while (not_empty(column)) {
        rest = get_down(column);
        if (rest == orig_column) rest = NULL;   // base case
        free(column->data);
        free(column);
        column = rest;
    }
    return;
}

void destroy_entire_grid (list grid) {
    list rest, orig_grid = grid;
    while (not_empty(grid)) {
        rest = get_right(grid);
        if (rest == orig_grid) rest = NULL;     // base case
        destroy_column_unsafely(grid);
        grid = rest;
    }
    return;
}
