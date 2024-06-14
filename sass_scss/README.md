# Sass and Scss Project

This project contains various Sass and Scss files to practice and demonstrate skills in writing and compiling Sass/Scss code.

## File List and Descriptions

1. **0-debug_log.scss**
   - **Description:** A Sass file that prints "Hello world" in the debug output.

2. **1-color_variable.scss**
   - **Description:** A Sass file that assigns the text color `#3D3D3D` to the HTML tags `body` and `p` using a Sass variable.

3. **2-color_variables.scss**
   - **Description:** A Sass file that assigns the text color `#3D3D3D` to the HTML tags `body` and `p`, and the background color `#6D6D6D` to the HTML tags `body` and `h2` using two Sass variables.

4. **3-nested_tag.scss**
   - **Description:** A Sass file that assigns no margin or padding to the `body` tags and a margin of `10px` to all `p` tags inside `body` tags using nested declarations.

5. **4-nested_class.scss**
   - **Description:** A Sass file that assigns the text color `#3D3D3D` to elements inside `body` tags and the text color `#FF0000` to any elements with the class `.red` inside `body` tags using nested declarations.

6. **5-nested_child.scss**
   - **Description:** A Sass file that assigns the text color `#3D3D3D` to elements inside `body` tags and the text color `#FF0000` to any elements with the class `.red` that are the first children of the `body` using nested declarations.

7. **6-nested_hover.scss**
   - **Description:** A Sass file that assigns the text color `#FF0000` to `button` tags and changes the text color to `#00FF00` when the user hovers over the `button` tags using nested declarations.

8. **7-nested_deeper.scss**
   - **Description:** A Sass file that assigns a font size of `14px` to all `body` tags, a font size of `16px` to all `h1` tags inside `body` tags, and a font size of `12px` to `h1` tags of class `.smaller` inside `body` tags using nested declarations.

9. **8-mixin_margins.scss**
   - **Description:** A Sass file that assigns margin left and right at `10px` to `body` tags and margin left and right at `15px` to `div` tags using a mixin.

10. **9-extend_list.scss**
    - **Description:** A Sass file that assigns a font size of `12px` to all tags of class `.info`, a text color of `#00FF00` to all tags of class `.success` while extending the style of the class `.info`, and a text color of `#FF0000` to all tags of class `.warning` while extending the style of the class `.info`.

11. **10-colors.scss**
    - **Description:** A Sass file that defines the color variables `$red`, `$green`, and `$blue`.

12. **10-import_colors.scss**
    - **Description:** A Sass file that assigns text colors to the classes `.red`, `.green`, and `.blue` using the imported color variables from `10-colors.scss`.

13. **11-photos.scss**
    - **Description:** A Sass file that defines the list of names `$list-names`.

14. **11-loop_photos.scss**
    - **Description:** A Sass file that creates a class for each name in the list `$list-names` and assigns the background image based on the name using `@import` and `@each` statement.

15. **12-loop_header.scss**
    - **Description:** A Sass file that creates `h1` to `h5` tags with font sizes ranging from `1px` to `5px` using `@for` statement.

16. **100-loop_col.scss**
    - **Description:** A Sass file that creates `.col-1` to `.col-4` classes with different widths using `@for` statement.

17. **101-media_query.scss**
    - **Description:** A Sass file that applies different font sizes to `h1` tags based on screen width using `@media` query.

18. **102-media_query.scss**
    - **Description:** A Sass file that applies different font sizes to `h1` tags and color to `h1.small` tags based on screen width using `@media` query.

19. **103-sort_list.scss**
    - **Description:** A Sass file that sorts the variable `$list_to_sort` and prints the sorted list in the debug output.

## How to Use

To compile these Sass files, make sure you have Sass installed. You can compile each file individually using the following command:

```sh
sass <filename>.scss

For example, to compile 0-debug_log.scss, run:

sass 0-debug_log.scss

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
