# 4.6. Tables

In this task you will learn how to enhance the accessibility of tables. Use a screen reader to read the table content on the page [before.html](./before.html). Your task is to find accessibility issues and propose solutions to fix them.

<details>
<summary>Hints (How to use screen reader with tables)</summary>

- Locating tables on the page:
  - `VO + Command + T` (macOS) or `Control + Alt + T` (Windows) to navigate to the next table.
  - `VO + U` (macOS) or `Control + Alt + U` (Windows) to open the rotor and then `left/right arrow` to locate tables list
- Reading tables:
  - `VO + Arrows` (macOS) or `Control + Alt + Arrows` (Windows) to navigate through the table cells.
  - `VO + C` (macOS) or `Control + Alt + C` (Windows) to read the current column header.
  - `VO + R` (macOS) or `Control + Alt + R` (Windows) to read the current row header.

</details>

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