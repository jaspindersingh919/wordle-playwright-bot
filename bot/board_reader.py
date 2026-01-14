def read_feedback_from_board(page, attempt):
    """
    Reads feedback from the Wordle board using the tile data-state values.
    Returns a list of 5 strings (correct / present / absent),
    or None if the row is not ready yet.
    """

    states = page.evaluate(
        """(attempt) => {
            // Get the Wordle board
            const board = document.querySelector('.Board-module_board__jeoPS');
            if (!board) return null;

            // Each row is a group
            const rows = board.querySelectorAll('[role="group"]');
            const row = rows[attempt];
            if (!row) return null;

            // Each tile has a data-state attribute
            const tiles = row.querySelectorAll('[data-testid="tile"]');
            if (tiles.length !== 5) return null;

            const result = [];
            for (const tile of tiles) {
                result.push(tile.getAttribute("data-state"));
            }

            return result;
        }""",
        attempt
    )

    # If nothing was returned, the board isn't ready yet
    if not states:
        return None

    # Tiles start as "empty" and change after animation
    if any(state == "empty" for state in states):
        return None

    return states