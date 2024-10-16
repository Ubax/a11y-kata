# 4.6. Tables

In this exercise, your goal is to improve the accessability of the table on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.06-tables/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.06-tables/before.html)
- [source code](./before.html)
Additionally, you can refer to the [after.html](after.html) file to compare your solutions.

## Hints

<details>
<summary>Hint (How to use screen reader with tables)</summary>

- Locating tables on the page:
  - <kbd>VO + Command + T</kbd> (macOS) or <kbd>Control + Alt + T</kbd> (Windows) to navigate to the next table.
  - <kbd>VO + U</kbd> (macOS) or <kbd>Control + Alt + U</kbd> (Windows) to open the rotor and then <kbd>left/right arrow</kbd> to locate tables list
- Reading tables:
  - <kbd>VO + Arrows</kbd> (macOS) or <kbd>Control + Alt + Arrows</kbd> (Windows) to navigate through the table cells.
  - <kbd>VO + C</kbd> (macOS) or <kbd>Control + Alt + C</kbd> (Windows) to read the current column header.
  - <kbd>VO + R</kbd> (macOS) or <kbd>Control + Alt + R</kbd> (Windows) to read the current row header.

</details>

TODO: Hints are missing

## Problems & solutions

<details>
<summary>Problem 1</summary>

There are no headers for the table columns. This makes it hard for screen reader users to understand the content of each cell.

</details>
<details>
<summary>Solution for problem 1</summary>

Use `<th>` tags with `scope="col"` to define the headers for the columns.

```html
<tr>
  <th scope="col" rowspan="2">Currency</th>
  <th scope="colgroup" colspan="5">October 2024</th>
  <th scope="colgroup" colspan="2">September 2024</th>
</tr>
<tr>
  <th scope="col">7th</th>
  ...
  <th scope="col">27th</th>
</tr>
```

</details>

<details>
<summary>Problem 2</summary>

There are no headers for the table rows. This makes it hard for screen reader users to understand the content of each cell.

</details>
<details>
<summary>Solution for problem 2</summary>

Use `<th>` tags with `scope="row"` to define the headers for the rows.

```html
<tr>
  <th scope="row">USD</th>
  <td>1.0982</td>
  ...
  <td>1.1158</td>
</tr>
...
```

</details>

<details>
<summary>Problem 3</summary>

Caption is missing for the table. A caption provides a name for a table, which helps screen reader users locate and understand the table content.

</details>
<details>
<summary>Solution for problem 3</summary>

There are several ways to fix this issue:

- Use `aria-labelledby` attribute to reference the caption element.
  ```html
  <h2 id="currency-exchange-rate">Currency Exchange Rates</h2>
  <table aria-labelledby="currency-exchange-rate">
    ...
  </table>
  ```
- Use `<caption>` element to provide a name for the table.
  ```html
  <table>
    <caption>
      <h2>Currency Exchange Rates</h2>
    </caption>
    ...
  </table>
  ```

</details>

## Resources

- [Tables tutorial on W3 page](https://www.w3.org/WAI/tutorials/tables/)
- [WCAG 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships)
- [`<table>` tag documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)

TODO: add resources
