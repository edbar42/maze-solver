import window
import shape


def main():
    win = window.Window(1920, 1080)
    # Cell( coords, left, right, top, bottom
    cell1 = shape.Cell(30, 30, 100, 100, True, True, True, False)
    cell2 = shape.Cell(30, 100, 100, 160, True, True, False, True)

    win.draw_cell(cell1, "black")
    win.draw_cell(cell2, "blue")

    cell1.draw_path(cell2, win.canvas, "red")

    win.wait_for_close()


if __name__ == "__main__":

    main()
